from django.urls import path

from .views import ContactViewSet, ProjectViewSet, TestimonialViewSet

urlpatterns = [
    path("contact/",
         ContactViewSet.as_view({"post": "send_contact_response"}), name="contact"),

    path('projects/',
         ProjectViewSet.as_view({'get': 'retrieve_all_projects'}), name='project-list'),

    path('testimonials/', TestimonialViewSet.as_view(
        {'get': 'retrieve_all_testimonials'}), name='testimonial-list'),
]
