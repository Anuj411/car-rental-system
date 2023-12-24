from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView
from app_modules.car.models import Car, CarImage
from app_modules.car.forms import CarCreateForm, CarImageCreateForm

from extra_views import CreateWithInlinesView, InlineFormSetFactory, UpdateWithInlinesView

class CarListView(ListView):
    model = Car
    template_name = "car/list_car.html"


class CarImageInline(InlineFormSetFactory):
    model = CarImage
    form_class = CarImageCreateForm
    factory_kwargs = {"extra": 0, "min_num": 1}

class CarCreateView(CreateWithInlinesView):
    model = Car
    form_class = CarCreateForm
    inlines = [CarImageInline]

    template_name = "car/create_car.html"

    def get_success_url(self):
        return reverse_lazy("seller:home")
    
    def forms_valid(self, form, inlines):
        form.save()

        for formset in inlines:
            for form in formset.forms:
                form.save()
        
        return self.get_success_url()
    
    def forms_invalid(self, form, inlines):
        print("Forms :", form.errors)
        for formset in inlines:
            print("Formset :", formset.errors)
        return self.render_to_response(self.get_context_data(form=form, inlines=inlines), status=201)


class CarUpdateView(UpdateWithInlinesView):
    model = Car
    form_class = CarCreateForm
    inlines = [CarImageInline]

    template_name = "car/update_car.html"

    def get_success_url(self):
        return redirect(reverse("seller:home"))
    
    def forms_valid(self, form, inlines):
        # super().forms_valid(form, inlines)
        form.save()

        for formset in inlines:
            for form in formset.forms:
                if form.cleaned_data.get("DELETE") and form.instance.id:
                    form.instance.delete()
                    continue
                if form.is_valid():
                    form.save()
        
        return self.get_success_url()
    
    def forms_invalid(self, form, inlines):
        print("Forms :", form.errors)
        for formset in inlines:
            print("Formset :", formset.errors)
        return self.render_to_response(self.get_context_data(form=form, inlines=inlines), status=201)