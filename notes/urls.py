# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import NoteViewsets

# router = DefaultRouter()
# router.register("r", NoteViewsets)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# myapp/urls.py
from django.urls import path
from .views import hello  # Import your view function

urlpatterns = [
    path('hello/', hello, name='hello'),  # Maps to /hello/
]