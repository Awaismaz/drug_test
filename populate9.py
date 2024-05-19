import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from drugtest.models import DrugSubCategory, DrugPanel

# Ensure the "Hair Follicle Drug Tests" subcategory exists
hair_follicle_sub_category_name = "Hair Follicle Drug Tests"
hair_follicle_sub_category, created = DrugSubCategory.objects.get_or_create(name=hair_follicle_sub_category_name)

# New panels data
hair_follicle_panels_data = [
    {
        "name": "5 Panel Hair Test",
        "about": """
A 5-panel hair test refers to a type of drug test that analyzes a hair sample for the presence of specific drugs or their metabolites. This type of test typically screens for five commonly abused substances:

- Marijuana (THC)
- Cocaine
- Amphetamines (including methamphetamine)
- Opiates (such as heroin, morphine, and codeine)
- Phencyclidine (PCP)

Hair testing is a method used to detect long-term drug use, as drugs and their metabolites can be incorporated into hair follicles as they grow. This allows for the detection of drug use over a longer period compared to other testing methods like urine or saliva tests, which only detect recent drug use.

During a hair test, a small sample of hair is collected from the individual being tested, typically from the scalp. The hair is then sent to a laboratory for analysis. The laboratory will process the sample to extract any drugs or metabolites present, and then perform testing to identify and quantify these substances.

Hair testing is often used in pre-employment screening, workplace drug testing programs, and in cases where there is a need to assess an individual's drug use history over an extended period. It provides a comprehensive picture of an individual's drug use patterns and can be particularly useful in detecting chronic drug use.
        """,
        "price": 85
    },
    {
        "name": "12 Panel Hair Test",
        "about": """
A 12-panel hair test refers to a type of drug test that examines a hair sample for the presence of a broader range of drugs compared to the standard 5-panel hair test. A 12-panel hair test typically screens for the following substances:

- Marijuana (THC)
- Cocaine
- Amphetamines (including methamphetamine)
- Opiates (such as heroin, morphine, and codeine)
- Phencyclidine (PCP)
- Benzodiazepines (such as alprazolam, diazepam, and lorazepam)
- Barbiturates
- Methadone
- Propoxyphene
- Meperidine
- Tramadol
- Oxycodone

The inclusion of additional substances in a 12-panel hair test expands the scope of drug detection beyond the basic panel of drugs covered in a 5-panel test. This broader panel is often used in environments where there may be concerns about a wider range of drug use, such as in certain workplaces or for legal purposes.

Similar to other hair testing procedures, a small sample of hair is collected from the individual being tested, typically from the scalp. The hair is then sent to a laboratory for analysis. The laboratory will process the sample to extract any drugs or metabolites present and then conduct testing to identify and quantify these substances.

Hair testing, including 12-panel tests, offers a longer detection window compared to other testing methods such as urine or saliva tests, making it useful for detecting chronic drug use over an extended period. It provides comprehensive insight into an individual's drug use history, aiding in making informed decisions regarding employment, treatment, or legal matters.
        """,
        "price": 475
    },
]

# Insert or update panels
for panel in hair_follicle_panels_data:
    obj, created = DrugPanel.objects.update_or_create(
        sub_category=hair_follicle_sub_category,
        name=panel['name'],
        defaults={'about': panel['about'], 'price': panel['price']},
    )

print("Hair Follicle panels have been populated successfully.")
