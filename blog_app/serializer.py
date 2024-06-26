from rest_framework import serializers
from blog_app.models import Blog, Category, BlogComment
from django.urls import reverse

class BlogCommentSerializer(serializers.ModelSerializer):
    blog = serializers.StringRelatedField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = BlogComment
        fields = "__all__"  

# class BlogSerializer(serializers.ModelSerializer):
#     comments = serializers.SerializerMethodField()
#     author = serializers.StringRelatedField(read_only=True)
#     category = serializers.CharField(source='category.category_name') 

#     class Meta:
#         model = Blog
#         fields = "__all__"

#     def get_comments(self, obj):
#         comments = BlogComment.objects.filter(blog=obj)[:3]
#         return BlogCommentSerializer(comments, many=True).data




class BlogSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Blog
        fields = "__all__"
        
    def get_comments(self, obj):
        comments = BlogComment.objects.filter(blog=obj)[:3]
        request = self.context.get('request')
        return {
            "comments": BlogCommentSerializer(comments, many=True).data,
        }
        
class CategorySerializer(serializers.ModelSerializer):
    # category_blogs = BlogSerializer(many=True, read_only=True)  
    category = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = "__all__"
        
        
# class CategorySerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     category_name = serializers.CharField()
#     category = BlogSerializer(many=True, read_only=True)
#     class Meta:
#         model = Category
#         fields = "__all__"

    
# class BlogCommentSerializer(serializers.ModelSerializer):
#     blog = serializers.StringRelatedField(read_only=True)
#     author = serializers.ReadOnlyField(source='author.username')
#     class Meta:
#         model = BlogComment
#         fields = "__all__"
        
        
            
    