from .models import Candidate
import django_filters


class CandidateFilter(django_filters.FilterSet):
    class Meta:
        model = Candidate
        fields = ['Skill_Category', 'Account', 'Grade', 'Role', 'Billing_Date', 'OnBoard_Date','Screening_Phase','Final_status']
        