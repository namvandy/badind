from django.urls import path

from articleapp.views import ArticleCreationView, ArticleDetailView

app_name='articleapp'

urlpatterns = [
    path('create/', ArticleCreationView.as_view(), name="create"),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name="detail"),
]