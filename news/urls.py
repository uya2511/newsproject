from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.CreateNewsView.as_view(), name='post'),
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),
    path('news/<int:category>', views.CategoryView.as_view(), name = 'news_cat'),
    path('user-list/<int:user>', views.UserView.as_view(),  name = 'user_list'),
    ]
