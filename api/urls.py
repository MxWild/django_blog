from django.urls import path

from api.views import PostList, PostDetail

app_name = 'api'

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view())
]
