from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Put your view methods here
def register(request):
    if request.method == 'POST':
        # Register the user
        # Get form values
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        # Check if passwords match
        if password == confirmPassword:
            # Check if username is taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register') 
            else:
                # Checks if email is taken
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=firstName, last_name=lastName)
                    # Login after registering
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect('index')
                    # Just save the user if not wanting to login
                    # user.save()
                    # messages.success(request, 'You are now registered and can log in')
                    # return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')