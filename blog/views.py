from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import dt, dt2
from .forms import PostForm, dtForm, dtForm2
import pyrebase# config = {
#     'apiKey': "AIzaSyBKvXiRu3CmG7uIpEcJFWUhcYzGe9zN0ao",
#     'authDoma# config = {
#     'apiKey': "AI
from django.db.models import Max

config = {
    'apiKey': "AIzaSyBKvXiRu3CmG7uIpEcJFWUhcYzGe9zN0ao",
    'authDomain': "sn-farm.firebaseapp.com",
    'databaseURL': "https://sn-farm.firebaseio.com",
    'projectId': "sn-farm",
    'storageBucket': "sn-farm.appspot.com",
    'messagingSenderId': "1076311191237"
  }
 
firebase = pyrebase.initialize_app(config)
database=firebase.database()
auth = firebase.auth()

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
#     EC1 = database.child('Suggest').child('Asparagus').child('EC').get().val()
    return render(request, 'blog/Cost.html')
def How_to_care(request):
    EC1 = database.child('Suggest').child('Asparagus').child('EC').get().val()
    Temp1 = database.child('Suggest').child('Asparagus').child('Temp').get().val()
    Time1 = int(database.child('Suggest').child('Asparagus').child('Time').get().val())
    pH1 = database.child('Suggest').child('Asparagus').child('pH').get().val()
    EC2 = database.child('Suggest').child('Broccoli').child('EC').get().val()
    Temp2 = database.child('Suggest').child('Broccoli').child('Temp').get().val()
    Time2 = int(database.child('Suggest').child('Broccoli').child('Time').get().val())
    pH2 = database.child('Suggest').child('Broccoli').child('pH').get().val()
    EC3 = database.child('Suggest').child('Grand Rapids Lettuce').child('EC').get().val()
    Temp3 = database.child('Suggest').child('Grand Rapids Lettuce').child('Temp').get().val()
    Time3 = int(database.child('Suggest').child('Grand Rapids Lettuce').child('Time').get().val())
    pH3 = database.child('Suggest').child('Grand Rapids Lettuce').child('pH').get().val()
    form={
          'EC1':EC1, 'Temp1':Temp1, 'Time1':Time1 ,'pH1':pH1,
          'EC2':EC2, 'Temp2':Temp2, 'Time2':Time2 ,'pH2':pH2,
          'EC3':EC3, 'Temp3':Temp3, 'Time3':Time3 ,'pH3':pH3
    }
    return render(request, 'blog/How_to_care.html',form)
def Control01(request):
    EC = database.child('Field').child('Field 1').child('EC').get().val()
    Moisture = database.child('Field').child('Field 1').child('Moisture').get().val()
    Temp = database.child('Field').child('Field 1').child('Temp').get().val()
    Unit_Electric = database.child('Field').child('Field 1').child('Unit Electric').get().val()
    Unit_Water = database.child('Field').child('Field 1').child('Unit Water').get().val()
    Velocity = database.child('Field').child('Field 1').child('Velocity').get().val()
    pH = database.child('Field').child('Field 1').child('pH').get().val()
    form={
          'EC':EC, 'Moisture':Moisture, 'Temp':Temp, 'Unit_Electric':Unit_Electric, 
          'Unit_Water':Unit_Water, 'Velocity':Velocity, 'pH':pH
    }
    return render(request, 'blog/Control01.html',form)
def Control02(request):
    EC = database.child('Field').child('Field 2').child('EC').get().val()
    Moisture = database.child('Field').child('Field 2').child('Moisture').get().val()
    Temp = database.child('Field').child('Field 2').child('Temp').get().val()
    Unit_Electric = database.child('Field').child('Field 2').child('Unit Electric').get().val()
    Unit_Water = database.child('Field').child('Field 2').child('Unit Water').get().val()
    Velocity = database.child('Field').child('Field 2').child('Velocity').get().val()
    pH = database.child('Field').child('Field 2').child('pH').get().val()
    form={
          'EC':EC, 'Moisture':Moisture, 'Temp':Temp, 'Unit_Electric':Unit_Electric, 
          'Unit_Water':Unit_Water, 'Velocity':Velocity, 'pH':pH
    }
    return render(request, 'blog/Control02.html',form)
def Getstarto(request):
    return render(request, 'blog/Getstarto.html')
def Setting01(request):
    if request.method=="POST":
          form=dtForm2(request.POST)
          if form.is_valid():
                form.save()
                posts=dt2.objects.order_by('-id')[0]
                database.child("Input Field").child("Field 1").child("EC").set(posts.Ec)
                database.child("Input Field").child("Field 1").child("Temp").set(posts.temp)
                database.child("Input Field").child("Field 1").child("pH").set(posts.pH)
                database.child("Input Field").child("Field 1").child("Water").set(posts.Water)
                return render(request, 'blog/Setting01.html',{'form':form})
          # else:
                # print('not valid')
                # form=dtForm()
                # return render(request, 'blog/Setting02.html',{'form':form})
    else:
          form=dtForm()
          return render(request, 'blog/Setting01.html',{'form':form})

def Setting02(request):
    if request.method=="POST":
          form=dtForm(request.POST)
          if form.is_valid():
                form.save()
                posts=dt.objects.order_by('-id')[0]
                database.child("Input Field").child("Field 2").child("EC").set(posts.Ec)
                database.child("Input Field").child("Field 2").child("Temp").set(posts.temp)
                database.child("Input Field").child("Field 2").child("pH").set(posts.pH)
                database.child("Input Field").child("Field 2").child("Water").set(posts.Water)
                return render(request, 'blog/Setting02.html',{'form':form})
          # else:
                # print('not valid')
                # form=dtForm()
                # return render(request, 'blog/Setting02.html',{'form':form})
    else:
          form=dtForm()
          return render(request, 'blog/Setting02.html',{'form':form})

# data = database.child('Asparagus').child('EC').get().val(