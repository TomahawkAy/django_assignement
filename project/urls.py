from django.urls import path
from project import views

urlpatterns = [
    path('', views.read_projects, name="create"),
    path('delete-project/<int:id>/', views.delete_project, name="delete_project")
]
