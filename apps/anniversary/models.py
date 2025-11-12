from django.db import models

from apps.accounts.models import User
from config import settings


# Create your models here.
class Anniversary(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='anniversaries', # 可通过user.anniversaries()访问
    )
    def __str__(self):
        return f"[{self.id}][{self.date}][{self.title}]({self.owner})"

    class Meta:
        ordering = ['id']