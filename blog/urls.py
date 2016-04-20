from django.conf.urls import url, include
from django.contrib import admin

from articles.views import blog_home


urlpatterns = [
    url(r'^$', blog_home),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include("articles.urls")),
]
