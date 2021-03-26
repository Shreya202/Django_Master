from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta



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
        ('IS4','IS4'),
        ('IS5','IS5'),
        ('IS6','IS6'),
    )    
    SCREENING_CHOICES = (
        ('PENDING','PENDING'),
        ('WIP','WIP'),
        ('COMPLETE','COMPLETE'),
    )

    SELECTION_CHOICES = (
        ('SELECTED','SELECTED'),
        ('REJECTED','REJECTED'),
        ('OFFER RELEASED','OFFER RELEASED'),
        ('ON-BOARDED','ON-BOARDED'),
    )
    ACCOUNT_CHOICES = (
        ('QVC','QVC'),
        ('FINASTRA','FINASTRA'),
        ('BLACKROCK','BLACKROCK'),
        ('GOLDMANSACHS','GOLDMANSACHS'),
    )
    
    Candidate_Name = models.CharField(max_length=70)
    Skill_Category = models.CharField(max_length=20,choices = SKILL_CHOICES)
    Account = models.CharField(max_length = 50,choices= ACCOUNT_CHOICES)
    Grade = models.CharField(max_length=10,choices = GRADE_CHOICES)
    Role = models.CharField(max_length=20)
    Billing_Date = models.DateField()
    OnBoard_Date = models.DateField(default='2021-01-01')
    Screening_Phase = models.CharField(max_length=20,choices = SCREENING_CHOICES)
    Final_status = models.CharField(max_length = 30, choices = SELECTION_CHOICES,default = 'SELECTED')

    def __str__(self):
        return self.Candidate_Name    

class PanelistSchedule(models.Model):
    UserName = models.CharField(max_length=70)
    Available_from = models.DateTimeField()
    Available_till = models.DateTimeField(editable=False)
    Slot_type = models.CharField(max_length=30, default='AVAILABLE')

    def __str__(self):
        return str(self.Available_from) + ' Schedule'

    def save(self):
        d = timedelta(hours=1)
        self.Available_till = self.Available_from + d
        super(PanelistSchedule, self).save()


class InterviewSchedule(models.Model):
    Skill = models.CharField(max_length=20)  
    panelist = models.ForeignKey(Panelist,on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)    
    interview_time = models.DateTimeField()


    def __str__(self):
        return str(self.interview_time)



