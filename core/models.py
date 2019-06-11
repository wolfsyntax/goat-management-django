from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class GoatProfile(models.Model):
	
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

	eartag_id = models.AutoField(primary_key=True)
	eartag_color = models.CharField(choices=TAG_COLOR, max_length=10)
	nickname = models.CharField(max_length=250)
	gender = models.CharField(choices=GENDER, max_length=8)
	body_color = models.CharField(max_length=128)
	status = models.CharField(choices=STATUS, max_length=10, default='active')
	category = models.CharField(choices=CATEGORY, max_length=12)
	is_castrated = models.BooleanField(default=0)
	birth_date = models.DateField()

	class Meta:
		db_table = 'goat_profile'
		get_latest_by = 'birth_date'
		ordering = ('eartag_id',)

class Purchase_record(models.Model):
	purchase_id = models.AutoField(primary_key=True)
	purchase_weight = models.DecimalField(decimal_places=2, max_digits=8)
	purchase_price = models.FloatField()
	purchase_date = models.DateField(auto_now=True)
	purchase_from = models.CharField(max_length=250)
	eartag = models.ForeignKey(GoatProfile, related_name='purchase_goat', on_delete=models.CASCADE)
	user = models.ForeignKey(User, related_name='goat_seller', on_delete=models.CASCADE)

	class Meta:
		ordering = ('purchase_id', '-purchase_date', 'eartag_id',)
		db_table = 'purchase_record'
		get_latest_by = 'purchase_date'	


class Birth_record(models.Model):
	birth_id = models.AutoField(primary_key=True)
	birth_weight = models.FloatField()
	dam = models.ForeignKey(GoatProfile, related_name='dam_profile', on_delete=models.CASCADE)
	sire = models.ForeignKey(GoatProfile, related_name='sire_profile', on_delete=models.CASCADE)
	eartag = models.ForeignKey(GoatProfile, related_name='offspring_profile', on_delete=models.CASCADE)

	class Meta:
		ordering = ('birth_id', 'eartag_id',)
		db_table = 'birth_record'
		get_latest_by = 'birth_id'