from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Register(models.Model):
	reg_name = models.CharField(max_length =30)
	number=models.IntegerField(validators=[MinValueValidator(6000000000),MaxValueValidator(9999999999)],unique=True,null=False)
	pin_code=models.IntegerField()

class ManureSell(models.Model):
	phone_number = models.IntegerField(validators=[MinValueValidator(6000000000),MaxValueValidator(9999999999)],unique=True,null=False)
	type_manure=models.CharField(max_length=50)
	description = models.TextField()
	selling_price = models.FloatField()
	quantity = models.PositiveIntegerField(default=1)
	product_img = models.ImageField(upload_to = 'productimg')

class CropPredictionModel(models.Model):
    nitrogen = models.IntegerField()
    phosporus = models.IntegerField()
    potassium = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()
    
    
    
    
