from django.db import models

from webapp.models.base_create_update import BaseCreateUpdateModel

class SubPost(BaseCreateUpdateModel):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Название')
    body = models.TextField(null=False, blank=False, verbose_name='Тело подпоста')
    post = models.ForeignKey('webapp.Post', verbose_name='Пост', on_delete=models.CASCADE, null=False, blank=False, related_name='subposts')

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = 'subposts'
        verbose_name = 'Подпост'
        verbose_name_plural = 'Подпосты'
