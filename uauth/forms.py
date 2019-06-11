from django import forms
# Create your forms here.
## Django Library
from django.contrib.auth.models import User
## Python Library
import re

class SignupForm(forms.Form):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=150)
	email = forms.CharField(max_length=250)
	username = forms.CharField(max_length=150)
	password = forms.CharField(max_length=150, widget=forms.widgets.PasswordInput(attrs={'class':'form-control'}))
	confirm_password = forms.CharField(max_length=150, widget=forms.widgets.PasswordInput(attrs={'class':'form-control'}))

	def clean(self):

		cd = super(SignupForm, self).clean()

		first_name = self.cleaned_data.get('first_name','')
		last_name = self.cleaned_data.get('last_name','')		
		username = self.cleaned_data.get('username','')		
		email = self.cleaned_data.get('email','')		
		password = self.cleaned_data.get('password','')		
		confirm_password = self.cleaned_data.get('confirm_password','')	

		if first_name is None:
			self.add_error('first_name','First name is required.')

		return cd

	def clean_first_name(self):
		
		firstName = self.cleaned_data['first_name']

		print("first_name (clean): {}\n".format(firstName))

		if firstName is not None:
			if len(firstName) < 3:
				print("L1\n")
				self.add_error('first_name','First name must be at least 3 characters in length.')
			elif len(firstName) > 30:
				print("L2\n")
				self.add_error('first_name','First name cannot exceed 30 characters in length.')
			else:
				if not re.match('^[a-zA-Z]{3}[a-zA-Z ]+$', firstName):
					print("L3\n")
					self.add_error('first_name','First name must only contain alphabetical characters and spaces')
			
			return firstName

		else:
			self.add_error('first_name', 'First name is required.')			

		
	
	def clean_last_name(self):
		
		lastName = self.cleaned_data['last_name']

		print("last_name (clean): {}\n".format(lastName))

		if lastName is not None:
			if len(lastName) < 2:
				print("L1\n")
				self.add_error('last_name','Last name must be at least 2 characters in length.')
			elif len(lastName) > 150:
				print("L2\n")
				self.add_error('last_name','Last name cannot exceed 150 characters in length.')
			else:

				if not re.match('^[a-zA-Z]{2}[a-zA-Z ]+$', lastName):
					print("L3\n")
					self.add_error('last_name','Last name must be at least 2 alphabetical characters and spaces.')
		else:
			self.add_error('last_name', 'Last name is required.')			

		return lastName

	def clean_username(self):
		
		value = self.cleaned_data['username']
		print("username (clean): {}\n".format(value))

		if value is not None:
			if len(value) < 8:
				print("L1\n")
				self.add_error('username','Username must be at least 8 characters in length.')
			elif len(value) > 150:
				print("L2\n")
				self.add_error('username','Username cannot exceed 150 characters in length.')
			else:
				if not re.match('^[a-zA-Z_-]+$', value):
					print("L3\n")
					self.add_error('username','Username must only contain alpha-numeric characters, underscores and dashes.')
		else:
			self.add_error('username', 'Username is required.')			

		return value

	def clean_email(self):

		value = self.cleaned_data['email']
		print("email (clean): {}\n".format(value))
		if value is not None:
			if len(value) < 8:
				print("L1\n")
				self.add_error('email','Email must be at least 8 characters in length.')
			elif len(value) > 150:
				print("L2\n")
				self.add_error('email','Email cannot exceed 150 characters in length.')
			else:
				if not re.match("^[a-zA-Z_.]{4,}@[a-zA-Z]+\.com+$", value):
					print("L3\n")
					self.add_error('email','Email must be a valid address.')
		else:
			self.add_error('email', 'Email is required.')			

		return value
		
	def clean_password(self):

		value = self.cleaned_data['password']
		
		print("password (clean): {}\n".format(value))

		if value is not None:
			if len(value) < 8:
				print("L1\n")
				self.add_error('password','Password must be at least 8 characters.')
			elif len(value) > 150:
				print("L2\n")
				self.add_error('password','Password cannot exceed 150 characters.')
			else:
				if not re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*(_|[^\w])).+$', value):
					print("L3\n")
					self.add_error('password','Password must contains alpha-numeric and special characters.')
		else:
			self.add_error('password', 'Password is required.')			

		return value
	
	def clean_confirm_password(self):	

		value = self.cleaned_data['confirm_password']
		password = self.cleaned_data.get('password','')	

		print("confirm_password (clean): {}\n\tpassword : {}".format(value, password))
		
		if value is not None:	
			if value != password: 
				print("L1\n")
				self.add_error('confirm_password','Confirm password does not match.')
		else:
			print("L2\n")
			self.add_error('confirm_password', 'Confirm Password is required.')			

		return value

	def save(self):

		first_name = self.cleaned_data.get('first_name','')
		last_name = self.cleaned_data.get('last_name','')		
		username = self.cleaned_data.get('username','')		
		email = self.cleaned_data.get('email','')		
		password = self.cleaned_data.get('password','')		
		confirm_password = self.cleaned_data.get('confirm_password','')	

		user = User.objects.create_user(username=username, email=email, password=password)
		user.first_name = first_name
		user.last_name = last_name
		user.is_staff = True
		user.save()
		print("\nData save\n")
