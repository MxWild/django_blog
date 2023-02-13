from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('add/', views.add_post, name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('<slug:slug>/edit/', views.edit_post, name='edit_post'),
]
