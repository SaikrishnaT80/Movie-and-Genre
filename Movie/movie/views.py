from django.shortcuts import render,redirect
from django.views.generic import View
from movie.forms import GenreForm,MovieForm
from movie.models import Genre,Movie
from django.contrib import messages


class GenreView(View):
    def get(self,request):
        form = GenreForm()
        return render(request,"genre.html",{"form":form})
    
    def post(self,request):
        form = GenreForm(request.POST)
        if form.is_valid():
            Genre.objects.create(**form.cleaned_data) #form.save
            messages.success(request,"Genre added successfully")
        else:
            messages.error(request,"failed to add genre")
        form = GenreForm()

        return render(request,"genre.html",{"form":form})
    

class MovieView(View):
    def get(self,request,*args,**kwargs):
        form = MovieForm()
        return render(request,"movie.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form = MovieForm(request.POST)
        if form.is_valid():
            Movie.objects.create(**form.cleaned_data) #form.save
            messages.success(request,"Movie added successfully")
        else:
            messages.error(request,"failed to add Movie")
        form = MovieForm()

        return render(request,"movie.html",{"form":form})
    

class Genre_list_View(View):
    def get(self,request,*args,**kwargs):
        qs = Genre.objects.all()
        return render(request,"genre_list.html",{"qs":qs})
    
    def post(self,request,*args,**kwargs):
        name = request.POST.get("text")
        qs = Genre.objects.filter(name = name)
        return render(request,"genre_list.html",{"qs":qs})
    
class Genre_details_View(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        qs = Genre.objects.get(id=id)
        mo = Movie.objects.filter(genre_id = id)
        return render(request,"genre_details.html",{"qs":qs,"mo":mo})
    
class Genre_update_View(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        obj = Genre.objects.get(id=id)
        form = GenreForm(instance=obj)
        return render(request,"genre_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        obj = Genre.objects.get(id=id)
        
        form = GenreForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request,"Genre updated successfully")
        else:
            messages.error(request,"Failed to update genre")
        return redirect("g_list")
    

class Movie_list_View(View):
    def get(self,request,*args,**kwargs):
        qs = Movie.objects.all()
        return render(request,"movie_list.html",{"qs":qs})
    
    def post(self,request,*args,**kwargs):
        title = request.POST.get("text")
        qs = Movie.objects.filter(title=title)
        return render(request,"movie_list.html",{"qs":qs})


    

class Movie_details_View(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        qs = Movie.objects.get(id=id)
        ge = Genre.objects.filter(name = qs.genre)
        return render(request,"movie_details.html",{"qs":qs,"ge":ge})
    
class Movie_update_View(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        obj = Movie.objects.get(id=id)
        form = MovieForm(instance=obj)
        return render(request,"movie_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        obj = Movie.objects.get(id=id)
        form = MovieForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request,"Movie updated successfully")
        else:
            messages.error(request,"Failed to update movie")
        return redirect("m_list")
        


