from django.db import models
from PIL import Image
import boto3
import os
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.models import User
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"


class Item(models.Model):
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="item/images", blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Open the uploaded image file
        img = Image.open(self.image)

        # Resize the image to 1920x1080 pixels
        new_width = 1920
        new_height = 1080
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)

        if resized_img.mode in ("RGBA", "P"):
            resized_img = resized_img.convert("RGB")

        # Save the resized image to a BytesIO buffer
        buffer = BytesIO()
        resized_img.save(buffer, format="JPEG")

        # Create an InMemoryUploadedFile
        resized_image = InMemoryUploadedFile(
            buffer,
            None,
            f"{self.image.name.split('/')[-1]}",
            "image/jpeg",
            buffer.tell(),
            None,
        )

        # Update the model's image field with the resized image
        self.image = resized_image

        super().save(*args, **kwargs)

    # def resize_image(self, original_image, target_width, target_height):
    #     # Open the uploaded image file
    #     img = Image.open(original_image)

    #     # Calculate the new dimensions
    #     aspect_ratio = img.width / img.height
    #     new_width = target_width
    #     new_height = int(target_width / aspect_ratio)

    #     # Resize the image using Lanczos resampling
    #     resized_img = img.resize((new_width, new_height), Image.LANCZOS)

    #     # Save the resized image to a BytesIO buffer
    #     buffer = BytesIO()
    #     resized_img.save(buffer, format="JPEG")

    #     # Create an InMemoryUploadedFile
    #     resized_image = InMemoryUploadedFile(
    #         buffer, None, "resized.jpg", "image/jpeg", buffer.tell(), None
    #     )

    #     return resized_image

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     if settings.DEBUG:
    #         # Your development implementation
    #         img = Image.open(self.image.path)
    #         new_width = 1920
    #         new_height = 1080
    #         resized_img = img.resize((new_width, new_height), Image.LANCZOS)
    #         resized_img.save(self.image.path)
    #     else:
    #         # Your prod implementation
    #         resized_image = self.resize_image(self.image.path, 1920, 1080)
    #         s3 = boto3.client(
    #             "s3",
    #             aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    #             aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    #         )
    #         s3.upload_fileobj(
    #             resized_image,
    #             os.environ.get("AWS_STORAGE_BUCKET_NAME"),
    #             f"item/images/{self.image.name}",
    #         )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Items"
