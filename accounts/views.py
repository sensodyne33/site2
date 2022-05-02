from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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


def login_view(request):
    #could be post or get request to login
    if request.method == 'POST':
        #authenticate it; validate it for us
        form = AuthenticationForm(data=request.POST)
        #log user in if form is valid
        if form.is_valid():
            return redirect('articles:list')
    #if request method is GET, form is new form and we send back this new form
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})