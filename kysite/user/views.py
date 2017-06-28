
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout

from django.views.generic import View
from .forms import UserForm



def index(request):
    return render(request,'user/index.html',)

def login(request):
    return render(request,'user/loginform/index.html',)


class UserFormView(View):
    form_class = UserForm
    template_name ='user/register_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request, self.template_name, {'form':form})


    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:

                    return render(request,'user/register_success.html',{'user':user})

        return render(request, self.template_name, {"form": form})

class LoginView(View):
    template_name='user/login123.html'

    def get(self,request):
        return render(request, self.template_name,)

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return render(request,'user/login_success.html',{'user':user})
        return render(request, self.template_name, )




def logoutuser(request):
    auth_logout(request)
    return redirect('user1:index')





