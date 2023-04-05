from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserSignup, UserLogin, PostList, PostDetail, like_post

urlpatterns = [
    path('signup/', UserSignup.as_view()),
    path('login/', UserLogin.as_view()),
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
     path('post/like/<int:post_id>', like_post, name='post_like'),
]

urlpatterns = format_suffix_patterns(urlpatterns)