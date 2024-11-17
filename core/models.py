import cloudinary
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='projects/')
    source_code_url = models.URLField(blank=True)
    site_url = models.URLField(blank=True)

    detail = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Delete the old image from Cloudinary if a new image is uploaded
        if self.pk:
            old_image = Project.objects.filter(pk=self.pk).first().image
            if old_image and old_image.name != self.image.name:
                cloudinary.uploader.destroy(old_image.name)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the image from Cloudinary
        if self.image:
            cloudinary.uploader.destroy(self.image.name)
        super().delete(*args, **kwargs)


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    quote = models.TextField()
    avatar = models.ImageField(upload_to='testimonials/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Delete the old image from Cloudinary if a new image is uploaded
        if self.pk:
            old_image = Testimonial.objects.filter(pk=self.pk).first().avatar
            if old_image and old_image.name != self.avatar.name:
                cloudinary.uploader.destroy(old_image.name)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the image from Cloudinary
        if self.avatar:
            cloudinary.uploader.destroy(self.avatar.name)
        super().delete(*args, **kwargs)
