from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('business_user/', views.business_user_form, name='business_user'),
    path('donor/', views.donor_form, name='donor'),
    path('drug_screen/', views.drug_screen, name='drug_screen_path'),

    path('test_selection_old/', views.test_selection_old, name='test_selection_old'),
    path('select_location/', views.select_location, name='select_location'),
    path('services/', views.services_view, name='services_view'),
    path('services/<int:service_id>/', views.services_view, name='services_detail'),
    path('drug-categories/<int:category_id>/', views.drug_category_details, name='drug_category_details'),
    # Add other paths for additional steps
]
