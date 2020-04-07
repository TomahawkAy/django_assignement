from django.db import models
from project.models import Project
from student.models import Student


# Create your models here.
class MembershipInProject(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    allocated_time_per_member = models.IntegerField(
        'Allocated time per member'
    )

    def __str__(self):
        return 'Member ' + self.student.first_name

    class Meta:
        unique_together = ("student", "project")
