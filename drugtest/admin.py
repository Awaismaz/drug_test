from django.contrib import admin
from .models import DrugTest

@admin.register(DrugTest)
class DrugTestAdmin(admin.ModelAdmin):
    list_display = ('drug_class', 'subdrug', 'description', 'blood', 'urine', 'oral_fluids', 'hair')
