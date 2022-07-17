from rest_framework import serializers
from .models import *

class GoodSerializer(serializers.ModelSerializer):
    """ Список товаров """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Good
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Country
        fields = '__all__'