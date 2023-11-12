from django import forms
from app_modules.home.models import Country, State, City
from django_select2.forms import ModelSelect2Widget


class AddressForm(forms.Form):
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        label="Country",
        widget=ModelSelect2Widget(
            model=Country,
            search_fields=['name__icontains'],
        )
    )

    state = forms.ModelChoiceField(
        queryset=State.objects.all(),
        label="State",
        widget=ModelSelect2Widget(
            model=State,
            search_fields=['name__icontains'],
            dependent_fields={'country': 'country'},
            max_results=500,
        )
    )