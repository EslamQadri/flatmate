from locations.models import City, Country, Area
from rest_framework.generics import ListAPIView
from locations.serializers import (
    CitySerializer,
    CountrySerializer,
    AreaSerializer,
    Governorate,
    All_LocationsSerializer,
)
from rest_framework.permissions import IsAuthenticated


class CityListView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CountryListView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class AreaListView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class GovernorateListView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Governorate.objects.all()
    serializer_class = Governorate


class All_LocationsListView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Area.objects.all()
    serializer_class = All_LocationsSerializer
