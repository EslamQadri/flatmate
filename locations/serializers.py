from rest_framework.serializers import ModelSerializer
from locations.models import City,Governorate,Country,Area

class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class GovernorateSerializer(ModelSerializer):
    class Meta:
        model = Governorate
        fields = '__all__'

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class AreaSerializer(ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__' 
class All_LocationsSerializer(ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'
        depth = 3