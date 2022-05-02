from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    #need to determine which request the form is sending back
    if request.method == 'POST':
        #take the data from form and validate it; check if pw is good
        form = UserCreationForm(request.POST)
        #once it's valid, save it
        if form.is_valid():
            form.save()
            #log the user in
            #send user to article:list
            return redirect('articles:list')
    #else it's a GET request
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {'form': form})