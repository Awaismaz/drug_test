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

