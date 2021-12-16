from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UsernameField
from django.contrib.auth.models import User
from django.forms import fields

class UserForm(UserCreationForm):
    email = forms.EmailField(required= True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({'class' : 'floating-input form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class' : 'floating-input form-control', 'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'class' : 'floating-input form-control', 'placeholder': 'Repetir contraseña'})
        self.fields['username'].widget.attrs.update({'class' : 'floating-input form-control', 'placeholder': 'Usuario'})
        
        for fieldname in ['username', 'password1', 'password2' , 'email']:
            self.fields[fieldname].label = ''

        for fieldname in ['username', 'password1', 'password2', 'email']:
            self.fields[fieldname].help_text = None

    def save(self, commit: True):
        user = super(UserForm, self).save(commit= False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = ''
        self.fields['username'].label = ''

    username = UsernameField(widget=forms.TextInput(attrs={'class': 'floating-input form-control', 'placeholder': 'Usuario', }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'floating-input form-control','placeholder': 'Contraseña'}))