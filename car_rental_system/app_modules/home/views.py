from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView
from app_modules.home.forms import AddressForm


class homeView(TemplateView):
    template_name = "home/home.html"


class addressCreateView(FormView):
    form_class = AddressForm
    template_name = "home/address.html"