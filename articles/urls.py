from django.conf.urls import url

from .views import blog_home, article_detail, article_create, article_delete, \
                   article_update


urlpatterns = [
    url(r'^$', blog_home, name="blog-home"),
    url(r'^(?P<pk>\d+)/$', article_detail, name="article-detail"),

    url(r'^create/$', article_create, name="article-create"),
    url(r'^delete/(?P<pk>\d+)/$', article_delete, name="article-delete"),
    url(r'^update/(?P<pk>\d+)/$', article_update, name="article-update"),
]
