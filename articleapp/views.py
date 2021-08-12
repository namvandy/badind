from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


class ArticleCreationView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = 'accountapp/hello_world.html'
    template_name = 'articleapp/create.html'
