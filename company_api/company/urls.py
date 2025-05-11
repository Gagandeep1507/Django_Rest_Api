from django.contrib import admin 
from django.urls import path , include
from company import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'company', views.CompanyViewset )
router.register(r'employee', views.EmployeeViewset)
urlpatterns = [
    path('api/v1/', include(router.urls)),  
]
