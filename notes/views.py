from django.shortcuts import render
from .models import Notes
from .serialisers import NoteSerialisers, NotesManualSerialisers
from rest_framework import viewsets

class NoteViewsets(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesManualSerialisers
    
