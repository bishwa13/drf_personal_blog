from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from posts.models import Post



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f'Account created for {username}!', username)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile_view(request):
    user = request.user
    posts = Post.objects.filter(author=user)  # Filter posts by the logged-in user
    context = {
        'user': user,
        'posts': posts,
    }
    return render(request, 'users/profile.html', context)

