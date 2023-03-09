from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blog_about = models.CharField(max_length=1024, blank=True)
    avatar = models.ImageField(default='default.png', upload_to='profile/')

    class Meta:
        db_table = 'profile'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return self.user.username
