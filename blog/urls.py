from django.urls import path
from .views import (
    HomeView, 
    EntryView, 
    CreateEntryVeiw, 
    UpdateEntryVeiw, 
    DeleteEntryVeiw,
    SearchResultsView
)

urlpatterns = [
    path("", HomeView.as_view(), name = "blog-home"),
    path('post/<int:pk>/', EntryView.as_view(), name = "post-detail"),
    path('create_entry/',  CreateEntryVeiw.as_view(), name = 'create-entry'),
    path('search/', SearchResultsView.as_view() , name='search_results'),
    path('post/<int:pk>/update/', UpdateEntryVeiw.as_view(), name = "post-update"),
    path('post/<int:pk>/delete/', DeleteEntryVeiw.as_view(), name = "post-delete"),
   
]
