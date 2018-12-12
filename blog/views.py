from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
# import pyrebase

# config = {
#     'apiKey': "AIzaSyAk_QAxeYfqQYzKVD2MYzxKJc9YB2QqYHo",
#     'authDomain': "farm-b3a67.firebaseapp.com",
#     'databaseURL': "https://farm-b3a67.firebaseio.com",
#     'projectId': "farm-b3a67",
#     'storageBucket': "farm-b3a67.appspot.com",
#     'messagingSenderId': "997525970560"
#   }
# firebase = pyrebase.initialize_app(config)

# auth = firebase.auth()

def post_first(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/1หน้า Home.html')

def post_detail(request):
    return render(request, 'blog/2หน้า Cost No.1.html')

def post_new(request):
    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = request.user
    #         post.published_date = timezone.now()
    #         post.save()
    #         return redirect('post_detail', pk=post.pk)
    # else:
    #     form = PostForm()
    return render(request, 'blog/3หน้า How to care.html')

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})