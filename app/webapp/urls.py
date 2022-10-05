from django.urls import path

from webapp.views.articles import add_view, detail_view, update_view, delete_view, confirm_delete
from webapp.views.base import index_view

urlpatterns = [
    path("", index_view, name='index'),
    path("articles/add/", add_view, name = 'article_add'),
    path("articles/", index_view),
    path("articles/<int:pk>", detail_view, name = 'article_detail'),
    path("articles/<int:pk>/update/", update_view, name= "article_update"),
    path("articles/<int:pk>/delete/", delete_view, name= "article_delete"),
    path("articles/<int:pk>/confirm_delete/", confirm_delete, name= "confirm_delete")
]