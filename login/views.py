from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def login(request): #request here refers to the login credentials that the user has submitted
    if request.method == 'POST':
        user_name = request.POST.get('user_name',False)
        password = request.POST['password']
        user = auth.authenticate(username = user_name, password=password)
        print(request.user)
        if user is not None:
            auth.login(request, user)
            if user_name=="admin" and password=="987654321":
                return redirect('adminView/')
            else:
                return redirect('../')
        else:
            return redirect("register")
    return render(request, 'login.html', {})


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if(password1 == password2):
            print(email)
            print(user_name)
            if(User.objects.filter(email=email).exists()):
                print('email exist')
                return redirect('register')
            elif (User.objects.filter(username=user_name).exists()):
                print('username exist')
            else:
                user = User.objects.create_user(username = user_name,password=password1, email=email,
                            first_name=first_name, last_name=last_name)
                user.save()
        else:
            return redirect('register')

        return redirect('login')
    return render(request, 'register.html')
