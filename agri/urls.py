from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('',views.home1,name='home1'),
path('body/',views.body,name='body'),
path('details/',views.get_details,name='details'),
path('manuredetails/',views.ManureView.as_view(),name="manuredetails"),
path('home',views.climateAPI,name='climate'),
path('home/',views.home,name='home'),
path('home/predict',views.predict,name='predict'),
#path('predictionsView/',views.predictionsView.as_view(),name='predictionsView'),
path('manuresell/',views.manuresell,name="manuresell"),
path('viewDataBase/',views.viewDataBase,name='viewdataBase'),
path('home/updateDB',views.updateDB,name='updateDB'),
path('pestrepellents/',views.pestrepellents,name='pestrepellents'),
path('contacts/',views.contacts,name='contacts'),
path('login/',views.login,name='login')]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
