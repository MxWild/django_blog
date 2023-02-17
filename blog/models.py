from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Status(models.Model):
    title = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'status'
        verbose_name = 'status'
        verbose_name_plural = 'statuses'
        ordering = ['title']

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=15, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags')

    class Meta:
        db_table = 'tag'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'
        ordering = ['-date_created']

    def save(self, *args, **kwargs):
        if not self.author_id:
            self.author_id = 1
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w3-input w3-border w3-padding-16',
                                            'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'w3-input w3-border w3-padding-16',
                                             'placeholder': 'Content'}),
            'status': forms.Select(attrs={'class': 'w3-select w3-border w3-padding-16'}),
        }
