from rest_framework import serializers
from .models import Notes

class NoteSerialisers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"

# Manual Way 
class NotesManualSerialisers(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(allow_blank =True)

    def create(self, validated_data):
        validated_data['title'] = validated_data['title'].lower()

        if "urgent" in validated_data['title']:
            validated_data["title"] += (" important")
        else:
            print("it doesnt contain")


        if validated_data['content'] == "":
            validated_data['content'] = "No content provided."

        notes = Notes.objects.create(**validated_data)
        print("Note Created :", notes)
        return notes
    

    def update(self, instance, validated_data):
    # Update the existing instance (the Note object)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
