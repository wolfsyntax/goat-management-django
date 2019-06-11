from django import forms
#addons
from django.contrib.auth.models import User
import re
##user defined
from .models import Purchase_record, Birth_record, GoatProfile

class GoatInfoForm(forms.Form):

	TAG_COLOR = (
		('yellow','Yellow'),
		('green', 'Green'),
		('orange', 'Orange'),
		('blue', 'Blue'),
	)

	GENDER = (
		('female', 'Female'),
		('male', 'Male'),
	)

	STATUS = (
		('active', 'Active'),
		('sold', 'Sold'),
		('deceased', 'Deceased'),
		('lost', 'Lost'),
		('stolen', 'Stolen'),
	)

	CATEGORY = (
		('birth', 'Birth'),
		('purchase', 'Purchase'),
	)

	#print("User: {}".format(user.id))
	eartag_id = forms.IntegerField(min_value=1, widget=forms.widgets.NumberInput(attrs={'class':'form-control'}), error_messages={'required':'Eartag ID is required.'})
	eartag_color = forms.ChoiceField(choices=TAG_COLOR, widget=forms.widgets.Select(attrs={'class': 'form-control'}), error_messages={'required':'Eartag Color is required.', 'invalid_choice': 'Eartag Color must be one of: yellow,green,orange,blue.'})
	nickname = forms.RegexField(regex='^[a-zA-Z]{3}[a-zA-Z ]+$', error_messages={'invalid':'Nickname may only contain alphabetical characters.','required':'Nickname is required.'})#, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
	gender = forms.ChoiceField(choices=GENDER, widget=forms.widgets.Select(attrs={'class': 'form-control'}), error_messages={'required':'Gender is required.', 'invalid_choice': 'Gender must be one of: male, female.'})
	body_color = forms.CharField(min_length=3,widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), error_messages={'required':'Body Color is required.','min_length': 'Body color must be at least 3 characters in length.'})
	category = forms.ChoiceField(choices=CATEGORY, widget=forms.widgets.RadioSelect(attrs={'class': 'form-check-input'}), error_messages={'required':'Category is required.','invalid_choice': 'Category must be one of: birth, purchase.'})
	is_castrated = forms.BooleanField(required=False, widget=forms.widgets.CheckboxInput(attrs={'class': 'form-check-input'}))
	birth_date = forms.DateField(error_messages={'required':'Birth date is required.','invalid': 'Birth date must be in the following format: yyyy-mm-dd.'})

	def clean(self):
#		print("\n\nGoat Info Form Validating ->")
		cd = super(GoatInfoForm, self).clean()
		birth_date = self.cleaned_data.get('birth_date','')
		eartag_id = self.cleaned_data.get('eartag_id','')
		eartag_color = self.cleaned_data.get('eartag_color','')
		nickname = self.cleaned_data.get('nickname','')
		gender = self.cleaned_data.get('gender','') 
		body_color = self.cleaned_data.get('body_color','')
		category = self.cleaned_data.get('category','')
		is_castrated = self.cleaned_data.get('is_castrated','')
		birth_date = self.cleaned_data.get('birth_date','')
		#print("clean (forms.py)::\nBirth Date: {}\nEartag ID: {}\n\n\n".format(birth_date, eartag_id))
		
		return cd

	def clean_eartag_id(self):
		
		value = self.cleaned_data.get('eartag_id','')	
		
		#print("\nclean_eartag_id (forms.py)::\n>Eartag ID: {}\n\n\n".format(value))
		
		if int(value) > 0:

			try:
					
				user = GoatProfile.objects.get(eartag_id=int(value))
				self.add_error('eartag_id','Eartag ID already exist.')
				print("Eartag ID already exists.")	
			except GoatProfile.DoesNotExist:
				print("clean_eartag_id (forms.py)::>Eartag ID: {} (does not exist)\n".format(value))
					#self.add_error('username','Username does not exist.')
				pass
		else:
			self.add_error('eartag_id','Eartag ID is not valid.')

		return value

	def clean_eartag_color(self):

		value = self.cleaned_data['eartag_color']
		
		#self.add_error('first_name','First Name is required.')	
		if not re.match('^\D{3,}$',value):
			self.add_error('eartag_color','Eartag Color must only contain alphabetical characters and spaces.')
		
		return value

	def clean_nickname(self):
				
		value = self.cleaned_data['nickname']
		#print("\nclean (forms.py)::\n>Nickname: {}\n\n\n".format(value))
		if len(value) < 4 :
			self.add_error('nickname','Nickname must be at least 4 characters in length.')

		return value

#	def clean_gender(self):
#		value = self.cleaned_data['gender']
		#print("\nclean (forms.py)::\n>Gender: {}\n\n\n".format(value))
#		return value

	def clean_body_color(self):
		value = self.cleaned_data['body_color']
		#print("\nclean (forms.py)::\n>Body Color: {}\n\n\n".format(value))
		
		nval = ''.join(e for e in value if e != '[' and e != ']')
		
		ls = nval.split(",")
		lx = []
		
		for lprocess in ls:
			lx.append(lprocess.split(":")[-1][1:-2])
		
		value = ', '.join(lx)
		print("\n\nNew Value: {}\n\n".format(value))
		if len(value) < 3 :
			self.add_error('body_color','Body Color must be a valid color name.')
		else:	
			if not re.match('^[a-zA-Z]{3}[a-zA-Z, ]*$', value):

				self.add_error('body_color','Body Color must be a valid color name..')


		return value

#	def clean_category(self):
#		value = self.cleaned_data['category']
		#print("\nclean (forms.py)::\n>Category: {}\n\n\n".format(value))

#		return value

#	def clean_birth_date(self):
#		value = self.cleaned_data['birth_date']
		#print("\nclean (forms.py)::\n>Birth: {}\n\n\n".format(value))
		
#		return value

	def save(self):
		print("Goat Info For is saved.\n")
		eartag_id=self.cleaned_data['eartag_id']
		eartag_color=self.cleaned_data['eartag_color']
		nickname=self.cleaned_data['nickname'].lower()
		gender=self.cleaned_data['gender']
		body_color=self.cleaned_data['body_color'].lower()
		category=self.cleaned_data['category']
		is_castrated=self.cleaned_data['is_castrated']
		birth_date=self.cleaned_data['birth_date']
		#print("Body Color: {} (before)\n".format(body_color))
		#nval = ''.join(e for e in body_color if e != '[' and e != ']')		
		#ls = nval.split(",")
		#lx = []
		#print("Body Color: {} (phase I)\n".format(nval))
		#print("Body Color: {} (phase II)\n".format(ls))
		
		#for lprocess in ls:
		#	lx.append(lprocess.split(":")[-1][1:-2])
		
		#value = ', '.join(lx)
		#print("\nSave value for body color: {}\n\n".format(value))
		data = GoatProfile(eartag_id=eartag_id, eartag_color=eartag_color, nickname=nickname, gender=gender, body_color=body_color, category=category, is_castrated=is_castrated, birth_date=birth_date)
		data.save()

class GoatPurchaseForm(forms.Form):
	
	purchase_weight = forms.DecimalField(decimal_places=2, min_value=0,max_digits=8, error_messages={'required': 'Purchase weight is required.', 'max_decimal_places': 'Purchase weight must be exact 2 decimal places.', 'invalid': 'Purchase weight must contain a decimal number.', 'min_value': 'Purchase weight must contain a number greater than or equat to 0','max_digits': 'Purchase weight cannot exceed 8 digits in length.'})
	purchase_price = forms.FloatField(max_value=100000,min_value=0, error_messages={'required':'Purchase Price is required.','invalid':'Purchase price must contain only decimal number.','min_value': 'Purchase price must contain a number greater than or equal to 0', 'max_value': 'Purchase price must contain a number less than or equal 100000'})
	purchase_date = forms.DateField(error_messages={'required': 'Purchase date is required.','invalid': 'Purchase Date must be in the following format: yyyy-mm-dd.'})
	purchase_from = forms.CharField(max_length=250,min_length=4, error_messages={'required':'Purchase From is required.', 'min_length': 'Purchase From must be at least 4 characters in length.', 'max_length':'Purchase From cannot exceed 250 characters in length.'})
	#eartag = models.ForeignKey(GoatProfile, related_name='purchase_goat', on_delete=models.CASCADE)
	#user = models.ForeignKey(User, related_name='goat_seller', on_delete=models.CASCADE)
	def clean(self):
		cd = super(GoatPurchaseForm, self).clean()
		purchase_weight = self.cleaned_data.get('purchase_weight','')	
		purchase_price = self.cleaned_data.get('purchase_price','')	
		purchase_date = self.cleaned_data.get('purchase_date','')	
		purchase_from = self.cleaned_data.get('purchase_from','')	
		return cd

#	def clean_purchase_weight(self):
#		pass

#	def clean_purchase_price(self):
#		pass

#	def clean_purchase_date(self):
#		pass

#	def clean_purchase_from(self):
#		pass

	def save(self, uid, eid):

		purchase_weight = self.cleaned_data.get('purchase_weight','')
		purchase_price = self.cleaned_data.get('purchase_price','')
		purchase_date = self.cleaned_data.get('purchase_date','')
		purchase_from = self.cleaned_data.get('purchase_from','')
		eartag_id = eid
		user_id = uid

		info = Purchase_record(purchase_weight=purchase_weight, purchase_price=purchase_price, purchase_date=purchase_date,purchase_from=purchase_from, eartag_id=eartag_id,user_id=uid)
		return info.save()

#	class Meta:
#		model = Purchase_record
	#	fields = ('dam','sire','eartag',)
#		exclude = ('eartag',)

class BirthInfoForm(forms.Form):

	birth_weight = forms.FloatField(min_value=0, max_value=1000,error_messages={'required':'Birth Weight is required.', 'max_value': 'Birth weight must contain a number less than or equal to 1000.','min_value': 'Birth weight must contain a number greater than or equal to 0.'})
	sire_id = forms.IntegerField(min_value=1, error_messages={'required':'Sire ID is required.', 'min_value': 'Sire ID must contain a number greater than or equal to 1'})
	dam_id = forms.IntegerField(min_value=1, error_messages={'required':'Dam ID is required.', 'min_value': 'Dam ID must contain a number greater than or equal to 1'})

	def clean(self):
		
		cd = super(BirthInfoForm, self).clean()
		
		birth_weight = self.cleaned_data.get('birth_weight','')
		sire_id = self.cleaned_data.get('sire_id','')
		dam_id = self.cleaned_data.get('dam_id','')		
		
		return cd

	def clean_sire_id(self):

		value = self.cleaned_data.get('sire_id','')	
		#print("\nclean_eartag_id (forms.py)::\n>Eartag ID: {}\n\n\n".format(value))
		
		if not value is None:
			if int(value) > 0:

				try:
						
					user = GoatProfile.objects.get(eartag_id=int(value),gender='male')					
					print("Eartag ID already exists.")	
				except GoatProfile.DoesNotExist:
					self.add_error('sire_id','Sire ID does not exist.')
					#print("clean_eartag_id (forms.py)::>Eartag ID: {} (does not exist)\n".format(value))
					#self.add_error('username','Username does not exist.')
					#pass
			else:

				self.add_error('sire_id','Sire ID is not valid.')

		else:
			self.add_error('sire_id','Sire ID is required.')
		
		return value

	def clean_dam_id(self):

		value = self.cleaned_data.get('dam_id','')	
		#print("\nclean_eartag_id (forms.py)::\n>Eartag ID: {}\n\n\n".format(value))
		
		if not value is None:
			if int(value) > 0:

				try:
						
					user = GoatProfile.objects.get(eartag_id=int(value),gender='female')					
					print("Dam ID already exists.")	
				except GoatProfile.DoesNotExist:
					self.add_error('dam_id','Dam ID does not exist.')
					#print("clean_eartag_id (forms.py)::>Eartag ID: {} (does not exist)\n".format(value))
					#self.add_error('username','Username does not exist.')
					#pass
			else:

				self.add_error('dam_id','Dam ID is not valid.')

		else:
			self.add_error('dam_id','Dam ID is required.')
		
		return value	

	def save(self):	

		sire = self.cleaned_data.get('sire_id','')	
		dam = self.cleaned_data.get('dam_id','')	
		birth_weight = self.cleaned_data.get('birth_weight','')	
		
		info = Birth_record(sire_id=sire,dam_id=dam,birth_weight=birth_weight)

		return info.save()

#	def clean(self):

#	def clean_sire_id(self):

#	def clean_dam_id(self):

	#class Meta:
	#	model = Birth_record
	#	fields = ('dam','sire','eartag',)
	#	exclude = ('birth',)