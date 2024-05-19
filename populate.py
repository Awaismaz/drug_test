import os
import django
from drugtest.models import DrugTest
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
# Create a DataFrame
df = pd.read_csv('drugdata.csv')

# Iterate and populate the database

for _, row in df.iterrows():
    drug_class = str(row['DRUG CLASS']).zfill(6)
    
    # Convert to integer before zero-filling, and handle NaN values
    subdrug = str(int(row['SUBDRUG'])).zfill(6) if pd.notna(row['SUBDRUG']) else ''

    DrugTest.objects.create(
        drug_class=drug_class,
        subdrug=subdrug,
        description=row['Description'],
        blood=bool(row['BLOOD']),
        urine=bool(row['URINE']),
        oral_fluids=bool(row['ORAL FLUIDS']),
        hair=bool(row['HAIR'])
    )
