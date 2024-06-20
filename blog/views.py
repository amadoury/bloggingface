from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import generic
from .models import Article

from vertexai.preview.generative_models import GenerativeModel
import requests
import markdown
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/amadou/Desktop/bloggingface/service_account.json"
 
class ListArticleView(generic.ListView):
    model = Article
    template_name = "blog/index.html"
    context_object_name = "list_articles"
    paginate_by = 5

class DetailArticle(generic.DetailView):
    model = Article
    template_name = 'blog/article.html'

    def get_object(self):
        object = super(DetailArticle, self).get_object()
        object.content = markdown.markdown(object.content)
        return object

def chatbot(request):
    return render(request, 'blog/chat.html')

def prompt(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        model = GenerativeModel('gemini-pro')
        res = model.generate_content(prompt)
        text = markdown.markdown(res.text)
        return JsonResponse({'response': text})  
    else : 
        return JsonResponse({'error': 'Invalid request'}, status=400)