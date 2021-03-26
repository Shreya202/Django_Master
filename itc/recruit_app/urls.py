from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SignUp,name = 'signup'),
    path('signup/panelist',views.PanelistSignUpView.as_view(),name = 'panelist_signup'),
    path('signup/recruiter',views.RecruiterSignUpView.as_view(),name = 'recruiter_signup'),
    path('',views.pickle,name = "home"),
    path('recruiter-home/',views.recruiter_home,name = 'recruiter_home'),
    path('recruiter/',views.recruiter,name = 'recruiter'),
    path('logout/',views.logoutUser,name = 'logout'),
    path('recruiter/interview',views.interviewschedule,name = 'interview'),
    path('recruiter/interview/all',views.all_interview,name = 'all_interview'),
    path('recruiter/interview/all/<int:id>',views.cancel_interview,name = 'cancel_interview'),
    path('recruiter/interview/save',views.interviewsave,name = 'save-interview'),
    path('recruiter/interview/check-schedule/',views.viewschedule,name = 'schedule'),
    path('recruiter/interview/load-panelists/',views.load_panelist,name = 'ajax_load_panelists'),
    path('recruiter/interview/load-candidates/',views.load_candidate,name = 'ajax_load_candidates'),
    path('recruiter/interview/load-schedules/',views.load_schedule,name = 'ajax_load_schedules'),
    path('recruiter/view/',views.view,name = 'view'),
    path('recruiter/search/',views.search,name = 'search'),
    path('recruiter/search/edit/<int:id>',views.edit ,name = 'edit'),
    path('recruiter/search/edit/update/<int:id>',views.updatecandidate,name = 'update'),
    path('panelist-home/',views.panelist_home,name = 'panelist_home'),
    path('panelist/',views.panelist,name = 'panelist'),
    path('panelist/queue',views.queue,name = 'queue'),
    path('login/',views.loginPage,name = 'login'),
    path('hr/',views.hr,name = 'hr'),

]

