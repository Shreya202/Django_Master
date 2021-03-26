from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import PanelistSignUpForm, RecruiterSignUpForm, CandidateForm, PanelistForm
from django.contrib.auth import login
from django.views.generic import CreateView
from .models import  User, Panelist, Recruiter, Candidate, PanelistSchedule, InterviewSchedule
from .filters import CandidateFilter
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def SignUp(request):
    return render (request,'recruit_app/signup.html')

class PanelistSignUpView(CreateView):
    model = User
    form_class = PanelistSignUpForm
    template_name = 'recruit_app/signsup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'panelist'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('login')        

def home(request):
    return render(request,'recruit_app/dashboard.html')

class RecruiterSignUpView(CreateView):
    model = User
    form_class = RecruiterSignUpForm
    template_name = 'recruit_app/signsup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'recruiter'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('login')    

def recruiter_home(request):
    obj = User.objects.get(username=request.user)
    if obj.is_recruiter == True:
        return render(request,'recruit_app/recruiter_home.html')  
    else:
        return HttpResponse("You are not authorized to access this page") 

def panelist_home(request):
    obj = User.objects.get(username=request.user)
    if obj.is_panelist == True:
        return render(request,'recruit_app/panelist_home.html')  
    else:
        return HttpResponse("You are not authorized to access this page")         

def recruiter(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CandidateForm()    
    return render(request,'recruit_app/recruiter.html',{'form': form})
         

def updatecandidate(request,id):
    updateemp = Candidate.objects.get(id = id)
    form = CandidateForm(request.POST,instance=updateemp)
    if form.is_valid():
        form.save()
        messages.success(request,"Record Updated Successfully..!")
        return redirect('search')
    else:
        messages.error(request,"No Update done")
            
    return render(request,'recruit_app/edit.html',{'editupdaterecord':updateemp})

def edit(request,id):
    display = Candidate.objects.get(id=id)
    print(display)
    return render(request,'recruit_app/edit.html',{'editupdaterecord':display})

def view(request):
    titles = Candidate.objects.all()
    context = {'title':titles}
    return render(request,'recruit_app/view.html',context)

def panelist(request):
    obj = User.objects.get(username=request.user)
    if obj.is_panelist == True:
    # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = PanelistForm(request.POST)
            print(form.errors)
            if form.is_valid():
                panelistschedule = form.save(commit=False)
                panelistschedule.UserName = request.user
                panelistschedule.save()
                messages.success(request,"Schedule added successfully")
                
                
                
                

                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                #return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = PanelistForm()
        return render(request,'recruit_app/panelist.html',{'form': form})
    else:
        return HttpResponse("You are not authorized to access this page")    

def search(request):
    candidate_list = Candidate.objects.all()
    candidate_filter = CandidateFilter(request.GET, queryset=candidate_list)
    return render(request, 'recruit_app/candidate_list.html', {'filter': candidate_filter}) 

def loginPage(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
        

            if user is not None:
                if user.is_panelist == True:
                    login(request,user)
                    return redirect('panelist_home')
                else:
                    login(request,user)
                    return redirect('recruiter_home')
            else:
                messages.info(request,'Username or Password is incorrect')    
            

    return render(request,'recruit_app/login.html')   

def logoutUser(request):
    logout(request)
    return redirect('login') 




# def interviewschedule(request):
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = InterviewScheduleForm(request.POST)
#         print(form.errors)
#         if form.is_valid():
            
#             form.save()
            
            

#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             #return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = InterviewScheduleForm()
#     return render(request,'recruit_app/interviewschedule.html',{'form': form})  

def hr(request):
    return render(request,'recruit_app/hr.html')      

def pickle(request):
    return render(request,'recruit_app/main.html')     

def interviewschedule(request):
    skill = Candidate.objects.all()
    d= {'skill':skill}
    return render(request, 'recruit_app/interview.html',d)

def load_panelist(request):
    skill_id = request.GET.get('programming')
    row = Candidate.objects.get(id = skill_id)
    real_skill = row.Skill_Category
    panels = Panelist.objects.filter(Skill=real_skill)
    return render(request,'recruit_app/panelist_dropdown_list_options.html',{'panels': panels})      

def load_candidate(request):
    skill_id = request.GET.get('programmings')
    row = Candidate.objects.get(id = skill_id)
    real_skill = row.Skill_Category     
    candids = Candidate.objects.filter(Skill_Category=real_skill)
    return render(request,'recruit_app/candidate_dropdown_list_options.html',{'candids': candids})

def viewschedule(request):
    sch = PanelistSchedule.objects.all()
    return render(request,'recruit_app/viewschedule.html',{'sch':sch})

def load_schedule(request):
    uid = request.GET.get('programmingss')
    use = User.objects.get(id = uid)
    name = use.username
    print(name)
    sche = PanelistSchedule.objects.filter(UserName = name, Slot_type='AVAILABLE')
    return render(request,'recruit_app/schedule_dropdown_list_options.html',{'sche':sche})

def interviewsave(request):
    print(request.user)
    skill = request.POST['skill']
    panelid = request.POST['panelists']
    panid = get_object_or_404(Panelist,user_id = panelid)
    #use = User.objects.get(id = panelid)
    #name = use.username
    candid = request.POST['candidates']
    candi = get_object_or_404(Candidate,id = candid)
    interview_id = request.POST['schedules']
    interview_obj = PanelistSchedule.objects.get(id = interview_id)
    interview_obj.Slot_type = 'BLOCKED'
    interview_obj.save()
    interview_time = interview_obj.Available_from
    InterviewSchedule.objects.create(Skill=skill,panelist=panid,candidate=candi,interview_time=interview_time)
    messages.success(request,"Interview Scheduled Successfully")
    return redirect("interview")

def queue(request):
    user = request.POST.get('mybtn2')
    print(request.POST.get('mybtn2'))
    obj = User.objects.get(username=user)
    obj_id = obj.id
    inter = InterviewSchedule.objects.filter(panelist_id = obj_id).order_by('interview_time')
    return render(request,'recruit_app/queue.html',{'inter': inter})

def all_interview(request):
    obj = InterviewSchedule.objects.all()
    return render(request,'recruit_app/all_interview.html',{'obj':obj})

def cancel_interview(request,id):
    instance = InterviewSchedule.objects.get(id=id)
    panel = instance.panelist
    time = instance.interview_time
    obj = PanelistSchedule.objects.filter(UserName=panel,Available_from=time).first()
    print(obj)
    obj.Slot_type = 'AVAILABLE'
    obj.save()
    instance.delete()
    messages.success(request,"Interview Cancelled Successfully")
    return redirect("all_interview")





