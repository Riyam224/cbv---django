from django.shortcuts import render , get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView





#todo  CLASS BADED VIEW 

class PostListView(ListView):
    model = Post
    # context_object_name = 'all_posts'
    ordering = ['-created_at']
    # queryset = Post.objects.filter(active=True)
    # template_name = 'post/test.html'

    def get_queryset(self):
        return Post.objects.filter(active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myname"] = 'riri'
        context['lastname'] = 'kkiki'
        context['comments'] = '1'
        return context
    
    
    


class PostDetailView(DetailView):
    model = Post
    



class PostCreateView(CreateView):
    model = Post
    


class PostDeleteView(DeleteView):
    model = Post
    

class PostUpdateView(UpdateView):
    model = Post
    
