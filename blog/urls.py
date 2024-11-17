from django.urls import path

from .views import BlogViewSet

urlpatterns = [
    # Blog Post
    path("posts/",
         BlogViewSet.as_view({"get": "retrieve_all_posts"}), name="all-posts"),
    path("post/featured/",
         BlogViewSet.as_view({"get": "retrieve_featured_post"}), name="featured-posts"),
    path("post/<slug:slug>/",
         BlogViewSet.as_view({"get": "retrieve_post_detail"}), name="post-detail"),

    # Blog Category
    path("categories/",
         BlogViewSet.as_view({"get": "retrieve_all_categories"}), name="all-categories"),
    path("category/<slug:slug>/",
         BlogViewSet.as_view({"get": "retrieve_posts_by_category"}), name="posts-by-category"),
]
