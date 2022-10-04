from django.shortcuts import render

# Import User creation form
from django.contrib.auth.forms import UserCreationForm

# import reverse_lazy
from django.urls import reverse_lazy

# import create view for inherit
from django.views.generic import CreateView

# Create signup views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
