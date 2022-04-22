from django.shortcuts import render, redirect
from django.views import View
from .models import User


class Login(View):
    def get(self, request):
        return render(request, "Login.html", {})

    def post(self, request):
        bad_password = False

        x = User.objects.get(name=request.POST['name'])
        bad_password = (x.password != request.POST["password"])

        if bad_password:
            return render(request, "Login.html", {"message": "password is incorrect, please try again!"})
        else:
            request.session["name"] = x.name
            return redirect("/Home/")