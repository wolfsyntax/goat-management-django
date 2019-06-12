from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# User defined imports
from .forms import SignupForm

def index(request):
	print("\n\nLogin Form\n\n")

	#form = LoginForm()	

	if request.method == 'POST':
		print("\n\nForm is submitted\n\n")
		#form = LoginForm(request.POST)
		#if form.is_valid():
			#cd = form.cleaned_data
			#print("\n\nForm submitted is valid\n\n")
		#username = cd['username']
		#password = cd['password']
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			print("\n\nLogin request authenticated\n\n")
			if user.is_active :

				login(request, user)
				user_req = '/dashboard'
	
				if 'next' in request.GET :
					user_req = request.GET['next']

				return HttpResponseRedirect(user_req)

			#else:
				#messages.add_message(request, messages.INFO, "Account is not 'active'. Please contact your Administrator.")
				#return HttpResponse('Account is not active.')

		else:
			messages.add_message(request, messages.WARNING, "Invalid Username or Password.")
			#return HttpResponse('Please authenticate again')
	#else:
	#	messages.add_message(request, messages.WARNING, "Invalid request.")

		
	context = {
		'title' : 'Django',
#		'form' : form
	}

	return render(request, 'auth/login.html', context)

def register(request):

	form = SignupForm()
	if request.method == 'POST':
		
		form = SignupForm(request.POST)

		if form.is_valid():
			print("\n\nRegistration Form is valid\n\n")
			form.save()
		else:
			print("\n\nRegistration Form is invalid\n\n")	

		messages.add_message(request, messages.WARNING, "Account is not 'active'. Please contact your Administrator")

	context = {
		'title' : 'Django',
		'form' : form
	}

	return render(request, 'auth/signup.html', context)
#	return HttpResponse('Registration Form')


def destroy(request):
	logout(request)
	context = {
		'title' : 'Django',
	}

	return render(request, 'auth/logout.html', context)

#	return HttpResponse('Logout Successful.')