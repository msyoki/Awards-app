from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Profile,Project
from .forms import NewProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer

# Create your views here.
def home(request):
    projects=Project.objects.all()
    return render(request,'awwards/home.html',{'projects':projects})

@login_required(login_url='/accounts/login/') 
def rate_project(request,project_id):
    project=Project.objects.get(id=project_id)
    return render(request,"awwards/project.html",{"project":project})

@login_required(login_url='/accounts/login/') 
def view_profile(request,user_id):
    Current_user=request.user
    user=User.objects.get(id=user_id)
    return render(request,"awwards/profile.html",{"user":user})

@login_required(login_url='/accounts/login/') 
def search_project(request):
    if "project" in request.GET and request.GET["project"]:
        search_term=request.GET.get("project")
        searched_projects=Project.search_by_name(search_term)
        message = f"{search_term}"

        return render(request,'awwards/search.html',{"message":message, "projects":searched_projects, "project":search_term})
    
    else:
        message = "Please enter search name"

        return render(request, 'awwards/search.html',{"message":message})

@login_required(login_url='/accounts/login/')     
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')
        
    else:
        form = NewProjectForm()
    return render(request, 'awwards/new_project.html', {"form":form, "current_user":current_user})

def api_page(request):
    return render(request,'awwards/api_page.html')


class ProfileList(APIView):
    def get(self, request, fromat=None):
        all_profiles =Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)


class ProjectList(APIView):
    def get(self, request, fromat=None):
        all_projects =Project.objects.all()
        serializers =ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)