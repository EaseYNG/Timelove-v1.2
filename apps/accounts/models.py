from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    nickname = models.CharField(max_length=20, blank=True)
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))

    partner = models.OneToOneField(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='partner_of',
    )

    # 解决 groups 和 user_permissions 反向关系冲突
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # 避免和 auth.User 冲突
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # 避免和 auth.User 冲突
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return f"{self.username} ({self.get_sex_display()})"
