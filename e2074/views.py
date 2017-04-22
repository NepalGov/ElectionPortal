from django.shortcuts import render,get_object_or_404, redirect

# Create your views here.

from .models import Candidate,Post,Feedback,Zone,District,Politicaldiv
from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm, WpZoneForm, WpDistrictForm, WpPoliticaldivForm

def profile(request, slug):
    template_name = 'profile.html'
    infor = get_object_or_404(Candidate, slug=slug)
    context = {'title': infor.name}
    return render(request,template_name,context)

def post(request, slug):
    template_name = 'post.html'
    post = get_object_or_404(Post, slug=slug)
    context = {'title': post.title, 'subtitle':'Discover everything election!','post':post}
    return render(request,template_name,context)

def home(request):
    if request.method =='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    template_name = 'index.html'
    blogs = Post.objects.all()
    context = {'title':'Election Portal', 'subtitle':'Discover everything election!', 'blogs':blogs,'form':form}
    return render(request,template_name,context)

def signup(request):
    template_name = 'wp-admin/signup.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        pass
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render (request, template_name, context)

@login_required()
def wpadmin(request):
    template_name = 'wp-admin/index.html'
    context = {'title':'Admin Home'}
    return render (request, template_name, context)

def wpzone(request):
    if request.method =='POST':
        form = WpZoneForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('wpzone')
    else:
        form = WpZoneForm()
    template_name = 'wp-admin/form.html'
    items = Zone.objects.all()
    context = {'title':'Add Zones','form':form,'items':items}
    return render (request, template_name, context)

def wpdistrict(request):
    if request.method =='POST':
        form = WpDistrictForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('wpdistrict')
    else:
        form = WpDistrictForm()
    template_name = 'wp-admin/form.html'
    items = District.objects.all()
    context = {'title':'Add Districts','form':form,'items':items,'message':'You Should Add Required Zone Before'}
    return render (request, template_name, context)

def wppoliticaldiv(request):
    if request.method =='POST':
        form = WpPoliticaldivForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('wpvdc')
    else:
        form = WpPoliticaldivForm()
    template_name = 'wp-admin/form.html'
    items = Politicaldiv.objects.all()
    context = {'title':'Add Political Division','form':form,'items':items,'message':'You Should Add Required Zone and Districts Before'}
    return render (request, template_name, context)
