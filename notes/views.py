from django.shortcuts import render
from .models import Notes
from .serialisers import NoteSerialisers, NotesManualSerialisers
from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class NoteViewsets(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesManualSerialisers

# def hello(request):
#     if request.method =="GET":
#         return JsonResponse({"message": "Hello!"})
#     return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def hello(request):
    if request.method == "GET":
        notes = Notes.objects.all()
        serialisers = NoteSerialisers(notes, many=True)
        return JsonResponse(serialisers.data, safe=False)

    elif request.method == "POST":
        data = json.load(request.body)
        serialisers = NoteSerialisers(data=data)
        if serialisers.is_valid():
            serialisers.save()
            return JsonResponse(serialisers.data, status= 201)
        return JsonResponse(serialisers.errors, status=400)
