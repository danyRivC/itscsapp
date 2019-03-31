from django.views.generic import ListView, DetailView
from .models.post import PostBlog

class AllPostsBlog(ListView):
    model = PostBlog
    template_name = 'blog/blog.html'

class PostBlogDetail(DetailView):
    model = PostBlog
    template_name = 'blog/blog-details.html'

