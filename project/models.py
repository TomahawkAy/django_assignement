from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from student.models import Student
from coach.models import Coach


# Create your models here.

class Project(models.Model):
    project_name = models.CharField('project title', max_length=30, default='Project name is unset')
    project_duration = models.IntegerField('estimated duration', default=0)
    time_allocated_by_creator = models.IntegerField('Allocated time',
                                                    validators=[MinValueValidator(1), MaxValueValidator(10)])
    needs = models.TextField(max_length=250)
    description = models.TextField(max_length=250)
    validity_state = models.BooleanField(default=False)
    creator = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='project_owner'
    )
    supervisor = models.ForeignKey(
        Coach,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='project_coach'
    )
    members = models.ManyToManyField(
        Student,
        through='project_membership.MembershipInProject',
        related_name='members',
        blank=True
    )

    def split_needs_into_array(self):
        return self.needs.split(',')
