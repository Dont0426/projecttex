from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignupForm, MyTestForm, CreateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'femitex/home.html',{'posts': posts})

def side_bar(request):
    posts = Post.objects.all()
    last_post = Post.objects.last()
    context = {'posts':posts, 'last_post': last_post}
    return render(request, 'femitex/side.html', context)

# def login(request):
#     posts = Post.objects.first()
#     return render(request,'femitex/login.html',{'post' : posts})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f"Hello {username}, Your account has been created successfully")
            return redirect('homepage')
    else:
        form = SignupForm()
    return render(request, 'femitex/signup.html',{'form': form})

def post_detail(request, pk):
    the_post = Post.objects.filter(id=pk).first()
    return render(request, 'femitex/post-detail.html',{'post': the_post})
@login_required
def createpost(request):
    user = request.user
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form_title = form.cleaned_data.get('title')
            form_body = form.cleaned_data.get('body')
            Post.objects.create(title = form_title, body = form_body, owner = user)
            messages.success(request, "Post created successfully")
            return redirect('homepage')
    else:
        form = CreateForm()
    return render(request, 'femitex/createpost.html', {'form': form})
class PostListView(ListView):
        model = Post
        context_object_name = 'posts'

class PostDetailView(DetailView):
        model = Post

class ClassCreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ClassUpdatePost(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.owner == self.request.user:
            return True
        else:
            return False

class ClassDeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if post.owner == self.request.user:
            return True
        else:
            return False

def postdelete(request, pk):
    user = request.user
    if Post.objects.filter(id = pk).exists():
        print("object exists")
        post = Post.objects.filter(id = pk).first()
        if user == post.owner:
            print("user ownership verified")
            Post.objects.get(id = pk).delete()
            messages.success(request, 'Post Deleted')
            return redirect('homepage')
        else:
            print("Ownership not verified")
            messages.success(request, "You cant delete this post")
            return redirect('homepage')
    
    else:
        print("object does not exist")
        messages.success(request, "Post deos not exist")
        return redirect ('homepage')




