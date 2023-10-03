from django import forms

class RegForm(forms.Form):
    FirstName = forms.CharField(max_length=20)
    SecondName = forms.CharField(max_length=20)
    Email = forms.EmailField()
    Password = forms.CharField(max_length=15,widget=forms.PasswordInput())
    ConfirmPassword = forms.CharField(max_length=15,widget=forms.PasswordInput())
    MobileNumber = forms.IntegerField()

class LogForm(forms.Form):
    Email = forms.EmailField()
    Password = forms.CharField(max_length=15,widget=forms.PasswordInput())

