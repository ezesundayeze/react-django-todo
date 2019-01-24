from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task import views
route = DefaultRouter()

route.register("task", views.TaskView, base_name="task" )
urlpatterns =[
path("", include(route.urls)),
]



