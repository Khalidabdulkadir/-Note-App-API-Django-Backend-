from django.shortcuts import render
from .models import Notes , Category
from .serialisers import NoteSerialisers, NotesManualSerialisers , Categoryserialisers
from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404

class NoteViewsets(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesManualSerialisers

class CategoryViewsets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Categoryserialisers

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
    
    
@csrf_exempt
def note_detail_view(request, pk):
    note = get_object_or_404(Notes, pk=pk)

    if request.method == 'GET':
        serializer = NotesManualSerialisers(note)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = json.loads(request.body)
        serializer = NoteSerialisers(note, data= data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)
    
    elif request.method == "DELETE":
        note.delete()
        return JsonResponse({"message": "Note deleted Successfully"}, status = 204)
    


# viewsets  Manual viewsets
@csrf_exempt
def get_category_viewsets(request):
    if request.method == "GET":
        category = Category.objects.all()
        serialiser = Categoryserialisers(category, many=True)
        print(f"The category Object are :{category}")
        print(f"The cateSerialised data are :{serialiser.data}")
        return JsonResponse(serialiser.data, safe=False)
    
    if request.method == "POST":
        data = json.loads(request.body)
        serializers = Categoryserialisers(data=data)

        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=201)
        return JsonResponse(serializers.errors, status=400)
    else:
        return JsonResponse({'error': 'Only GET method is allowed.'}, status=405)
