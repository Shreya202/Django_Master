from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



class User(AbstractUser):
    is_panelist = models.BooleanField(default=False)
    is_recruiter = models.BooleanField(default = False)
    
class Panelist(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    Psid = models.IntegerField(null = True)
    Skill = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.user.username

class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    Psid = models.IntegerField(null = True)

    def __str__(self):
        return self.user.username



class Candidate(models.Model):
    SKILL_CHOICES = (
        ('JAVA','JAVA'),
        ('PYTHON','PYTHON'),
        ('FULL STACK','FULL STACK'),
        ('BACKEND','BACKEND'),
    )
    GRADE_CHOICES = (
        ('IS1','IS1'),
        ('IS2','IS2'),
        ('IS3','IS3'),
    )    
    SCREENING_CHOICES = (
        ('PENDING','PENDING'),
        ('WIP','WIP'),
        ('COMPLETE','COMPLETE'),
    )

    SELECTION_CHOICES = (
        ('SELECTED','SELECTED'),
        ('REJECTED','REJECTED')
    )
    
    Candidate_Name = models.CharField(max_length=70)
    Skill_Category = models.CharField(max_length=20,choices = SKILL_CHOICES)
    Account = models.CharField(max_length = 50)
    Grade = models.CharField(max_length=10,choices = GRADE_CHOICES)
    Role = models.CharField(max_length=20)
    Billing_Date = models.DateField()
    OnBoard_Date = models.DateField(default='2021-01-01')
    Screening_Phase = models.CharField(max_length=20,choices = SCREENING_CHOICES)
    Final_status = models.CharField(max_length = 10, choices = SELECTION_CHOICES,default = 'SELECTED')

    def __str__(self):
        return self.Candidate_Name    

class PanelistSchedule(models.Model):
    UserName = models.CharField(max_length=70)
    Available_from = models.DateTimeField()
    Available_till = models.DateTimeField()

    def __str__(self):
        return self.UserName + ' Schedule'



