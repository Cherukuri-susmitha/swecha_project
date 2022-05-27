from xml.dom.minidom import Element
from django.shortcuts import render
from django.views import View
from agri.utils.crop import result
from .forms import RegisterForm,ManureSellForm,CropPredictionModelForm
from .models import Register,ManureSell,CropPredictionModel
from urllib import response
import pandas as pd 
import joblib
import requests
import json
from urllib.request import urlopen
#from django.contrib.gis.utils import GeoIP
result = result.result_dict()
def home1(request):
	return render(request,'home1.html') 

url_1 = 'http://ipinfo.io/json'
response_1 = urlopen(url_1)

data1 = json.load(response_1)
print(data1) 

modelPre = joblib.load('./model/RandomForest.pkl')
# Create your views here.


def home(request):
	temp={}
	temp['nitrogen']=90
	temp['phosporus'] = 43
	temp['potassium'] =42       
	temp['temperature'] = 28
	temp['humidity'] = 80
	temp['ph'] = 6.5
	temp['rainfall'] = 202
	context  = {'temp':temp}
	return render(request,'home.html',context)
    
    
def predict(request):
	if request.method == 'POST':
		temp={}
		temp['nitrogen'] = request.POST.get('nitrogen')
		temp['phosporus'] = request.POST.get('phosporus')
		temp['potassium'] = request.POST.get('potassium')        
		temp['temperature'] = request.POST.get('temperature')
		temp['humidity'] = request.POST.get('humidity')
		temp['ph'] = request.POST.get('ph')
		temp['rainfall'] = request.POST.get('rainfall')
	y_pred = pd.DataFrame({'x':temp}).transpose()
	'''x=['n','p','k','temp','hum','ph','rain']
    temp=[90,43,42,20.879,80.56,6.5029,202.9]
    y_pred=pd.DataFrame({'x':temp}).transpose()'''
	result1 = modelPre.predict(y_pred)
	print(result1)
	def listToString(s):
		str1 = ""
		for ele in str1:
			str += ele
		return ele
	result2 = listToString(result1)
	v = 0
	for i in result.keys():
		v=result2[1]
	context = {'result2': result2,'temp':temp}
	return render(request,'predict.html',context)    


def viewDataBase(request):
    return None

def updateDB(request):
	return None
def climateAPI(request):
    data2 = data1['loc']
    data3 =data2.split(',')
    print(data3[0])
    print(data3[1])
    lat= data3[0]
    lon=data3[1]
    url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=56752ad73f3117fc97f16a4dcf376db6'
    response = requests.get(url).json()

    temperature1 = response['main']['temp'] - 273
  
    context = {'temperature':temperature1,'humidity':response['main']['humidity'],'lat':data3[0],'lon':data3[1]}
    return render(request,'home.html',context)
    
    
def body(request):
	return render(request,'body.html')
	
	
def get_details(request):
	data = Register.objects.all()
	context = {'data' : data}
	return render(request,'details.html',context)

'''class predictionsView(View):
	def get(self,request):
		data_123 = CropPredictionModel.objects.all()
		return render(request,'predictionsView.html',{'data':data_123})'''
		
		
class ManureView(View):
	def get(self,request):
		data = ManureSell.objects.all()
		return render(request,'manuredetails.html',{'data':data})
		
		
def manuresell(request):
	manure = ManureSellForm()
	if request.method == 'POST' :
		manure= ManureSellForm(request.POST,request.FILES)
		if manure.is_valid():
			print(manure)
			manure.save()
	context = {'manure' : manure}
	return render(request,'manuresell.html',context)
	
	
def login(request):
	form1 = RegisterForm()
	if request.method == 'POST' :
		form1 = RegisterForm(request.POST)
		if form1.is_valid():
			print(form1)
			form1.save()			
	context = {'form' : form1 }
	return render(request,'login.html',context)
	
def pestrepellents(request):
	return render(request,'pestrepellents.html')
def contacts(request):
	return render(request,'contacts.html')
