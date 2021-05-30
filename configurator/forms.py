from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}),label='', max_length=256)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
     label='', max_length=256)


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               label='', max_length=256)
