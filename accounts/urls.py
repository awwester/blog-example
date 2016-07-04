from django.conf.urls import url

from .views import LoginFormView


urlpatterns = [
    url(r'^login/$', LoginFormView.as_view(), name="accounts-login"),
]
