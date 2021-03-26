from django import forms
from django.forms import ModelForm
from .models import Candidate, Panelist, Recruiter, User, PanelistSchedule
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction





class PanelistSignUpForm(UserCreationForm):
    username = forms.CharField(required= True)
    Psid = forms.IntegerField(required=True)
    Skill = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.is_panelist = True
        user.save()
        panelist = Panelist.objects.create(user= user)
        panelist.Psid = self.cleaned_data.get('Psid')
        panelist.Skill = self.cleaned_data.get('Skill')
        panelist.save()
        return user    

class RecruiterSignUpForm(UserCreationForm):
    username = forms.CharField(required= True)
    Psid = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        exclude = ['is_panelist','is_recruiter','first_name','last_name','Password','last_login','groups','user_permissions','date_joined','is_staff','is_active','date_joined','is_superuser','password']

    @transaction.atomic
    def save(self):
        user = super().save(commit = False)
        user.username = self.cleaned_data.get('username')
        user.is_recruiter = True
        user.save()
        recruiter = Recruiter.objects.create(user = user)
        recruiter.Psid = self.cleaned_data.get('Psid')
        recruiter.save()
        return recruiter

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"
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
    widgets = {
            'Skill_Category': forms.Select(choices=SKILL_CHOICES,attrs={'class': 'form-control'}),
            'Grade': forms.Select(choices=GRADE_CHOICES,attrs={'class': 'form-control'}),
            'Screening_Phase': forms.Select(choices=SCREENING_CHOICES,attrs={'class': 'form-control'}),
            'Final_status': forms.Select(choices=SELECTION_CHOICES,attrs={'class': 'form-control'}),
        }


class DateInput(forms.DateTimeInput):
    input_type = 'datetime'


class PanelistForm(ModelForm):
    class Meta:
        model = PanelistSchedule
        fields = ['Available_from']
        widgets = {
            'Available_from': DateInput(),
        }
        


