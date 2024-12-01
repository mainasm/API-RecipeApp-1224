from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('recipes/', views.RecipeListCreateView.as_view(), name = 'recipe-list'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('tags/', views.TagListCreateView.as_view(), name='tag-list'),
    path('reviews/', views.ReviewListCreateView.as_view(), name='review-list'),
    path('favorites/', views.FavoriteListCreateView.as_view(), name='favorite-list'),
    path('comments/', views.CommentListCreateView.as_view(), name='comment-list'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]