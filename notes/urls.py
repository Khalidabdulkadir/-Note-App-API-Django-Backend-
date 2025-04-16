from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewsets

router = DefaultRouter()
router.register("r", NoteViewsets)

urlpatterns = [
    path('', include(router.urls)),
]