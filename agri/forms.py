from django import forms
from .models import Register,ManureSell,CropPredictionModel
class RegisterForm(forms.ModelForm):
	class Meta:
		model = Register
		fields = '__all__'
class ManureSellForm(forms.ModelForm):
	class Meta:
		model = ManureSell
		fields = '__all__'
		file = forms.FileField(
		label = 'Select a file',
		help_text = 'maximum file size: 50mb',allow_empty_file=False)
class CropPredictionModelForm(forms.ModelForm):
    class Meta:
        model = CropPredictionModel
        fields = "__all__"
