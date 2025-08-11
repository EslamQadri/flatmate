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
    list_display = ("id", "city_name_en", "city_name_ar", "governorate")
    search_fields = (
        "city_name_en",
        "city_name_ar" "governorate__governorate_name_en",
        "governorate__governorate_name_ar",
    )
    list_filter = ("governorate",)


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("name", "city__city_name_en")
    search_fields = ("name", "city__city_name_en")
    list_filter = ("city",)
    ordering = ("city", "name")
    prepopulated_fields = {"name": ("city",)}
