from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, \
                                 UpdateView, RedirectView

from .models import Article
from .forms import ArticleForm


class BlogHomeListView(ListView):
    template_name = "articles/articles_home.html"
    model = Article
    paginate_by = 3

    def get_context_data(self, **kwargs):
        "add range template context variable that we can loop through pages"
        context = super(BlogHomeListView, self).get_context_data(**kwargs)
        context['range'] = range(context["paginator"].num_pages)
        return context


class BlogHomeRedirectView(RedirectView):
    url = reverse_lazy('blog-home')


class ArticleDetailView(DetailView):
    template_name = "articles/article.html"
    model = Article


class ArticleCreateView(CreateView):
    template_name = "articles/article_create.html"
    form_class = ArticleForm

    def form_valid(self, form):
        """
        Assign the author to the request.user
        """
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog-home')


class ArticleUpdateView(UpdateView):
    template_name = "articles/article_update.html"
    model = Article
    form_class = ArticleForm
