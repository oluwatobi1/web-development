from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)
from .models import Comment, Post
from .forms import CommentForm, PostForm

# Create your views here.

###########################################


class AboutView(TemplateView):
    template_name = 'blog_app/about.html'

class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = 'post_list.html'

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
    context_object_name = "post_drafts"
    model = Post
    redirect_field_name = 'blog_app/post_list.html'
    template_name = 'blog_app/post_draft_list.html'

    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull = True).order_by('create_date')

###########################################################
###########################################################
###########################################################


def add_comments_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk = pk)
    else:
        form = CommentForm()
    return render(request, 'blog_app/comment_form.html', {'form':form})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk = pk)


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk = post_pk)
