from django.shortcuts import render
from django.http import JsonResponse
from django_datatables_too.mixins import DataTableMixin
from django.db.models import Q
from django.views.generic import TemplateView, View, UpdateView
from app_modules.users.models import BaseUser

from app_modules.car.models import Car
from django.urls import reverse_lazy
from app_modules.users.forms import UserForm


class HomeView(TemplateView):
    template_name = "seller/home.html"


class CarListDataTableView(DataTableMixin, View):
    model = Car

    def get_queryset(self):
        return Car.objects.filter(created_by=self.request.user)

    def _get_actions(self, obj):
        update_url = reverse_lazy('car:update_car', kwargs={'pk': obj.pk})
        delete_url = reverse_lazy('seller:car_list')
        return f'<a href="{update_url}" title="Edit" class="btn btn-primary btn-xs"><i class="fa fa-pencil"></i></a> <a data-title="{obj}" title="Delete" href="{delete_url}" class="btn btn-danger btn-xs btn-delete"><i class="fa fa-trash"></i></a>'

    def _get_image(self, obj):
        return f'<img src="{obj.get_image}" width="100px" height="100px">'

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        if self.search:
            return qs.filter(
                Q(model__icontains=self.search) |
                Q(type__icontains=self.search) |
                Q(company__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        data = []
        for o in qs:
            data.append({
                # 'car_image': self._get_image(o),
                'id': o.id,
                'model': o.model,
                'type': o.type,
                'price': o.price,
                'actions': self._get_actions(o),
            })
        return data

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)


class UpdateProfileView(UpdateView):
    model = BaseUser
    form_class = UserForm
    template_name = "seller/update_profile.html"


class GetProfileImageView(TemplateView):
    template_name = "seller/get_profile_image.html"

    def get(self, request, *args, **kwargs):
        print(request.GET)
        context = super().get_context_data(**kwargs)
        return render(request, self.template_name, context=context)
