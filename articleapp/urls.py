from django.urls import path

from articleapp.views import ArticleCreationView

app_name='articleapp'

urlpatterns = [
    path('create/', ArticleCreationView.as_view(), name="create")
]