from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    TaskList,CreateTask,
    UpdateTask,CustomLoginView,
    RegisterPage,TaskDelete
    )

urlpatterns=[
  path('',TaskList.as_view(),name='home'),
  path('login/',CustomLoginView.as_view(),name='login'),
  path('logout/',LogoutView.as_view(next_page='login'),name='logout'), 
  path('register/',RegisterPage.as_view(),name='register'),   
  path('create-task/',CreateTask.as_view(),name='task-create'),
  path('update-task/<int:pk>/',UpdateTask.as_view(),name='task-update'),
  path('delete-task/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
]