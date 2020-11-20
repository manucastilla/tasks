from django.urls import path

from tasks import views

urlpatterns = [
    path("list", views.getList, name="AllTasks"),
    path('list/<int:pk>', views.updateTask, name="ChangeTask"),
    path('create', views.createTask, name="createTask"),
    path('deleteAll', views.delete_all, name="deleteTask"),
]
