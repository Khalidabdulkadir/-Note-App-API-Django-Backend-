from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewsets , CategoryViewsets

router = DefaultRouter()
# router.register("notes", NoteViewsets)

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryViewsets.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryViewsets.as_view(), name='category-detail'),

    # Notes
    path('notes/', NoteViewsets.as_view(), name='notes-list'),
    path('notes/<int:pk>/', NoteViewsets.as_view(), name='notes-detail'),

]
