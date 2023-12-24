from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter

from django.urls import reverse, reverse_lazy


class CustomAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        if request.user.role == request.user.CUSTOMER:
            path = reverse("customer:home")
        elif request.user.role == request.user.SELLER:
            path = reverse("seller:home")
        return path.format(username=request.user.username)