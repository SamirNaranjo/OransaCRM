from django.urls import path
from User.views import *

app_name = 'User'

urlpatterns = [
    # user
    path('list/', UserListView.as_view(), name='list_user'),
    path('add/', UserCreateView.as_view(), name='user_create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),

]