from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer


class StandardPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 120


class BlogViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    # Retrieve all posts with pagination, excluding featured posts
    def retrieve_all_posts(self, request, *args, **kwargs):
        try:
            posts = Post.objects.filter(featured=False).order_by("-updated_at")
            paginator = StandardPagination()
            paginated_posts = paginator.paginate_queryset(posts, request)
            serializer = PostSerializer(paginated_posts, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            print(e)
            return Response(
                {"detail": "An unexpected error occurred while fetching posts."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def retrieve_post_detail(self, request, *args, **kwargs):
        try:
            post = Post.objects.get(slug=kwargs['slug'])
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response(
                {"detail": "Post not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(e)
            return Response(
                {"detail": "An unexpected error occurred while fetching the post detail."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # Retrieve all categories with pagination
    def retrieve_all_categories(self, request, *args, **kwargs):
        try:
            categories = Category.objects.all().order_by("name")
            paginator = StandardPagination()
            paginated_categories = paginator.paginate_queryset(
                categories, request)
            serializer = CategorySerializer(paginated_categories, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            print(e)
            return Response(
                {"detail": "An unexpected error occurred while fetching categories."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # Retrieve posts by category with pagination, excluding featured posts
    def retrieve_posts_by_category(self, request, *args, **kwargs):
        try:
            category = Category.objects.get(slug=kwargs['slug'])
            posts = category.posts.filter(
                featured=False).order_by("-updated_at")
            paginator = StandardPagination()
            paginated_posts = paginator.paginate_queryset(posts, request)
            serializer = PostSerializer(paginated_posts, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Category.DoesNotExist:
            return Response(
                {"detail": "Category not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(e)
            return Response(
                {"detail": "An unexpected error occurred while fetching posts for this category."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def retrieve_featured_post(self, request, *args, **kwargs):
        try:
            post = Post.objects.filter(featured=True).first()
            if post is None:
                return Response(
                    {"detail": "No featured post found."},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(
                {"detail": "An unexpected error occurred while fetching the featured post."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
