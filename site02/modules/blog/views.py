from typing import Any
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Article, Category


def articles_list(request, page):
    articles = Article.objects.all()
    paginator = Paginator(articles, per_page=2)
    context = {'page_obj': page_object}
    return render(request, 'blog/articles_func_list.html', context)


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/articles_list.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная страница"
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/articles_detail.html'
    context_object_name = 'articles'
    category = None

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Article.objects.all().filter(category_slug=self.category.slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Статьи из категории: {self.object.title}'
        return context


class ArticleByCategoryListView(ListView):

    model = Article

    template_name = 'blog/articles_list.html'

    context_object_name = 'articles'

    category = None

    def get_queryset(self):

        self.category = Category.objects.get(slug=self.kwargs['slug'])

        queryset = Article.objects.all().filter(category__slug=self.category.slug)

        return queryset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['title'] = f'Статьи из категории: {self.category.title}'

        return context
