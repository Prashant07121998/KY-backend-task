from django.contrib.auth.models import User
from django import  forms
from .models import Profile


class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =['username','email','password']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']

class SignupForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    college_name = forms.CharField(max_length=200)
    phone_number = forms.IntegerField()
    fb_profile_link = forms.CharField()

    class Meta:
        model = Profile
        fields = ['full_name', 'college_name', 'phone_number', 'fb_profile_link']


    def signup(self, request, user):
        # I think the profile will exist at this point based on
        # your post_save_create. But if not, just create it here
        if user.profile:
            user.profile.full_name = self.cleaned_data['full_name']
            user.profile.college_name = self.cleaned_data['college_name']
            user.profile.phone_number = self.cleaned_data['phone_number']
            user.profile.fb_profile_link = self.cleaned_data['fb_profile_link']
            user.profile.save()
