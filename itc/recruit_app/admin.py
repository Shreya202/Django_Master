from django.contrib import admin

from .models import User, Panelist, Recruiter, Candidate, PanelistSchedule, InterviewSchedule

admin.site.register(User)
admin.site.register(Panelist)
admin.site.register(Recruiter)
admin.site.register(Candidate)
admin.site.register(PanelistSchedule)
admin.site.register(InterviewSchedule)



# Register your models here.
