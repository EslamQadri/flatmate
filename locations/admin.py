from django.contrib import admin
from locations.models import Country, City, Area, Governorate


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")
    search_fields = ("name", "code")


@admin.register(Governorate)
class GovernorateAdmin(admin.ModelAdmin):
    list_display = ("id", "governorate_name_ar", "governorate_name_en")


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "governorate")
    search_fields = (
        "name",
        "governorate__governorate_name_en",
        "governorate__governorate_name_ar",
    )
    list_filter = ("governorate",)


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("name", "city")
    search_fields = ("name", "city__name")
    list_filter = ("city",)
    ordering = ("city", "name")
    prepopulated_fields = {"name": ("city",)}
