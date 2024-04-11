from rest_framework import serializers
from blog_app.models import Blog

def anime_name_valid(value):
    def validate_name(self, value):
        if len(value)<4:
            raise serializers.ValidationError("Blog Title is Very Short")
        else:
            return value
class BlogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    anime_name = serializers.CharField(validators = [anime_name_valid])
    author = serializers.CharField()
    anime_description = serializers.CharField(validators = [anime_name_valid])
    post_date = serializers.DateField()
    is_public = serializers.BooleanField()
    slug = serializers.CharField()
    class Meta:
        model = Blog
        fields = "__all__"
    
    
    # Field-level validation
    # def validate_anime_name(self, value):
    #     if len(value)<4:
    #         raise serializers.ValidationError("Blog Title is Very Short")
    #     else:
    #         return value
        
    #Object-level Validation
    def validate(self, data):
        if data['anime_name'] == data['anime_description']:
            raise serializers.ValidationError("Blog Title and description can not be same")
        else:
            return data
    
#----------------Simple Serializer-------------
# class BlogSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField()
#     author = serializers.CharField()
#     description = serializers.CharField()
#     post_date = serializers.DateField()
#     is_public = serializers.BooleanField()
#     slug = serializers.CharField()
    
#     def create(self, validated_data):
#         return Blog.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.author = validated_data.get('author', instance.author)
#         instance.description = validated_data.get('description', instance.description)
#         instance.post_date = validated_data.get('post_date', instance.post_date)
#         instance.is_public = validated_data.get('is_public', instance.is_public)
#         instance.slug = validated_data.get('slug', instance.slug)
#         instance.save()
#         return instance