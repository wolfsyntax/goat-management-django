from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):

	context = {
		'title' : 'Django'
	}
	return render(request, 'sitemap/index.html', context)
	#return HttpResponse('Homepage')

def about(request):

	context = {
		'title' : 'Django'
	}
	return render(request, 'sitemap/about.html', context)
#	return HttpResponse('About page')

def contact(request):

	context = {
		'title' : 'Django'
	}
	return render(request, 'sitemap/contact.html', context)
#	return HttpResponse('Contact page')	

def faq(request):

	context = {
		'title' : 'Django'
	}
	return render(request, 'sitemap/faq.html', context)
#	return HttpResponse('Support page')	

def dashboard(request):
	context = {
		'title' : 'Django'
	}
	return render(request, 'sitemap/about.html', context)
		
## Custom Error Page
def custom404(request, exception):
	return HttpResponse("PAGE NOT FOUND")

def custom403(request, exception):
	return HttpResponse("PERMISSION DENIED")

def custom500(request):
	return HttpResponse("SERVER ERROR")