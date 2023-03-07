from django.urls import path

from api.views import post_list, PostDetail, PostList

app_name = 'api'

urlpatterns = [
    # path('posts/', post_list.as_view()),
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view())
]
