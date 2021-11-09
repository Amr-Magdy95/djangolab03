from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail

# Create your views here.
from django.http import HttpResponse
from .models import Movie


def index(request):
    latest_movies = Movie.objects.order_by("-publication_date")
    context = {
        "latest_movies": latest_movies
    }
    return render(request, 'lab02app/index.html', context)

#Create
def view_form(request):
    
    #form = Movie(request.POST, request.FILES)
    # Get the current instance object to display in the template
    #img_obj = form.instance
    return render(request, 'lab02app/postmovie.html',{})
    return render(request, 'index.html', {'form': form, 'img_obj': img_obj})



def movie_form(request):
    if request.method == "POST":
        movie_name = request.POST.get("movie_name")
        pub_date = request.POST.get("pub_date")
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        movie_object = Movie.objects.create(name=movie_name, publication_date = pub_date, file_url= file_url)
        movie_object.save()
        #send_mail("Movie Created", "Dear user an movie has been added", 
        #'', ['aaaro95@gmail.com'],fail_silently=False)
        return redirect("lab02app:index")
        return render(request, 'lab02app/index.html', {'file_url': file_url})
        #pub_date = request.POST.get("image")


        return HttpResponse( pub_date)

#Read
def movie_details(request, movie_id):
    movie = Movie.objects.get(pk = movie_id)
    from pprint import pprint
    pprint(vars(movie))
    context = {
        "movie": movie
    }
    return render(request, 'lab02app/displaymovie.html',context)
    #response = "you're looking at the result: {}".format(movie)
    #return HttpResponse(response)

#Update
def update_movie(request, movie_id):
    movie = Movie.objects.get(pk = movie_id)
    print(movie)
    context = {
    "movie": movie
    }
    return render(request, 'lab02app/onemovie.html',context)
def confirm_update(request, movie_id):
    if request.method == "POST":
        movie_name = request.POST.get("movie_name")
        pub_date = request.POST.get("pub_date")

        Movie.objects.filter(pk=movie_id).update(name=movie_name, publication_date = pub_date)

        return redirect("lab02app:index")
def delete_movie(request, movie_id):
    Movie.objects.filter(pk=movie_id).delete()
    return redirect("lab02app:index")

