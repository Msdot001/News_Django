from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article

"""
LoginRequiredMixin: Views can only be access by  logged-in user

UserPassesTestMixin: view can only be access when authorised user is confirmed
"""
class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields =("title", "body",)   
    template_name = "article_edit.html"

    def test_func(self): 
        """Only authoruised author can update"""
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        """Only authoruised author can update"""
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model= Article
    template_name = "article_new.html"
    fields = ("title", "body",)

    def form_valid(self, form): # new
        """Setting the author to the current logged-in User"""
        form.instance.author = self.request.user
        return super().form_valid(form)


