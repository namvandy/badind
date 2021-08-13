from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


class ArticleCreationView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'articleapp/create.html'

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'
    form_class = ArticleCreationForm