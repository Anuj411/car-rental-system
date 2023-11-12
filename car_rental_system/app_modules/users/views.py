from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import REDIRECT_FIELD_NAME

from allauth.account.forms import LoginForm
from allauth.core.exceptions import ImmediateHttpResponse
from allauth.account.utils import get_next_redirect_url

from app_modules.users.forms import CustomSignupForm

class LoginRegistrationView(TemplateView):
    template_name = "users/base_template.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["signup_form"] = CustomSignupForm
        context["login_form"] = LoginForm
        return context


class LoginView(FormView):
    form_class = LoginForm
    template_name = "users/login.html"
    redirect_field_name = REDIRECT_FIELD_NAME

    def get(self, request):
        return redirect("users:register_login")

    def get_form_kwargs(self):
        kwargs = super(LoginView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs
    
    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            return form.login(self.request, redirect_url=success_url)
        except ImmediateHttpResponse as e:
            return e.response
    
    def get_success_url(self):
        # Explicitly passed ?next= URL takes precedence
        ret = (
            get_next_redirect_url(self.request, self.redirect_field_name)
            or self.success_url
        )
        return ret
    
    def form_invalid(self, form):
        return render(self.request, "users/base_template.html", context={"login_form":form, "signup_form":CustomSignupForm})