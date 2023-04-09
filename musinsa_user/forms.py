from django import forms


class UserForm(forms.Form):
    username = forms.CharField(max_length=50, label='아이디')
    password = forms.CharField( max_length=20, label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, label='비밀번호확인', widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='아이디')
    password = forms.CharField( max_length=20, label='비밀번호', widget=forms.PasswordInput)