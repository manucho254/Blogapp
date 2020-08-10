from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView,
    )
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q


class HomeView(LoginRequiredMixin,ListView):
    model = Blog
    template_name = "blog/index.html"
    context_object_name = "my_blogs"
    ordering = ['-entry_date']
    paginate_by = 2

class EntryView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "blog/entry_detail.html"

class CreateEntryVeiw(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "blog/create_entry.html"
    fields = ['entry_title','entry_text','entry_pic']
    success_url = reverse_lazy('blog-home')
    def form_valid(self,form):
        form.instance.entry_author =self.request.user
        return super().form_valid(form)

class UpdateEntryVeiw(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = "blog/create_entry.html"
    fields = ['entry_title','entry_text','entry_pic']
    success_url = reverse_lazy('blog-home')
    def form_valid(self,form):
        form.instance.entry_author =self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.entry_author:
            return True
        return False 

class DeleteEntryVeiw(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.entry_author:
            return True
        return False 

def searchblog(request):
    if request.method == "GET":
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups= Q(entry_title__icontains=query) | Q(entry_text__icontains=query)

            results = Blog.objects.filter(lookups).distinct()

            context={'results':results,
                  'submitbutton':submitbutton
                  }
            return render(request,'blog/index.html', context)
        else:
            return render(request, 'blog/index.html')
    else:
            return render(request, 'blog/index.html')

