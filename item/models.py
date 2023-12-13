from django.db import models
from PIL import Image
from django.contrib.auth.models import User


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
        super().save(*args, **kwargs)

        # Open the uploaded image file
        img = Image.open(self.image.path)

        # Set the new dimensions (1920x1080 pixels)
        new_width = 1920
        new_height = 1080

        # Resize the image using Lanczos resampling
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)

        # Save the resized image back to the original file path
        resized_img.save(self.image.path)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Items"
