from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="index"),
    path('article-create/', views.article_create_view, name="article-create"),
    path('article/<int:pk>/', views.article_detail_view, name="article-detail"),
    path('article/<int:pk>/update', views.article_update_view, name="article-update"),
    path('article-approval/', views.article_approve_view, name="article-approval"),
    path('articles-edited/', views.article_edited_view, name="articles-edited"),
]
