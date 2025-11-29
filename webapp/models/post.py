from django.contrib.auth import get_user_model

from django.db import models

from webapp.models.base_create_update import BaseCreateUpdateModel


class Post(BaseCreateUpdateModel):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    body = models.TextField(null=False, blank=False, verbose_name='Тело поста')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор', related_name='posts', default=1)


    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = 'posts'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'