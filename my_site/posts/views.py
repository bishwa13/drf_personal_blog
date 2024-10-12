# posts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/post_detail.html', {'post': post})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # dont saving at database yet
            post.author = request.user
            post.save()
            return redirect('post_list')  # Assuming there's a view for the post list
    else:
        form = PostForm()
    
    return render(request, 'posts/post_create.html', {'form': form})
