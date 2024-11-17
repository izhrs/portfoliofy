import cloudinary
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False,
                            blank=False, db_index=True)
    description = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # delete old image if new image is uploaded
        if self.pk:
            existing_category = Category.objects.get(pk=self.pk)
            old_image = existing_category.image
            if old_image and old_image.name != self.image.name:
                cloudinary.uploader.destroy(old_image.name)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            cloudinary.uploader.destroy(self.image.name)
        super().delete(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False,
                            blank=False, db_index=True)
    categories = models.ManyToManyField(Category, related_name="posts")
    description = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to='post/')
    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Mark only one post as featured
        if self.featured:
            # Unmark all other posts as featured
            Post.objects.exclude(pk=self.pk).filter(
                featured=True).update(featured=False)

        # delete old image if new image is uploaded
        if self.pk:
            existing_post = Post.objects.get(pk=self.pk)
            old_image = existing_post.image
            if old_image and old_image.name != self.image.name:
                cloudinary.uploader.destroy(old_image.name)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            cloudinary.uploader.destroy(self.image.name)
        super().delete(*args, **kwargs)


class PostContent(models.Model):
    blog = models.ForeignKey(
        Post, related_name="content", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/content/')
    content = models.TextField()

    def __str__(self):
        return f"Section {self.id}"

    def save(self, *args, **kwargs):
        # delete old image if new image is uploaded
        if self.pk:
            existing_post_content = PostContent.objects.get(pk=self.pk)
            old_image = existing_post_content.image
            if old_image and old_image.name != self.image.name:
                cloudinary.uploader.destroy(old_image.name)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            cloudinary.uploader.destroy(self.image.name)
        super().delete(*args, **kwargs)
