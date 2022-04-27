from django.urls import path
from .views import PostCreateListAPI, AddCommetToPostAPI, CommentToCommentAPI, CommetsAPIListView

# api/v1/
urlpatterns = [
    path('posts/', PostCreateListAPI.as_view()),
    path('posts/<int:pk>/comments/', AddCommetToPostAPI.as_view()),
    path('comments/', CommetsAPIListView.as_view()),
    path('comments/<int:pk>/', CommentToCommentAPI.as_view()),
]
