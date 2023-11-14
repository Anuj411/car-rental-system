from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView


class homeView(TemplateView):
    template_name = "customer/home.html"