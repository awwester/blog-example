from django.conf.urls import url, include
from django.contrib import admin

from articles.views import BlogHomeRedirectView


urlpatterns = [
    url(r'^$', BlogHomeRedirectView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include("articles.urls")),
]
