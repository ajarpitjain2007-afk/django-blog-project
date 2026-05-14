from django.shortcuts import render , redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from .models import Post , Comment
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.http import JsonResponse
from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404

# Create your views here.


# posts =[

#     {'title': 'coding',
#     'author': 'dragon',
#     'content': 'this is my first blog',
#     'Date': 'i dont'
#      },
#     {'title': 'hacking',
#     'author': 'meaony',
#     'content': 'this is also my first blog',
#     'Date': 'i dont know'
#      }

#      ]
def home(request):

    context = [ 
        
        {
        'posts': Post.objects.all()
}
]

    return render(request,'blog/blog.html', context={'posts':Post.objects.all()})


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-Date']
    paginate_by = 7

class PostDetailView(DetailView):
    model = Post
   


    
    


class PostCreateView(CreateView,LoginRequiredMixin):
    model = Post
    fields = ['title','content']
    success_url = '/'


    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(UpdateView,LoginRequiredMixin,UserPassesTestMixin):
    model = Post
    fields = ['title','content']
    success_url = '/'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(DeleteView,LoginRequiredMixin,UserPassesTestMixin):
    model = Post
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    



def about(request):
    return render(request,'blog/about.html')



def BlogLikes(request,pk):
    
    post = get_object_or_404(Post, pk=pk)

    liked = False

    if request.method == "POST":

        if request.user in post.like.all():
            post.like.remove(request.user)
        else:
            post.like.add(request.user)
            liked = True

    return JsonResponse({
        'liked': liked,
        'total_likes': post.total_likes()
    })




def add_comment(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST" and request.user.is_authenticated:
        content = request.POST.get('content')
        if content:
             Comment.objects.create(
                post=post,
                author=request.user,
                content=content 
            )

    return redirect('blog-detail',pk=post.pk)

           
    
def ProfileView(request , id):
     if request.user.id == id:
         return render(request,"users/profile.html")
     else:
        #  ph = User.objects.filter(post__isnull=False).distinct()
         usr = User.objects.get(id=id)
         return render(request,"blog/ProfileView.html", {"usr":usr})