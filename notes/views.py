from django.shortcuts import render
from .models import Notes , Category
from .serialisers import NoteSerialisers , Categoryserialisers
from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class NoteViewsets(APIView):
    def get(self, request):
        notes = Notes.objects.all()
        serailizers = NoteSerialisers(notes, many=True)
        
        return Response(serailizers.data)
    
    def post(self, request):
        serialisers = NoteSerialisers(data=request.data)
        if serialisers.is_valid():
            serialisers.save()
            return Response(serialisers.data, status=status.HTTP_201_CREATED)
        return Response(serialisers.errors, status=status.HTTP_404_NOT_FOUND)  
    
    def delete(self, request, pk):
        try:
            notes = Notes.objects.get(pk=pk)
            return JsonResponse({"error": "Notes not found"}, status=404)
        
        except Notes.DoesNotExist:
            notes.delete()
            return JsonResponse({"message": "Notes deleted successfully."}, status=204)
        
    def update(self, request, pk):
        try:
            notes = Notes.objects.get(pk=pk)
        except Notes.DoesNotExist:
            return JsonResponse({"error": "Notes not found"}, status=404)

        serializer = NoteSerialisers(notes, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)

        return JsonResponse(serializer.errors, status=400)
 
        
class CategoryViewsets(APIView):
    def get(self, request):
        category = Category.objects.all()
        serialiser = Categoryserialisers(category, many= True)
        return Response(serialiser.data)
    
    def post(self, request):
        serialiser = Categoryserialisers(data=request.data)

        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serialiser = Categoryserialisers(category, data=request.data, partial=True)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return JsonResponse({"error": "Category not found"}, status=404)

        category.delete()
        return JsonResponse({"message": "Category deleted successfully."}, status=204)