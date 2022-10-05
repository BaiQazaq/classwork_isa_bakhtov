from datetime import *
from django.utils import timezone
from django.db import models
from django.db.models import TextChoices


# Create your models here.
class StatusChoices(TextChoices):
    ACTIVE = 'ACTIVE', 'Активна'
    NOT_ACTIVE = 'NOT_ACTIVE', 'Не Активна'


class Article(models.Model):
    status = models.CharField(verbose_name='Статус', choices=StatusChoices.choices, max_length=100, default=StatusChoices.ACTIVE)
    title = models.CharField(verbose_name='Заголовок',max_length=200, null=False)
    text = models.TextField(verbose_name='Текст', max_length=3000, null=False, blank=False)
    author = models.TextField(verbose_name='Автор', max_length=100, null=False, blank=False, default="No name")
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False, null=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)

    def __str__(self):
        return f"{self.title} - {self.author}"
    
    # class Meta:
    #     verbose_name = 'Статья'
    #     verbose_name_plural = 'Статьи'
        
    
    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()


# class Comment(models.Model):
#     article = models.ForeignKey(
#         verbose_name='Статья',
#         to='weapp.Article',
#         null= False,
#         blank=False,
#         related_name='comments',
#         on_delete=models.RESTRICT
#     )
#     text = models.TextField()