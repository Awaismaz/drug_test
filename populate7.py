import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from drugtest.models import DrugSubCategory, DrugPanel


# Ensure the "Popular Tests" subcategory exists
sub_category_name = "Popular Tests"
sub_category, created = DrugSubCategory.objects.get_or_create(name=sub_category_name)

# Define the new panels to be added to "Popular Tests"
new_panels_data = [
    {
        "name": "16 Panel Urine Drug Test",
        "price": 250,
        "about": """
A 16-panel drug test is an extended and comprehensive drug screening method that checks for the presence of sixteen different drugs or classes of drugs in a person's system. The specific substances included in a 16-panel drug test can vary based on the testing requirements of the organization or entity conducting the test.

While the composition can vary, a standard 16-panel drug test may include the following:

- Marijuana (THC): Cannabis or marijuana.
- Cocaine: A powerful stimulant drug.
- Opiates: This category includes drugs like heroin and prescription opioids.
- Amphetamines: Stimulant drugs affecting the central nervous system.
- Phencyclidine (PCP): A hallucinogenic drug.
- Benzodiazepines: Medications that act as sedatives, such as diazepam (Valium) or alprazolam (Xanax).
- Barbiturates: Central nervous system depressants.
- Methamphetamines: Stimulant drugs, including methamphetamine.
- Methadone: A synthetic opioid often used in the treatment of opioid addiction.
- Propoxyphene: An opioid pain medication.
- Ecstasy (MDMA): A synthetic drug with stimulant and hallucinogenic properties.
- Tricyclic Antidepressants (TCAs): A class of antidepressant medications.
- Oxycodone: A prescription opioid painkiller.
- Buprenorphine: A medication used in opioid addiction treatment.
- Barbiturate: Specific barbiturates not covered in the basic panel.
- Fentanyl: A potent synthetic opioid painkiller.

The 16-panel drug test is employed in various settings, including workplace drug testing, probation and parole programs, and other situations where a highly comprehensive screening for a wide range of substances is necessary. The specific substances included in a drug test can be customized based on the needs and concerns of the organization conducting the test.
        """
    },
    {
        "name": "20 Panel Urine Drug Test (All opiates)",
        "price": 299,
        "about": """
A 20-panel drug test is an extensive and highly comprehensive drug screening method that checks for the presence of twenty different drugs or classes of drugs in a person's system. The specific substances included in a 20-panel drug test can vary based on the testing requirements of the organization or entity conducting the test. Such tests are typically utilized in situations where an extensive screening for a broad range of substances is deemed necessary.

While the composition can vary, a standard 20-panel drug test may include the following:

- Marijuana (THC): Cannabis or marijuana.
- Cocaine: A powerful stimulant drug.
- Opiates: This category includes drugs like heroin and prescription opioids.
- Amphetamines: Stimulant drugs affecting the central nervous system.
- Phencyclidine (PCP): A hallucinogenic drug.
- Benzodiazepines: Medications that act as sedatives, such as diazepam (Valium) or alprazolam (Xanax).
- Barbiturates: Central nervous system depressants.
- Methamphetamines: Stimulant drugs, including methamphetamine.
- Methadone: A synthetic opioid often used in the treatment of opioid addiction.
- Propoxyphene: An opioid pain medication.
- Ecstasy (MDMA): A synthetic drug with stimulant and hallucinogenic properties.
- Tricyclic Antidepressants (TCAs): A class of antidepressant medications.
- Oxycodone: A prescription opioid painkiller.
- Buprenorphine: A medication used in opioid addiction treatment.
- Barbiturate: Additional barbiturates not covered in the basic panel.
- Fentanyl: A potent synthetic opioid painkiller.
- Meperidine: A synthetic opioid painkiller.
- Methaqualone: A sedative and hypnotic medication.
- Ketamine: A dissociative anesthetic with hallucinogenic effects.
- Tramadol: An opioid pain medication.

The 20-panel drug test is utilized in various settings, including workplace drug testing, probation and parole programs, and other situations where an exceptionally comprehensive screening for a wide range of substances is necessary. The specific substances included in a drug test can be tailored based on the needs and concerns of the organization conducting the test.
        """
    },
    {
        "name": "22 Panel",
        "price": 399,
        "about": """
A 22-panel drug test is an even more extensive and comprehensive drug screening method that checks for the presence of twenty-two different drugs or classes of drugs in a person's system. The specific substances included in a 22-panel drug test can vary based on the testing requirements of the organization or entity conducting the test. Such tests are typically utilized in situations where an exceptionally thorough screening for a broad range of substances is deemed necessary.

While the composition can vary, a standard 22-panel drug test may include the following:

- Marijuana (THC): Cannabis or marijuana.
- Cocaine: A powerful stimulant drug.
- Opiates: This category includes drugs like heroin and prescription opioids.
- Amphetamines: Stimulant drugs affecting the central nervous system.
- Phencyclidine (PCP): A hallucinogenic drug.
- Benzodiazepines: Medications that act as sedatives, such as diazepam (Valium) or alprazolam (Xanax).
- Barbiturates: Central nervous system depressants.
- Methamphetamines: Stimulant drugs, including methamphetamine.
- Methadone: A synthetic opioid often used in the treatment of opioid addiction.
- Propoxyphene: An opioid pain medication.
- Ecstasy (MDMA): A synthetic drug with stimulant and hallucinogenic properties.
- Tricyclic Antidepressants (TCAs): A class of antidepressant medications.
- Oxycodone: A prescription opioid painkiller.
- Buprenorphine: A medication used in opioid addiction treatment.
- Barbiturate: Additional barbiturates not covered in the basic panel.
- Fentanyl: A potent synthetic opioid painkiller.
- Meperidine: A synthetic opioid painkiller.
- Methaqualone: A sedative and hypnotic medication.
- Ketamine: A dissociative anesthetic with hallucinogenic effects.
- Tramadol: An opioid pain medication.
- EDDP (Methadone Metabolite): A metabolite of methadone.
- EtG (Ethyl Glucuronide): A metabolite of ethanol (alcohol).

The 22-panel drug test is utilized in various settings, including workplace drug testing, probation and parole programs, and other situations where an extremely comprehensive screening for a wide range of substances is necessary. The specific substances included in a drug test can be customized based on the needs and concerns of the organization conducting the test.
        """
    }
]

# Insert or update the new panels for "Popular Tests"
for panel_data in new_panels_data:
    DrugPanel.objects.update_or_create(
        sub_category=sub_category,
        name=panel_data["name"],
        defaults={'about': panel_data["about"], 'price': panel_data["price"]},
    )

print("New Popular Test Panels have been populated successfully.")
