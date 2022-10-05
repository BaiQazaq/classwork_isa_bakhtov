from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ArticleForm
from webapp.models import Article, StatusChoices


def add_view(request):
    form = ArticleForm()
    if request.method == "GET":
        return render(request, 'article_create.html', context={"choices": StatusChoices.choices, 'form': form})
    form = ArticleForm(request.POST)
    if not form.is_valid():
        return render(request, 'article_create.html', context={"choices": StatusChoices.choices, 'form': form})
    article = Article.objects.create(**form.cleaned_data)
    return redirect('article_detail', pk=article.pk)

def detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article.html', context={'article': article})


def update_view(request, pk):
    errors = {}
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        if not request.POST.get('title'):
            errors['title'] = 'Поле обязательно к заполнению'
        article.title = request.POST.get('title')
        article.author = request.POST.get('author')
        article.text =request.POST.get('text')
        article.status =request.POST.get('status')
        if errors:
            return render(
        request,
        'article_update.html',
        context={
            'article': article, 
            'choices': StatusChoices.choices, 
            'errors': errors
            })
        article.save()
        return redirect('article_detail', pk=article.pk)
    return render(
        request,
        'article_update.html',
        context={
            'article': article, 
            'choices': StatusChoices.choices, 
            'errors': errors
            })


def delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return render(request, 'article_confirm_delete.html', context={'article': article})


def confirm_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('index')