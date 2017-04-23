from django.shortcuts import render,get_object_or_404, redirect

# Create your views here.

from .models import Candidate,Post,Feedback,Zone,District,Politicaldiv
from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm, WpZoneForm, WpDistrictForm, WpPoliticaldivForm, WpPostForm

from django.utils.text import slugify


def profile(request, slug, district, politicaldiv):
    template_name = 'profile.html'
    infor = get_object_or_404(Candidate, slug=slug, district__name=district, politicaldiv__name=politicaldiv)
    context = {'title': infor.name}
    return render(request,template_name,context)

def explore(request):
    template_name = 'explore.html'
    infor = District.objects.all()
    context = {'title': 'Find Candidates', 'subtitle':'Discover everything election!','infor':infor}
    return render(request,template_name,context)

def district(request, name):
    template_name = 'district.html'
    dis = get_object_or_404(District, name=name)
    infor = Politicaldiv.objects.all()
    context = {'title': dis.name, 'subtitle':'Discover everything election!','infor':infor,'dis':dis}
    return render(request,template_name,context)

def politicaldiv(request, name, name2):
    template_name = 'politicaldiv.html'
    dis = get_object_or_404(District, name=name)
    location = get_object_or_404(Politicaldiv, name=name2)
    infor = Candidate.objects.all()
    context = {'title': location.name, 'subtitle':'Discover everything election!','infor':infor,'dis':dis,'location':location}
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
            return redirect('wppoliticaldiv')
    else:
        form = WpPoliticaldivForm()
    template_name = 'wp-admin/form.html'
    items = Politicaldiv.objects.all()
    context = {'title':'Add Political Division','form':form,'items':items,'message':'You Should Add Required Zone and Districts Before'}
    return render (request, template_name, context)

def wppost(request):
    if request.method == 'POST':
        form = WpPostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.auther = request.user
            form.slug = slugify(form.title)
            form.save()
            return redirect(wppost)
    else:
        form = WpPostForm()
    template_name = 'wp-admin/form.html'
    items = Post.objects.all()
    context = {'title':'Add Post/Article','form':form,'items':items,'message':'Select home 1 or 2 or 3 to make these post shown in hoempage'}
    return render (request, template_name, context)
