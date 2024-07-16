from django.shortcuts import render
from management.models import User
from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed
from django.shortcuts import redirect


def frontpage(request):
    return render(request, 'core/base.html')


def signup(request):
    if request.method == "POST":
        number = request.data['number']
        password = request.data['password']
        user = User.objects.filter(number=number).first()
        if not user:
            raise NotAuthenticated("User is not found !")

        if not user.check_password(password):
            raise AuthenticationFailed("Password is incorrect !")

        return redirect('frontpage')


