from django.shortcuts import render

# Import Models
from .models import Post

# import TemplateView class to create custom AboutPageView class
from django.views.generic import TemplateView

# import List View and details view classes
from django.views.generic import ListView, DetailView

# import create view class and update view  from generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# reverse lazy for prevent not found error
from django.urls import reverse_lazy

# create view class for delete data
class DeleteViewPost(DeleteView):
    model = Post
    template_name = "post_delete.html"
    # if success move that to home page if failed wait
    success_url = reverse_lazy("home")


# Create view class for update data
class UpdateViewPost(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


# Create view class for custome data enty form
class CreateViewPost(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


# Create class based view for HomePageView Inherit ListView
class HomePageView(ListView):
    model = Post
    template_name = "home.html"


# Create class based view for DetailsView inherit from DetailsView
class DetailView(DetailView):
    model = Post
    template_name = "post_details.html"


# Create class based view for AboutPageView
class AboutPageView(TemplateView):
    template_name = "about.html"
