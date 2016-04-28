from django import forms

class SignupForm(forms.Form):
	name = forms.CharField(label="Name:",max_length=100)
	email = forms.CharField(label="Email", max_length=100)
	username = forms.CharField(label="Username",max_length=100)
	password = forms.CharField(label="Password",max_length=100)
	password_conf = forms.CharField(label="Password_conf",max_length=100)

class LoginForm(forms.Form):
	username = forms.CharField(label="Username",max_length=100)
	password = forms.CharField(label="Password",max_length=100)