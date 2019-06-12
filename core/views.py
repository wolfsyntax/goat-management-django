from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404

# Create your views here.
from django.contrib.auth.decorators import login_required
## User defined
from .models import GoatProfile, Birth_record, Purchase_record
from .forms import GoatInfoForm, GoatPurchaseForm, BirthInfoForm, EditInfoForm

@login_required(login_url='/auth/login')
def index(request):
	goatInfForm = GoatInfoForm()

	context = {
		'title': 'GOAT'
	}

	flag = False

	dam_lib = GoatProfile.objects.filter(gender__iexact='female').only("eartag_id")#.values_list('eartag_id')
	sire_lib = GoatProfile.objects.filter(gender__iexact='male').only("eartag_id")#.values_list ('eartag_id')

	if request.method == 'POST':
		goatInfForm = GoatInfoForm(request.POST)

		if goatInfForm.is_valid():
			
			cd = goatInfForm.cleaned_data
			
			
			#print("Body Color: {}\n\n".format(cd['body_color']))
			if cd['category'] == 'purchase':
				extra_form = GoatPurchaseForm(request.POST)
				flag = True
				if extra_form.is_valid():
					#return HttpResponse("Goat Purchase Form is submitted and validated")	
					goatInfForm.save()
					extra_form.save(request.user.id,cd['eartag_id'])
					return HttpResponseRedirect("/goat")
					#print("Goat Purchase Form is valid.\n")
			else:
				extra_form = BirthInfoForm(request.POST)
				if extra_form.is_valid():
					#return HttpResponse("Birth Info is submitted and validated")	
					goatInfForm.save()
					extra_form.save(cd['eartag_id'])

					return HttpResponseRedirect("/goat")
					print("Goat Birth Form is valid.\n")
			print("Extras: {}\n".format(extra_form.cleaned_data))
			context.setdefault('plus_form',extra_form)
			

			#print("\n\n{}\n\n{}".format(cd,request.POST['body_color']))
			

			#return HttpResponse("Goat Info Form is submitted and validated")	
		#return HttpResponse("Form was submitted")
	
	#context = {
	#	'title': 'GOAT',
	#	'form': goatInfForm
	#}
	context.setdefault('form',goatInfForm)
	context.setdefault('dam_rec',dam_lib)
	context.setdefault('sire_rec',sire_lib)
	context.setdefault('flag',flag)
	#return render(request,'sales/index.html',context)
	return render(request,'core/new_goat.html',context)
	#return HttpResponse('Goat Management')

#def dashboard(request):
@login_required(login_url='/auth/login')
def manage(request):
	print("\n\nURL: goat/\nUser ID: {}\n\n".format(request.user.id))

	context = {
		'title': 'GOAT',
		'goat_rec': GoatProfile.objects.all()
	}

	return render(request,'core/list_goat.html',context)
	#return HttpResponse('Goat Profile - List')

@login_required(login_url='/auth/login')
def edit_goat(request, tag_id):

	flag = False

	context = {
		'title': 'GOAT'	
	}

	if request.method == 'GET':

		goat_info = get_object_or_404(GoatProfile, eartag_id=tag_id)
		context.setdefault('goat_rec', goat_info)
		
		if goat_info.category == 'birth':
			extra_info = get_object_or_404(Birth_record, eartag_id=tag_id)
			flag = False
		else:
			flag = True
			extra_info = get_object_or_404(Purchase_record, eartag_id=tag_id)

		context.setdefault('extra_rec', extra_info)
		
		
	else:

		goatInfForm = EditInfoForm(request.POST)
		print("\n\nEdit form is submitted.\n\n\n")
		if goatInfForm.is_valid():
			
			cd = goatInfForm.cleaned_data
			
			
			#print("Body Color: {}\n\n".format(cd['body_color']))
			if cd['category'] == 'purchase':
				extra_form = GoatPurchaseForm(request.POST)
				flag = True
				if extra_form.is_valid():
					#return HttpResponse("Goat Purchase Form is submitted and validated")	
					goatInfForm.save()
					extra_form.save(request.user.id,cd['eartag_id'])
					#print("Goat Purchase Form is valid.\n")
			else:
				extra_form = BirthInfoForm(request.POST)
				if extra_form.is_valid():
					#return HttpResponse("Birth Info is submitted and validated")	
					goatInfForm.save()
					extra_form.save(cd['eartag_id'])
					print("Goat Birth Form is valid.\n")
			#print("Extras: {}\n".format(extra_form.cleaned_data))
			context.setdefault('plus_form',extra_form)
			context.setdefault('form',goatInfForm)
			
	dam_lib = GoatProfile.objects.filter(gender__iexact='female').only("eartag_id")#.values_list('eartag_id')
	sire_lib = GoatProfile.objects.filter(gender__iexact='male').only("eartag_id")#.values_list ('eartag_id')

	context.setdefault('dam_rec',dam_lib)
	context.setdefault('sire_rec',sire_lib)
	context.setdefault('flag', flag)

	return render(request,'core/edit_goat.html',context)	
	#return HttpResponse('Goat Manage (edit): {}'.format(tag_id))

@login_required(login_url='/auth/login')
def view_goat(request, tag_id):
	goat_info = get_object_or_404(GoatProfile, eartag_id=tag_id)
	if goat_info.category == 'birth':
		extra_info = get_object_or_404(Birth_record, eartag_id=tag_id)
	else:
		extra_info = get_object_or_404(Purchase_record, eartag_id=tag_id)
	
	context = {
		'title': 'GOAT',
		'goat_rec' : goat_info,#GoatProfile.objects.get(eartag_id=tag_id)
		'plus_form': extra_info
	}
	

	return render(request,'core/show_goat.html',context)	
	#return HttpResponse('Goat Manage (view): {}'.format(tag_id))
