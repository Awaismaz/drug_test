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

class BackgroundCheckForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    maiden_name1 = forms.CharField(max_length=100, required=False, label='Maiden or All Former Names Used (1)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    maiden_name2 = forms.CharField(max_length=100, required=False, label='Maiden or All Former Names Used (2)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    ssn = forms.CharField(max_length=11, label='Social Security Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.CharField(max_length=10, label='Sex', widget=forms.TextInput(attrs={'class': 'form-control'}))
    race = forms.CharField(max_length=50, label='Race', widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), label='Date of Birth')
    phone = forms.CharField(max_length=15, label='Phone Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    current_address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Current Street Address')
    city = forms.CharField(max_length=50, label='City', widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(max_length=2, label='State', widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip_code = forms.CharField(max_length=10, label='Zip', widget=forms.TextInput(attrs={'class': 'form-control'}))
    drivers_license = forms.CharField(max_length=50, label='Drivers License Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    state_of_issuance = forms.CharField(max_length=2, label='State of Issuance', widget=forms.TextInput(attrs={'class': 'form-control'}))
    residence_history = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Residence History for the past 7 years')
    crime_charged = forms.BooleanField(required=False, label='Have you ever been charged and/or convicted of any crime or offense?', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    civil_action = forms.BooleanField(required=False, label='Have you ever been involved in a Civil Action as the Plaintiff or Defendant?', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    case_details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False, label='If you answered Yes to Numbers 1 or 2, please provide details')
    comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False, label='Comments')
    signature = forms.CharField(max_length=100, label='Signature', widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_signed = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), label='Date Signed')