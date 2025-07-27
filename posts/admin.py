from django.contrib import admin
from posts.models import Post, PostImage


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "country",
        "city",
        "area",
        "location",
        "description",
        "latitude",
        "longitude",
        "capacity",
        "free_spaces",
        "price",
        "price_type",
        "is_completed",
        "is_reported",
        "created_at",
        "updated_at",
    )
    search_fields = ("author__username", "location", "description")
    list_filter = ("country", "city", "area", "is_completed", "is_reported")
    ordering = ("-created_at",)


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ("post", "image")
    search_fields = ("post__author__username",)
    list_filter = ("post__city",)
    ordering = ("-id",)
    prepopulated_fields = {"image": ("post",)}


