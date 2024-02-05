from django.db import models

class DrugTest(models.Model):
    drug_class = models.CharField(max_length=10)
    subdrug = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=255)
    blood = models.BooleanField(default=False)
    urine = models.BooleanField(default=False)
    oral_fluids = models.BooleanField(default=False)
    hair = models.BooleanField(default=False)

    class Meta:
        ordering = ['drug_class', 'subdrug']

    def __str__(self):
        return f"{self.description} ({self.drug_class} - {self.subdrug})"
    
class BusinessUser(models.Model):
    business_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.business_name

class Donor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    drivers_license_number = models.CharField(max_length=20)
    # Assume relationship with DrugTest or other models if necessary

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class DrugCategory(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Drug Categories"  # Correct plural form

class DrugSubCategory(models.Model):
    drug_test = models.ForeignKey(DrugCategory, on_delete=models.CASCADE, related_name='sub_categories')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Drug Sub Categories"  # Correct plural form

class DrugPanel(models.Model):
    sub_category = models.ForeignKey(DrugSubCategory, on_delete=models.CASCADE, related_name='drug_panels')
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    panel_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

