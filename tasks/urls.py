from django.urls import path

from tasks import views

urlpatterns = [
     path("list", views.getList, name="AllTasks")
]
