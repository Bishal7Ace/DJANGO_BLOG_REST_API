from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.views import APIView
# Create your views here.

class BlogListView(APIView):
    def get(self, request):
        all_blogs = Blog.objects.filter(is_public = True)
        serializer = BlogSerializer(all_blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#GET, PUT, DELETE
class BlogDetailView(APIView):
    def get(self, request, pk):
        blog = Blog.objects.get(is_public = True, pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    def put(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_200_OK)
        
# @api_view(['GET', 'POST'])
# def blog_list(request):
#     if request.method == "GET":
#        all_blogs = Blog.objects.filter(is_public = True)
#        serializer = BlogSerializer(all_blogs, many=True)
#        return Response(serializer.data, status=status.HTTP_200_OK)
   
#     if request.method == "POST":
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','POST', 'DELETE'])
# def blog_detail(request, pk):
#     if request.method == "GET":
#         blog = Blog.objects.get(is_public = True, pk=pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)
    
#     if request.method == "POST":
#         blog = Blog.objects.get(pk=pk)
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == "DELETE":
#         blog = Blog.objects.get(pk=pk)
#         blog.delete()
#         return Response(status=status.HTTP_200_OK)