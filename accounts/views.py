from django.shortcuts import render, redirect

# Put your view methods here
def register(request):
    if request.method == 'POST':
        # Register the user
        print('Registering the user')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # Login the user
        print('Registering the user')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')