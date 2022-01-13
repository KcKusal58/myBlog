from django.db.models import fields
from django.http import request
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Blog, Contact
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import math

# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    no_of_posts = 6
    #if request.GET['pageno']
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    
    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = blogs[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page-1
    else:
        prev = None
    if page<math.ceil(length/no_of_posts):  
        nxt = page + 1
    else:
        nxt = None
    context = {'blogs': blogs, 'prev': prev, 'nxt': nxt}
    return render(request, 'bloghome.html', context)

class PostListView(ListView):
        model = Blog
        template_name = 'bloghome.html'
        context_object_name = 'blogs'
        #ordering = ['-date_posted']

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name= 'blog_form.html'
    fields = ['title', 'content', 'short_desc','slug']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name= 'blog_form.html'
    fields = ['title', 'content', 'short_desc', 'slug']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, DeleteView):
        model = Blog
        template_name= 'blog_confirm_delete.html'
        success_url = '/blog/'
        def test_func(self):
            post = self.get_object()
            if self.request.user == post.user:
             return True
            return False
        

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog': blog}

    return render(request, 'blogpost.html', context)


def search(request):
    return render(request, 'search.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        instance = Contact(name=name, email=email,phone=phone,desc=desc)
        instance.save()
    return render(request, 'contact.html')

def leafle(request):
    return render(request, 'leaf.html')