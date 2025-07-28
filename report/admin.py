from django.contrib import admin

from report.models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "reason", "created_at")
    search_fields = ("post__author__username", "user__username", "reason")
    list_filter = ("reason", "created_at")
    ordering = ("-created_at",)

    