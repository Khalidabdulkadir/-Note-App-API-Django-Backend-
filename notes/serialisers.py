from rest_framework import serializers
from .models import Notes, Category

class NoteSerialisers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"
    
class Categoryserialisers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
