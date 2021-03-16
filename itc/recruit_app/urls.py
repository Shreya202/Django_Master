from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SignUp,name = 'signup'),
    path('signup/panelist',views.PanelistSignUpView.as_view(),name = 'panelist_signup'),
    path('signup/recruiter',views.RecruiterSignUpView.as_view(),name = 'recruiter_signup'),
    path('',views.pickle,name = "home"),
    path('recruiter/',views.recruiter,name = 'recruiter'),
    path('logout/',views.logoutUser,name = 'logout'),
    path('recruiter/interview',views.interviewschedule,name = 'interview'),
    path('recruiter/view/',views.view,name = 'view'),
    path('recruiter/search/',views.search,name = 'search'),
    path('recruiter/search/edit/<int:id>',views.edit ,name = 'edit'),
    path('recruiter/search/edit/update/<int:id>',views.updatecandidate,name = 'update'),
    path('panelist/',views.panelist,name = 'panelist'),
    path('login/',views.loginPage,name = 'login'),
    path('hr/',views.hr,name = 'hr'),

]

