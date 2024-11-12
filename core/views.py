from django.conf import settings
from django.core.mail import BadHeaderError, EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class ContactViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def send_contact_response(self, request, *args, **kwargs):
        data = request.data
        user_email = data.get('email')
        user_name = data.get('name')
        user_message = data.get('message')

        if not user_email or not user_name or not user_message:
            return Response(
                {"error": "All fields are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Prepare context for email templates
        context = {
            "user_name": user_name,
            "user_email": user_email,
            "user_message": user_message,
        }

        # Render HTML templates
        admin_html_content = render_to_string(
            "emails/admin_notification_email.html", context)
        user_html_content = render_to_string(
            "emails/acknowledgment_email.html", context)

        try:
            # Send HTML email to admin
            admin_email = EmailMultiAlternatives(
                subject=f"New Contact Message from {user_name}",
                body=strip_tags(admin_html_content),  # Fallback to plain text
                from_email="notification@izhar.xyz",
                to=[settings.DEFAULT_FROM_EMAIL],
            )
            admin_email.attach_alternative(admin_html_content, "text/html")
            admin_email.send()

            # Send HTML acknowledgment email to user
            user_email_obj = EmailMultiAlternatives(
                subject="Thank you for reaching out!",
                body=strip_tags(user_html_content),  # Fallback to plain text
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user_email],
            )
            user_email_obj.attach_alternative(user_html_content, "text/html")
            user_email_obj.send()

        except BadHeaderError:
            return Response(
                {"error": "Invalid header found."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            {"message": "Message sent successfully!"},
            status=status.HTTP_200_OK
        )
