from django.contrib import admin
from locations.models import Country, City, Area


# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name", "country__name")
    list_filter = ("country",)


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("name", "city")
    search_fields = ("name", "city__name")
    list_filter = ("city",)
    ordering = ("city", "name")
    prepopulated_fields = {"name": ("city",)}
