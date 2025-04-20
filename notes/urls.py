# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import NoteViewsets , CategoryViewsets

# router = DefaultRouter()
# router.register("notes", NoteViewsets)
# router.register("categories", CategoryViewsets)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# myapp/urls.py
from django.urls import path
from .views import hello, note_detail_view, get_category_viewsets


urlpatterns = [
    path('hello/', hello, name='hello'), 
    path('category/', get_category_viewsets, name='category'), 
    path('notes/<int:pk>/', note_detail_view),

]