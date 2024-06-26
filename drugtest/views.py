from django.shortcuts import render, redirect
from .forms import BusinessUserForm, DonorForm, LocationForm, BackgroundCheckForm
from .models import DrugTest, DrugCategory
from django.conf import settings
import os
def home(request):
    # Home page with options to select test or site
    return render(request, 'drugtest/home.html')

def business_user_form(request):
    if request.method == 'POST':
        form = BusinessUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor')  # Redirect to the next step
    else:
        form = BusinessUserForm()
    return render(request, 'drugtest/business_user_form.html', {'form': form})

def donor_form(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test_selection')  # Redirect to the test selection page
    else:
        form = DonorForm()
    return render(request, 'drugtest/donor_form.html', {'form': form})

def drug_screen(request):
    # Logic for Drug Screen path
    return render(request, 'drugtest/drug_screen.html')

from django.shortcuts import render
from .models import Service


def services_view(request):
    selected_service_id = request.GET.get('service_id')
    services = Service.objects.all()
    selected_service = None
    if selected_service_id:
        selected_service = Service.objects.filter(id=selected_service_id).first()
    return render(request, 'drugtest/services_page.html', {
        'services': services,
        'selected_service': selected_service
    })



def test_selection_old(request):
    # Fetch all drug tests
    all_drug_tests = DrugTest.objects.all().order_by('drug_class', 'subdrug')

    # Prepare unique drug classes with their descriptions
    drug_test_details = {}
    for dt in all_drug_tests:
        if dt.drug_class not in drug_test_details:
            drug_test_details[dt.drug_class] = {
                'description': dt.description,
                'sub_drugs': []
            }
        if dt.subdrug:
            drug_test_details[dt.drug_class]['sub_drugs'].append(dt)

    return render(request, 'drugtest/test_selection_old.html', {'drug_tests': drug_test_details})


def display_sites(request):
    # You might store the sites in the session or pass them in another way
    sites = request.session.get('sites', [])
    return render(request, 'drugtest/display_sites.html', {'sites': sites})


from zeep import Client

def select_location(request, id):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            wsdl_path = os.path.join(settings.BASE_DIR, "LabcorpOTS.wsdl")
            client = Client(wsdl=wsdl_path)
            response = client.service.matchSites(
                userId='ESITESTING', 
                password='Solutions4mee!', 
                zipCode=form.cleaned_data['zip_code'], 
                searchRadius=form.cleaned_data['distance_choices']
            )

            # Assuming response is an array of sites
            sites = response[:12]  # Limit to 12 sites
            print(sites)
            return render(request, 'drugtest/display_sites.html', {'sites': sites})
    else:
        form = LocationForm()

    return render(request, 'drugtest/select_location.html', {'form': form})


def contact(request):
    pass

def order_kit(request):
    pass

def background_search(request):
    if request.method == 'POST':
        form = BackgroundCheckForm(request.POST)
        if form.is_valid():
            # Process the form data (save to database, send email, etc.)
            # ...
            return redirect('success_url')  # Replace 'success_url' with your actual success URL
    else:
        form = BackgroundCheckForm()
    
    return render(request, 'drugtest/background_search.html', {'form': form})


def drug_category_details(request, category_id):
    services = Service.objects.all()
    category = DrugCategory.objects.prefetch_related('sub_categories__drug_panels').get(id=category_id)
    selected_service = category.service  # Access the parent service directly from the category instance
    
    return render(request, 'drugtest/drug_category_details.html', {
        'category': category,
        'services': services,
        'selected_service': selected_service,  # Add the selected_service to the context
    })
