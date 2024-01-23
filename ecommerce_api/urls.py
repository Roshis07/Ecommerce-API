
from django.urls import path
from .views import ItemListView
urlpatterns = [
    path('ItemList/', ItemListView.as_view(),name='ItemList'),    
]
