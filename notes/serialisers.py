from rest_framework import serializers
from .models import Notes

class NoteSerialisers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"

# Manual Way 
class NotesManualSerialisers(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    def create(self, validated_data):
        validated_data['title'] = validated_data['title'].upper()
        
        return Notes.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
    # Update the existing instance (the Note object)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
