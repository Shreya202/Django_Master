from django.shortcuts import render, redirect, HttpResponse
from .forms import PanelistSignUpForm, RecruiterSignUpForm, CandidateForm, PanelistForm
from django.contrib.auth import login
from django.views.generic import CreateView
from .models import  User, Panelist, Recruiter, Candidate
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
        login(self.request, user)
        return redirect('home')        

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
        login(self.request, user)
        return redirect('home')     

def recruiter(request):
     # if this is a POST request we need to process the form data
    print('started')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CandidateForm(request.POST)
        print("Correcr redirect")
        # check whether it's valid:
        if form.is_valid():
            print("start")


            form.save()
            print("Candidate saved")
            

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CandidateForm()
        print(form)
    print('ended')    
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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PanelistForm(request.POST)
        print(form.errors)
        if form.is_valid():
            panelistschedule = form.save(commit=False)
            panelistschedule.UserName = request.user
            panelistschedule.save()
            
            
            
            

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PanelistForm()
    return render(request,'recruit_app/panelist.html',{'form': form})

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
                    return redirect('panelist')
                else:
                    login(request,user)
                    return redirect('recruiter')
            else:
                messages.info(request,'Username or Password is incorrect')    
            

    return render(request,'recruit_app/login.html')   

def logoutUser(request):
    logout(request)
    return redirect('login') 




def interviewschedule(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InterviewScheduleForm(request.POST)
        print(form.errors)
        if form.is_valid():
            
            form.save()
            
            

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InterviewScheduleForm()
    return render(request,'recruit_app/interviewschedule.html',{'form': form})  

def hr(request):
    return render(request,'recruit_app/hr.html')      

def pickle(request):
    return render(request,'recruit_app/main.html')     

def interviewschedule(request):
    return render(request, 'recruit_app/interview.html')                         

