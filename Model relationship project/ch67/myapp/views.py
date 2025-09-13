from django.shortcuts import render
from myapp.models import Page, Post, Song
from django.contrib.auth.models import User

def home(request):
  return render(request, 'myapp/home.html')

def show_user_data(request):
    data_1 = User.objects.all()
    data_2 = User.objects.filter(email="gubrani@gmai.com")
    data_3 = User.objects.filter(mypage__pcat="cricket matches")
    data_4 = User.objects.filter(post__ptpublished="2025-09-13")
    data_5 = User.objects.filter(song__sduration=3)
    return render(request, 'myapp/user.html',{'data1':data_1,'data2':data_2,'data3':data_3,'data4':data_4,'data5':data_5})

def show_page_data(request):
  data1 = Page.objects.all()
  data2 = Page.objects.filter(pcat="Tech")
  data3 = Page.objects.filter(user__email="rajeshkumar@gmail.com")
  return render(request, 'myapp/page.html',{'data1':data1,'data2':data2,'data3':data3})

def show_post_data(request):
  data1 = Post.objects.all()
  data2 = Post.objects.filter(ptpublished='2025-09-13')
  data3 = Post.objects.filter(user__username='raj')
  return render(request, 'myapp/post.html',{'data1':data1,'data2':data2,'data3':data3})

def show_song_data(request):
  data1 = Song.objects.all()
  data2 = Song.objects.filter(sduration=4)
  data3 = Song.objects.filter(user__username='sahil')
  return render(request, 'myapp/song.html',{'data1':data1,'data2':data2,'data3':data3})
