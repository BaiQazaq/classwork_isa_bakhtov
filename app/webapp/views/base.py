from django.shortcuts import render

from webapp.models import Article


def index_view(request):
    articles = Article.objects.exclude(is_deleted=True)
    context = {
        "articles": articles
    }
    return render(request, 'index.html', context)
