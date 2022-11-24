from django.shortcuts import render, redirect
from .models import Blog, EditorForm
from .form import EditorFM
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import Group


# Create your views here.
def HomeView(request):
    blog = Blog.objects.filter(status=True).order_by('-id')
    return render(request,'index.html',{'blogs':blog})

def AboutView(request):
    return render(request,'about.html')

def ContactView(request):
    return render(request,'contact.html')

@login_required(login_url="login")
def PostView(request, pk):
    if request.user.is_staff:
        return redirect("login")
    post = Blog.objects.get(slug=pk)
    return render(request,'post.html',{'post':post})

@login_required(login_url="login")
def ApplyFormView(request):
    user=request.user
    if user.is_staff:
        return redirect("login")
    
    fm = EditorFM()
    if request.method == "POST":
        fm = EditorFM(request.POST,request.FILES)
        if fm.is_valid():
            subject = fm.cleaned_data['subject']
            message = fm.cleaned_data['message']
            portfolio_url = fm.cleaned_data['portfolio_url']
            resume = fm.cleaned_data['resume']
    
            editor = EditorForm(user=user,subject=subject,message=message,portfolio_url=portfolio_url,resume=resume)
            editor.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    return render(request,'applyform.html',{'form':fm})