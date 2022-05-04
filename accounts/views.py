from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout


# Create your views here.
def signup_view(request):
    #need to determine which request the form is sending back
    if request.method == 'POST':
        #take the data from form and validate it; check if pw is good
        form = UserCreationForm(request.POST)
        #once it's valid, save it
        if form.is_valid():
            #returns user to us
            user=form.save()
            #log the user in
            login(request,user)
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
            #find the user in DB using form
            user = form.get_user()
            #then login user
            login(request,user)
            #user log in the new url has a "next" key word
            if 'next' in request.POST:
                #if user tring to access /articles/create then
                #redirect them to the create url+template after they are logged in
                return redirect(request.POST.get('next'))
            else:
                #else redirect them to article list if their request do not contain
                #create and it's a simply log in
                return redirect('articles:list')
    #if request method is GET, form is new form and we send back this new form
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    #make a POST request to log user out
    if request.method == 'POST':
        logout(request)
        #get request and redirect to article list url
        return redirect('articles:list')

