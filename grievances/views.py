from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import GrievancePost
from .forms import GrievanceForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def index(request):
    grievanceposts = GrievancePost.objects.filter(posted_date__lte=timezone.now()).order_by('posted_date')
    if grievanceposts == None:
        return render(request, 'grievances/grievances_feed.html', {})
    return render(request, 'grievances/grievances_feed.html', {'grievanceposts': grievanceposts})

def grievance_detail(request, pk):
    grievancepost = get_object_or_404(GrievancePost, pk=pk)
    return render(request, 'grievances/grievance_detail.html', {'post': grievancepost})

def grievance_new(request):
    if request.method == "POST":
        form = GrievanceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if post.department == 'E':
                post.assigned_to = 'Karan'
            if post.department == 'L':
                post.assigned_to = 'Manan'
            if post.department == 'H':
                post.department = 'Jayesh'
            if post.department == 'A':
                post.department = 'Vijayan'
            post.complainant = request.user
            post.last_updated__date = timezone.now()
            post.status = 0
            post.save()
            return redirect('grievance_detail', pk=post.pk)
    else:
        form = GrievanceForm()

    return render(request, 'grievances/new_grievance.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            index(request)
            return
    else:
        form = UserCreationForm()
    return render(request, 'grievances/signup.html',  {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            index(request)
            return
        else:
            login(request)

def about_us(request):
    return render(request, 'grievances/about_us.html', {})

def council_team(request):
    return render(request, 'grievances/council_team.html', {})