from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Governorate(models.Model):
    country = models.ForeignKey(
        Country, related_name="governorates", on_delete=models.CASCADE
    )
    governorate_name_ar = models.CharField(max_length=100, null=True, blank=True)
    governorate_name_en = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.governorate_name_en} in {self.country}"


class City(models.Model):
    name = models.CharField(max_length=100)
    governorate = models.ForeignKey(
        Governorate, related_name="cities", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name}, {self.governorate.governorate_name_en}"


class Area(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name="areas", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.city.name}"
