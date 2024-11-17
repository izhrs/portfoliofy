from django.urls import path

from .views import BlogViewSet

urlpatterns = [
    # Blog Post
    path("",
         BlogViewSet.as_view({"get": "retrieve_all_posts"}), name="all-posts"),
    path("<slug:slug>/",
         BlogViewSet.as_view({"get": "retrieve_post_detail"}), name="post-detail"),

    # Blog Category
    path("categories/",
         BlogViewSet.as_view({"get": "retrieve_all_categories"}), name="all-categories"),
    path("category/<slug:slug>/",
         BlogViewSet.as_view({"get": "retrieve_posts_by_category"}), name="posts-by-category"),
]
