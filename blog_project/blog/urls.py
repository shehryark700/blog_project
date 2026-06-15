from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('accounts/signup/', views.signup, name='signup'),
]
