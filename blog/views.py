
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .models import Post, Categories, PostComment
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, Http404
###
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class blog(ListView):
   model = Post
   template_name = 'blog_list.html'
   context_object_name = 'posts'
   cats = Categories.objects.all()
   ordering = ['-post_date']
   paginate_by = 50

   def get_context_data(self, *args, **kwargs):
      cat_list = Categories.objects.all()
      latestpost_list = Post.objects.all().order_by('-post_date')[:50]
      context = super(blog, self).get_context_data(*args, **kwargs)
      context["cat_list"] = cat_list
      context["latestpost_list"] = latestpost_list
      return context

def search(request):
   template = 'search_list.html'
   query = request.GET.get('q')
   if query:
      posts = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query)).order_by('-post_date')
   else:
      posts = Post.objects.all()

   cat_list = Categories.objects.all()
   latestpost_list = Post.objects.all().order_by('-post_date')[:50]
   paginator = Paginator(posts, 50)
   page = request.GET.get('page')
   posts = paginator.get_page(page)
   return render(request, template, {'posts':posts, 'cat_list': cat_list, 'latestpost_list':latestpost_list, 'query':query})

def CategoryView(request, cats):
   if Categories.objects.filter(categoryname=cats).exists():
      category_posts = Post.objects.filter(category__categoryname=cats).order_by('-post_date')
      cat_list = Categories.objects.all()
      latestpost_list = Post.objects.all().order_by('-post_date')[:10]
      paginator = Paginator(category_posts, 2)
      page = request.GET.get('page')
      category_posts = paginator.get_page(page)
      return render(request, 'category_list.html', {'cats':cats, 'category_posts':category_posts, 'cat_list': cat_list, 'latestpost_list':latestpost_list})
   else:
      raise Http404

class blogdetail(DetailView):
   model = Post
   template_name = 'blog_detail.html'

   def get_context_data(self, *args, **kwargs):
      cat_list = Categories.objects.all()
      latestpost_list = Post.objects.all().order_by('-post_date')[:15]
      context = super(blogdetail, self).get_context_data(*args, **kwargs)
      context["cat_list"] = cat_list
      context["latestpost_list"] = latestpost_list
      return context

@login_required(login_url='/login')
def send_comment(request, slug):
   message = request.POST.get('message')
   post_id = request.POST.get('post_id')
   post_comment = PostComment.objects.create(sender=request.user, message=message)
   post = Post.objects.filter(id=post_id).first()
   post.comments.add(post_comment)
   return redirect('.')


###########


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    #fields = ["title", "content", "image", "tags"]  # for Specifict Post
    fields = '__all__'

    def create(request):
        form = PostForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('blog/posts_form.html')
    #return render(request,'blog/posts_form.html/',{'form':form})

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse_lazy("index")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    #fields = ["title", "content", "image", "tags"]
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy("index")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return reverse_lazy("index")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
##################