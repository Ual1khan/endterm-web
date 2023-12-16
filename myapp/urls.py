from django.urls import path
from .views import PostListCreateView, PostDetailView, UserCreateView, TokenPairObtainView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('token/', TokenPairObtainView.as_view(), name='token_obtain_pair'),
]
