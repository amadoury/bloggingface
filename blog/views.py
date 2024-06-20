from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from .models import Article

from vertexai.preview.generative_models import GenerativeModel, Image
import requests
import markdown
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/amadou/Desktop/bloggingface/service_account.json"



class ListArticleView(generic.ListView):
    model = Article
    template_name = "blog/index.html"
    context_object_name = "list_articles"
    paginate_by = 5


    def get_queryset(self):
        queryset = super().get_queryset()
        # for article in queryset:
        #     article.title = "hello world"  
        return queryset

class DetailArticle(generic.DetailView):
    model = Article
    template_name = 'blog/article.html'

    def get_object(self):
        object = super(DetailArticle, self).get_object()
        object.content = markdown.markdown(object.content)
        return object

def chatbot(request):
    return render(request, 'blog/chat.html')

@csrf_exempt
def prompt(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        model = GenerativeModel('gemini-pro')
        res = model.generate_content(prompt)
        text = res.text
        print(text)
        text = markdown.markdown(text)
        return JsonResponse({'response': text})  
    else : 
        return JsonResponse({'error': 'Invalid request'}, status=400)