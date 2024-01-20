from django import forms
from .models import BusinessUser, Donor

class BusinessUserForm(forms.ModelForm):
    class Meta:
        model = BusinessUser
        fields = ['business_name', 'name', 'address', 'email', 'phone']
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['first_name', 'last_name', 'date_of_birth', 'drivers_license_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'drivers_license_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LocationForm(forms.Form):
    zip_code = forms.CharField(label='Zip Code', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    distance_choices = forms.ChoiceField(
        label='Distance (miles)',
        choices=[(10, '10'), (20, '20'), (40, '40'), (60, '60'), (80, '80'), (99, '99')],
        widget=forms.RadioSelect
    )