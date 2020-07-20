from django.shortcuts import render
from django.views.generic import (TemplateView, ListView
    )
from .models import Comment, Post

# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog_app/about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte = timezone.now().order_by("-publish_date"))
