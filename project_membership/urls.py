from django.urls import path

from project_membership import views

urlpatterns = [
    path('', views.index, name="memberships-index"),
    path('remove-membership/<int:project_id>/<int:student_id>', views.delete_membership, name="delete-membership")
]
