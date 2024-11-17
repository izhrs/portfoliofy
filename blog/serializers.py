from rest_framework import serializers

from .models import Category, Post, PostContent


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostContent
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    content = PostContentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
