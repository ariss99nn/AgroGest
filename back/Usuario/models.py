from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    logEntry = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)
    role = models.CharField(
        max_length=20,
        choices=[('ADMIN', 'Administrator'), ('AGRICULTOR', 'Farmer')]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="usuario_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="usuario_set",
        related_query_name="user",
    )

    def save(self, *args, **kwargs):
        if not self.logEntry:
            self.logEntry = "Usuario creado automáticamente"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
