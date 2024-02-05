import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from drugtest.models import DrugSubCategory, DrugPanel

# Ensure the "Popular Tests" subcategory exists
sub_category_name = "Popular Tests"
sub_category, created = DrugSubCategory.objects.get_or_create(name=sub_category_name)

# Additional Panels data for "Popular Tests"
additional_panels_data = [
    {
        "name": "10 Panel Urine",
        "price": 89,
        "about": """
A 10-panel drug test is a type of drug screening that checks for the presence of ten different drugs or classes of drugs in a person's system. The specific substances included in a 10-panel drug test can vary based on the testing requirements of the organization or entity conducting the test. However, a standard 10-panel drug test typically covers a broad range of drugs, including commonly abused substances.

A typical 10-panel drug test often includes:

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

The 10-panel drug test is commonly used in various settings, including workplace drug testing, probation and parole programs, and other situations where a comprehensive screening for a wide range of substances is necessary. Keep in mind that the specific substances included in a drug test can be customized based on the specific needs and concerns of the organization conducting the test.
        """
    },
    {
        "name": "11 Panel Urine Drug Test",
        "price": 99,
        "about": """
An 11-panel drug test is a type of drug screening that checks for the presence of eleven different drugs or classes of drugs in a person's system. Like other multi-panel drug tests, the specific substances included in an 11-panel drug test can vary based on the testing requirements of the organization or entity conducting the test.

A standard 11-panel drug test often includes:

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

The 11-panel drug test is utilized in various settings, including workplace drug testing, probation and parole programs, and other situations where a comprehensive screening for a wide range of substances is deemed necessary. As always, the specific substances included in a drug test can be customized based on the needs and concerns of the organization conducting the test.
        """
    },
    {
        "name": "12 Panel Urine Drug Test",
        "price": 149,
        "about": """
A 12-panel drug test is a type of drug screening that checks for the presence of twelve different drugs or classes of drugs in a person's system. Similar to other multi-panel drug tests, the specific substances included in a 12-panel drug test can vary based on the testing requirements of the organization or entity conducting the test.

A standard 12-panel drug test often includes:

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

The 12-panel drug test is employed in various settings, including workplace drug testing, probation and parole programs, and other situations where a comprehensive screening for a wide range of substances is necessary. The specific substances included in a drug test can be customized based on the needs and concerns of the organization conducting the test.
        """
    },
    {
        "name": "14 Panel Urine Drug Test",
        "price": 199,
        "about": """
A 14-panel drug test is a comprehensive drug screening method that checks for the presence of fourteen different drugs or classes of drugs in a person's system. As with other multi-panel drug tests, the specific substances included in a 14-panel drug test can vary based on the testing requirements of the organization or entity conducting the test.

A standard 14-panel drug test often includes:

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

The 14-panel drug test is utilized in various settings, including workplace drug testing, probation and parole programs, and other situations where a comprehensive screening for a broad range of substances is necessary. The specific substances included in a drug test can be tailored based on the needs and concerns of the organization conducting the test.
        """
    }
]

# Insert or update panels for "Popular Tests"
for panel_data in additional_panels_data:
    DrugPanel.objects.update_or_create(
        sub_category=sub_category,
        name=panel_data["name"],
        defaults={'about': panel_data["about"], 'price': panel_data["price"]},
    )

print("Additional Popular Test Panels have been populated successfully.")
