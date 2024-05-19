import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from drugtest.models import DrugSubCategory, DrugPanel

# Ensure the "Background Search" subcategory exists
background_search_sub_category_name = "Background Search"
background_search_sub_category, created = DrugSubCategory.objects.get_or_create(name=background_search_sub_category_name)

# New panel data
background_search_panel_data = {
    "name": "Triple Database Package",
    "about": """
When Register is clicked, you will be asked followind data:

- National Criminal Index
- Registered Sex Offender Registry
- Terrorism Registry (Do Not Fly List)

A Social Security Number Trace is included at no additional charge.

How long do database background check results take?
Results of database background checks are very quick. We review the database report before reporting it to the employer. Reports are generally returned on the same or the next business day.

How do Employment Background Checks work?
An electronic waiver will be emailed and/or texted to the person you wish to screen. When he or she e-signs that form, granting you the right to get their background check, we'll automatically begin running their report. Results are reported back in our secure online portal.
    """,
    "price": 99.00
}

# Insert or update panel
obj, created = DrugPanel.objects.update_or_create(
    sub_category=background_search_sub_category,
    name=background_search_panel_data['name'],
    defaults={'about': background_search_panel_data['about'], 'price': background_search_panel_data['price']},
)

print("Background Search panel has been populated successfully.")
