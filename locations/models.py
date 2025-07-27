from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(
        Country, related_name="cities", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name}, {self.country.name}"


class Area(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name="areas", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.city.name}"
