from rest_framework import serializers
from menu.models import Menu

#Serializers allows us to convert complex Django complex data structures such as
# querysets or model instances in Python native objects that can be easily converted JSON/XML
# format.

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'description', 'price', 'created', 'updated']