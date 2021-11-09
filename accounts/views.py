from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    form = UserCreationForm()
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lab02app:index")


    return render(request, "registration/signup.html", context={'form': form})