from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password, check_password
from .forms import SignupForm, LoginForm
from django.template.context_processors import csrf

def signup(request):
	errors = {}
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			f = form.cleaned_data
			password = make_password(f['password'])
			if(f['password_conf'] == f['password']):
				user = User(name=f['name'],email=f['email'],username=f['username'],password=password)
				user.save()
				request.session['name'] = user.name
				request.session['username'] = user.username
				# request.session['picture'] = user.picture
				return HttpResponseRedirect(reverse('index'))
			else:
				errors['password'] = "Passwords do not match"
		else:
			errors = form.errors
	form = SignupForm()
	return render_to_response('users/signup.html', {'form':form, 'errors':errors, 'request':request})

def login(request):
	errors = {}
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			f = form.cleaned_data
			errors['no_user'] = "The username or password entered is incorrect"
			for user in User.objects.all():
				if check_password(f['password'],user.password) and f['username']==user.username:
					request.session['name'] = user.name
					request.session['username'] = user.username
					errors = {}
					# request.session['picture'] = user.picture
		else:
			errors = form.errors

	form = LoginForm()
	return render_to_response('users/login.html',{'form':form, 'errors':errors, 'request':request})

def logout(request):
	request.session.delete()
	return HttpResponseRedirect(reverse('index'))

