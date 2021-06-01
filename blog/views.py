from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class all_posts(LoginRequiredMixin,ListView):
    template_name='home.html'
    context_object_name= 'blogs'
    model= post
    ordering='-date_posted'

class posts_user(LoginRequiredMixin,ListView):
    template_name='user_post.html'
    context_object_name= 'blogs'
    model= post
    ordering='-date_posted'

    def get_queryset(self):
        
        user= get_object_or_404(User,username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-date_posted')

class post_detail(DetailView):
    template_name='detail.html'
    context_object_name= 'post'
    model= post

class post_create(LoginRequiredMixin,CreateView):
    template_name='create_post.html'
    context_object_name= 'post'
    model= post
    fields=['title','content']
    success_url='/'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class post_delete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    template_name='delete.html'
    model= post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False

class post_update(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name='update.html'
    model= post
    fields=['title','content']
    success_url='/'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False


       
def about(request):
    return render(request, 'about.html')

