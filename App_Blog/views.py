from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse,reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import View,TemplateView,CreateView,UpdateView,DeleteView,ListView,DetailView
from App_Blog.models import Blog, Comment, Likes

import uuid # unique id

def blog_list(request):
    return render(request, 'App_Blog/blog_list.html', context={})

class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image', )
    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" +  str(uuid.uuid4()) # slug is a unique field and title can be same
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))