from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import ImproperlyConfigured, PermissionDenied

from .models import Article


class PublicArticlesMixin(object):
    """
    include this mixin to only have public articles available
    """
    queryset = Article.objects.filter(public=True)


class AuthRequiredMixin(object):
    """
    require that a user is authenticated. If the user is not authenticated
    send them to the login page.
    """
    login_url = settings.LOGIN_URL

    def dispatch(self, request, *args, **kwargs):
        """
        check if the user is authenticated. If they are authenticated return the
        normal dispatch. If not, redirect them to login page.
        """
        if not request.user.is_authenticated():
            return redirect_to_login(request.get_full_path(), self.login_url)

        return super(AuthRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class UserAuthorMixin(AuthRequiredMixin):
    """
    Checks that the user is the author of the article. If they are not, return a
    403 error
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated() and request.user.id is not self.get_object().author.id:
            raise PermissionDenied

        return super(UserAuthorMixin, self).dispatch(
            request, *args, **kwargs)
