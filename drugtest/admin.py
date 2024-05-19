from django.contrib import admin
from .models import DrugTest, DrugCategory, DrugSubCategory, DrugPanel, Service

# @admin.register(DrugTest)
# class DrugTestAdmin(admin.ModelAdmin):
#     list_display = ('drug_class', 'subdrug', 'description', 'blood', 'urine', 'oral_fluids', 'hair')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(DrugCategory)
class DrugCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(DrugSubCategory)
class DrugSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'drug_test')  # Assuming you want to display the related DrugTest name
    list_filter = ('drug_test',)  # Filter by DrugTest if needed

@admin.register(DrugPanel)
class DrugPanelAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub_category', 'about', 'price', 'panel_id')
    list_filter = ('sub_category',)  # Filter by SubCategory if needed
