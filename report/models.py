from django.db import models

from posts.models import Post
from user_profile.models import UserProfile


class Report(models.Model):
    post = models.ForeignKey(
        Post, related_name="post_reports", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        UserProfile, related_name="user_reports", on_delete=models.CASCADE
    )
    description = models.TextField(null=True, blank=True)
    reason = models.CharField(
        max_length=255, choices=[("spam", "Spam"), ("inappropriate", "Inappropriate")]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report by {self.user.username} on {self.post}"

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("post", "user")
        verbose_name = "Report"
        verbose_name_plural = "Reports"
