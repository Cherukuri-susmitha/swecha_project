from django.contrib import admin
from .models import Register,ManureSell,CropPredictionModel
# Register your models here.
@admin.register(Register)
class RegisterModelAdmin(admin.ModelAdmin):
	list_display =['reg_name','number','pin_code']

@admin.register(ManureSell)
class ManureSellModelAdmin(admin.ModelAdmin):
	list_display =['id','phone_number','type_manure','selling_price','description','product_img']
@admin.register(CropPredictionModel)
class CropPredictionModelAdmin(admin.ModelAdmin):
	list_display =['nitrogen','phosporus','potassium','temperature','humidity','ph','rainfall']
