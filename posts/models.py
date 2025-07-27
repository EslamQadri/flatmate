from django.db import models
from user_profile.models import UserProfile
from locations.models import City, Area, Country


class Post(models.Model):

    author = models.ForeignKey(
        UserProfile, related_name="posts", on_delete=models.CASCADE
    )
    country = models.ForeignKey(
        Country,
        related_name="countrys",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    city = models.ForeignKey(
        City, related_name="citys", on_delete=models.CASCADE, null=True, blank=True
    )
    area = models.ForeignKey(
        Area, related_name="area", on_delete=models.CASCADE, null=True, blank=True
    )
    location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    free_spaces = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_type = models.CharField(
        max_length=50, choices=[("bad", "Bad"), ("flat", "Flat"), ("room", "Room")]
    )
    is_completed = models.BooleanField(default=False)
    is_reported = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name="post_images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post_images/")

    def __str__(self):
        return f"Image for {self.post}"

    class Meta:
        ordering = ["-id"]


class FavoritePost(models.Model):
    user = models.ForeignKey(
        UserProfile, related_name="favorite_posts", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, related_name="favorited_by", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "post")

    def __str__(self):
        return f"{self.user.username} favorited {self.post}"
