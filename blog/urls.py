from django.urls import path
from .views import (
    HomeView, 
    EntryView, 
    CreateEntryVeiw, 
    UpdateEntryVeiw, 
    DeleteEntryVeiw
)
from .views import (searchblog)

urlpatterns = [
    path("", HomeView.as_view(), name = "blog-home"),
    path('post/<int:pk>/', EntryView.as_view(), name = "post-detail"),
    path('create_entry/',  CreateEntryVeiw.as_view(), name = 'create-entry'),
    path('search_blog/', searchblog, name='searchblog'),
    path('post/<int:pk>/update/', UpdateEntryVeiw.as_view(), name = "post-update"),
    path('post/<int:pk>/delete/', DeleteEntryVeiw.as_view(), name = "post-delete"),
   
]
