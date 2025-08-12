from django.urls import path
from locations.views import (
    CityListView,
    AreaListView,
    CountryListView,
    GovernorateListView,
    All_LocationsListView,
)

urlpatterns = [
    path("cities/", CityListView.as_view(), name="cities"),
    path("areas/", AreaListView.as_view(), name="areas"),
    path("countries/", CountryListView.as_view(), name="countries"),
    path("governorates/", GovernorateListView.as_view(), name="governorates"),
    path("all/", All_LocationsListView.as_view(), name="all"),
]
