from allauth.account.views import app_settings
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, View, CreateView

from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import REDIRECT_FIELD_NAME

from allauth.account.forms import LoginForm
from allauth.core.exceptions import ImmediateHttpResponse
from allauth.account.utils import get_next_redirect_url
from allauth.utils import get_request_param
from allauth.account.views import (RedirectAuthenticatedUserMixin,
                                    LogoutFunctionalityMixin,
                                    _ajax_response)
from allauth.account.adapter import get_adapter

from app_modules.users.forms import (UserForm, 
                                    SellerForm,
                                    )
from app_modules.seller.models import Seller
from utils.helper import generate_unique_username

from django.contrib.auth import get_user_model
User = get_user_model()

class LoginSignupView(RedirectAuthenticatedUserMixin, TemplateView):
    template_name = "users/base_template.html"
    redirect_field_name = REDIRECT_FIELD_NAME
    success_url = None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["signup_form"] = UserForm
        context["login_form"] = LoginForm
        return context
    
    def get_success_url(self):
        # Explicitly passed ?next= URL takes precedence
        ret = (
            get_next_redirect_url(self.request, self.redirect_field_name)
            or self.success_url
        )
        return ret

class LoginView(RedirectAuthenticatedUserMixin, FormView):
    form_class = LoginForm
    template_name = "users/login.html"
    redirect_field_name = REDIRECT_FIELD_NAME

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
        return render(self.request, "users/base_template.html", context={"login_form":form, "signup_form":UserForm})

class LogoutView(LogoutFunctionalityMixin, TemplateView):
    template_name = "users/logout.html"
    redirect_field_name = REDIRECT_FIELD_NAME

    def get(self, *args, **kwargs):
        if app_settings.LOGOUT_ON_GET:
            return self.post(*args, **kwargs)
        if not self.request.user.is_authenticated:
            response = redirect(self.get_redirect_url())
            return _ajax_response(self.request, response)
        ctx = self.get_context_data()
        response = self.render_to_response(ctx)
        return _ajax_response(self.request, response)

    def post(self, *args, **kwargs):
        url = self.get_redirect_url()
        if self.request.user.is_authenticated:
            self.logout()
        response = redirect(url)
        return _ajax_response(self.request, response)

    def get_context_data(self, **kwargs):
        ctx = kwargs
        redirect_field_value = get_request_param(self.request, self.redirect_field_name)
        ctx.update(
            {
                "redirect_field_name": self.redirect_field_name,
                "redirect_field_value": redirect_field_value,
            }
        )
        return ctx

    def get_redirect_url(self):
        return get_next_redirect_url(
            self.request, self.redirect_field_name
        ) or get_adapter(self.request).get_logout_redirect_url(self.request)


class SignupView(RedirectAuthenticatedUserMixin, FormView):
    form_class = UserForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("users:login_signup")

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.username = generate_unique_username(form.cleaned_data["first_name"])
        new_user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, "users/base_template.html", context={"login_form":LoginForm, "signup_form":form})


class SellerSignupView(RedirectAuthenticatedUserMixin, CreateView):
    form_class = SellerForm
    template_name = "users/seller_signup.html"

    def get_success_url(self):
        return redirect(reverse("users:login_signup"))

    def form_valid(self, form):
        user = form.save(commit=False)
        user.role = User.SELLER
        user.save()
        
        Seller.objects.create(gst_no=form.cleaned_data["gst_no"], user=user)
        return self.get_success_url()