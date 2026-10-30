from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def post_list_view(request):
    all_posts = Post.objects.all()                     # 1. Fetch all blog posts from the database using our Model
    context = {'posts': all_posts}                     # 2. Package them into a dictionary to send to the template
    return render(request, 'index.html', context)      # 3. Render the HTML template with the data and return it to the user

@login_required
def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.Post)
        if form.is_valid():
            post = form.save(commit=False)  # Pause saving to attach the author first
            post.author = request.user      # Automatically assign loggin-in user
            post.save()                     # Now save to the databbase
            return redirect('post_list')    # Send user back to homepage
    else:
        form = PostForm()                   # Render an empty form for GET requests

    return render(request, 'create_post.html', {'form': form})    


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)             # Auto log in user after signup
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('post_list')