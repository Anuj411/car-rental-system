# from django.shortcuts import render, redirect
# from django.urls import reverse, reverse_lazy

from django.views.generic import TemplateView, CreateView, FormView, View


class homeView(TemplateView):
    template_name = "customer/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

