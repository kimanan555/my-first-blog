from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import dt
from .forms import PostForm, dtForm
<<<<<<< HEAD
import pyrebase
from django.db.models import Max
=======
# import pyrebase
>>>>>>> 7e603c0a953f5f8e64a514a47a09b9709b614b9c

# config = {
#     'apiKey': "AIzaSyBKvXiRu3CmG7uIpEcJFWUhcYzGe9zN0ao",
#     'authDomain': "sn-farm.firebaseapp.com",
#     'databaseURL': "https://sn-farm.firebaseio.com",
#     'projectId': "sn-farm",
#     'storageBucket': "sn-farm.appspot.com",
#     'messagingSenderId': "1076311191237"
#   }
 
# firebase = pyrebase.initialize_app(config)
# database=firebase.database()
# auth = firebase.auth()

# def post_first(request):
#     # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/1หน้า Home.html')

# def post_detail(request):
#     return render(request, 'blog/2หน้า Cost No.1.html')

# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/3หน้า How to care.html')

# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})
def Main(request):
    return render(request, 'blog/Main.html')
def Cost(request):
#     data = database.child('Asparagus').child('EC').get().val()
    return render(request, 'blog/Cost.html')
def How_to_care(request):
    return render(request, 'blog/How_to_care.html')
def Control01(request):
#     data = database.child('Data').get().val()
    # data = database.child('Suggest').child('Asparagus').child('EC').get().val()
    return render(request, 'blog/Control01.html')
def Control02(request):
    return render(request, 'blog/Control02.html')
def Getstarto(request):
    return render(request, 'blog/Getstarto.html')
def Setting01(request):
    return render(request, 'blog/Setting01.html')
def Setting02(request):
    if request.method=="POST":
          form=dtForm(request.POST)
      #     data = database.child('Suggest').child('Asparagus').child('EC').get().val()
          if form.is_valid():
                print('valid')
                form.save()
                posts = dt.objects.order_by('num_id')
                postss=dt.objects.order_by('-id')[0]
            #     print(post[-1].pH)
            #     for post in postss:
                print(postss.pH)
            #     print(posts[1])
            #     print(posts)
                return render(request, 'blog/Setting02.html',{'form':form})
          # else:
                # print('not valid')
                # form=dtForm()
                # return render(request, 'blog/Setting02.html',{'form':form})
    else:
          form=dtForm()
          return render(request, 'blog/Setting02.html',{'form':form})

# data = database.child('Asparagus').child('EC').get().val()