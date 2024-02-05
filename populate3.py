import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from drugtest.models import DrugSubCategory, DrugPanel

# Ensure the "Drug and Alcohol Combined" subcategory exists
sub_category_name = "Drug and Alcohol Combined"
sub_category, created = DrugSubCategory.objects.get_or_create(name=sub_category_name)

# If the subcategory was just created, you might want to set additional attributes here

# Panels data
panels_data = [
    {
        "name": "5 Panel + Alcohol",
        "about": """
A standard 5-panel drug test typically includes the following substances:

- Cocaine
- Amphetamines/Methamphetamines
- Opiates (including heroin, morphine, and codeine)
- Phencyclidine (PCP)
- Marijuana (THC)
- Urine Alcohol

If you require testing for both drugs and alcohol, you might want to consider a broader panel, such as a 7-panel or 10-panel test, that includes alcohol along with additional drug classes. Keep in mind that the specific substances included in multi-panel tests can vary, so it's essential to check the details of the test kit or service you are using to ensure it meets your testing requirements.
        """,
        "price": 99
    },
    {
        "name": "6 Panel Plus Urine Alcohol",
        "about": """
A 6-panel drug test typically includes the testing for six commonly abused drugs or drug classes, and urine alcohol testing can be included as well. The specific substances included in a 6-panel drug test can vary, but a common configuration might include:

- Cocaine
- Amphetamines/Methamphetamines
- Opiates (including heroin, morphine, and codeine)
- Phencyclidine (PCP)
- Marijuana (THC)
- Benzodiazepines or Barbiturates
- Urine Alcohol

If you want to include urine alcohol testing, it's important to use a test kit or service that explicitly includes alcohol testing. Alcohol testing in urine often involves detecting ethyl glucuronide (EtG) or ethyl sulfate (EtS), which are metabolites of ethanol, the intoxicating component in alcoholic beverages.

Before conducting any testing, be sure to check the specific substances covered by the 6-panel test you are using, as the composition can vary between different providers or manufacturers. Additionally, ensure that the test kit or service meets your specific requirements for both drug and alcohol testing.
        """,
        "price": 119
    },
    {
        "name": "7 Panel + Alcohol",
        "about": """
A 7-panel drug test typically screens for seven commonly abused drugs or drug classes, and it may include alcohol testing as well. The specific substances included in a 7-panel drug test can vary, but a common configuration might include:

- Cocaine
- Amphetamines/Methamphetamines
- Opiates (including heroin, morphine, and codeine)
- Phencyclidine (PCP)
- Marijuana (THC)
- Benzodiazepines
- Barbiturates
- Urine Alcohol

If you want to include alcohol testing, you should check the details of the specific 7-panel test you are using, as the inclusion of alcohol can vary among different providers or manufacturers. Alcohol testing in urine often involves detecting metabolites such as ethyl glucuronide (EtG) or ethyl sulfate (EtS).

Always follow the instructions provided with the specific drug test kit or service you are using, and make sure it meets your testing requirements for both drugs and alcohol. If you need a more comprehensive panel that includes alcohol testing, you might also consider a 10-panel drug test, which typically covers a broader range of substances.
        """,
        "price": 125
    },
    {
        "name": "7 Panel + BAT",
        "about": """
A 7-panel drug test is a type of drug screening that looks for the presence of seven different drugs or classes of drugs in a person's system. The specific substances included in a 7-panel drug test may vary depending on the testing requirements of the organization or entity conducting the drug test. However, it typically covers a broader range of drugs compared to a 5-panel or 6-panel test.

A standard 7-panel drug test often includes:

- Marijuana (THC): Cannabis or marijuana.
- Cocaine: A powerful stimulant drug.
- Opiates: This category includes drugs like heroin and prescription opioids.
- Amphetamines: Stimulant drugs affecting the central nervous system.
- Phencyclidine (PCP): A hallucinogenic drug.
- Benzodiazepines: Medications that act as sedatives, such as diazepam (Valium) or alprazolam (Xanax).
- Barbiturates: Central nervous system depressants, which can include drugs like phenobarbital.
- Urine Alcohol

The 7-panel drug test is used in various settings, including workplace drug testing, probation and parole programs, and other situations where testing for a broader range of substances is necessary. Keep in mind that drug testing panels can be customized based on specific requirements, so the exact composition of a 7-panel drug test can vary.
        """,
        "price": 95
    },
]

# Insert or update panels
for panel in panels_data:
    obj, created = DrugPanel.objects.update_or_create(
        sub_category=sub_category,
        name=panel['name'],
        defaults={'about': panel['about'], 'price': panel['price']},
    )

print("Panels have been populated successfully.")
