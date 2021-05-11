from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Post
from allauth.socialaccount.models import SocialAccount
from .forms import PostForm
from django.views.generic import DetailView, UpdateView, DeleteView

def index(request):
    return render (request, 'testapp/index.html')


def start(request):
    error = ''
    if request.method == "POST":
        req = PostForm(request.POST)
        if req.is_valid():
            req.save()
        else:
            error = 'Ошибка заполнения формы'

    post = Post.objects.all()
    social = SocialAccount.objects.all()
    form = PostForm()
    return render (request, 'testapp/main.html',{'social':social,'form':form,'error':error, "post":post})

def lk(request):
    post = Post.objects.all()
    social = SocialAccount.objects.all()
    form = PostForm()
    return render (request, 'testapp/mypost.html',{'social':social,'form':form, "post":post})

class PostDetailView(DetailView):
    model = Post
    template_name = 'testapp/post_detail.html'
    context_object_name = 'post'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'testapp/update.html'
    form_class = PostForm

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/lk'
    template_name = 'testapp/delete.html'