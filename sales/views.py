#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
from django.contrib.auth.decorators import login_required
## User defined

@login_required(login_url='/auth/login')
def index(request):
	context = {
		'title': ''
	}

	return render(request, 'sales/index.html', context)	

@login_required(login_url='/auth/login')
def create(request):
	context = {
		'title': ''
	}

	return render(request, 'sales/new_sale.html', context)