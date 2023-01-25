from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleUpdateView(UpdateView):
    model = Article
    fields =("title", "body",)   # field intend to update
    template_name = "article_update.html"

class ArticleDeleteView(DeleteView):
    model= Article
    template_name = "article_delete"
    success_url = reverse_lazy("article_list")

