from django.shortcuts import render, get_object_or_404,redirect
from .models import Chapter, Manga
from django.contrib.auth import authenticate,login,user_logged_in,logout
from django.contrib import messages

def home(request):
    mangas = Manga.objects.all()
    return render(request, 'home.html', {'mangas': mangas})

def getmanga(request, manga_id):
    chapters = Chapter.objects.filter(id=manga_id)
    name = Manga.objects.filter(id=manga_id).all()[0]
    return render(request, 'manga.html', {'chapters': chapters,'name':name,'manga_id':manga_id})

def getmangachapter(request, manga_id, chapter_number):
    chapter = get_object_or_404(Chapter, id=manga_id, chapter_number=chapter_number)
    number = [x for x in range(1,chapter.number_of_pictures+1)]
    return render(request, 'chapter.html', {'chapter': chapter, 'manga_id': manga_id, 'number':number})

def loginUser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            context={'error':'username or password is incorrect!'}
            return render(request,'login.html',context=context)
    if request.method=='GET':
        return render(request,'login.html')

def logoutUser(request):
    if user_logged_in:
        logout(request)
        return redirect('home')