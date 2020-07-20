from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)
from .models import Comment, Post
from .forms import CommentForm, PostForm

# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog_app/about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte = timezone.now()).order_by("-publish_date")

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'

    model = Post
    form_class = PostForm

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    model = Post
    form_class = PostForm

class PostDeleteView(LoginRequiredMixin,DeleteView):
    login_url = "/login/"
    redirect_field_name = 'blog_app/post_list.html'
    model = Post
    success_url = reverse_lazy('post_list')

class PostDraftListView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    model = Post
    redirect_field_name = 'blog_app/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull = True).order_by('created_date')
