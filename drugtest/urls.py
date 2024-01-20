from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('business_user/', views.business_user_form, name='business_user'),
    path('donor/', views.donor_form, name='donor'),
    path('clinical/', views.clinical, name='clinical_path'),
    path('drug_screen/', views.drug_screen, name='drug_screen_path'),
    path('test_selection/', views.test_selection, name='test_selection'),
    path('select_location/', views.select_location, name='select_location'),
    # Add other paths for additional steps
]
