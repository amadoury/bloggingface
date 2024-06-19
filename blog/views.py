from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views import generic
from .models import Article


class ListArticleView(generic.ListView):
    model = Article
    template_name = "blog/index.html"
    context_object_name = "list_articles"
    paginate_by = 5


    def get_queryset(self):
        queryset = super().get_queryset()
        for article in queryset:
            article.title = "hello world"  
        return queryset

class DetailArticle(generic.DetailView):
    model = Article
    template_name = 'blog/article.html'
