import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from drugtest.models import DrugTest
from django.db.models import Count

def add_missing_sub_drugs():
    # Find drug classes with only one entry (no sub drugs)
    drug_classes_single_entry = DrugTest.objects.values('drug_class').annotate(dcount=Count('drug_class')).filter(dcount=1)

    for entry in drug_classes_single_entry:
        drug_class = entry['drug_class']

        # Get the existing single DrugTest object for this class
        drug_test = DrugTest.objects.filter(drug_class=drug_class)[0]

        # Check if the subdrug field is empty
        if not drug_test.subdrug:
            # Create a new DrugTest entry with subdrug same as drug_class
            DrugTest.objects.create(
                drug_class=drug_class,
                subdrug=drug_class,
                description=drug_test.description,  # Or any default description you want
                blood=drug_test.blood,
                urine=drug_test.urine,
                oral_fluids=drug_test.oral_fluids,
                hair=drug_test.hair
            )

            print(f'Added sub drug for drug class {drug_class}')

if __name__ == '__main__':
    add_missing_sub_drugs()
