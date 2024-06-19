from django.urls import path
from django.conf.urls.i18n import set_language
from . import views

urlpatterns = [
    path("", views.ListArticleView.as_view(), name="index"),
    path('set-language/', set_language, name='set_language'),
    path("<int:pk>/", views.DetailArticle.as_view(), name="detail_article")
]