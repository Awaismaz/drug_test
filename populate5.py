import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from drugtest.models import DrugSubCategory, DrugPanel

# Ensure the "Popular Tests" subcategory exists
sub_category_name = "Popular Tests"
sub_category, created = DrugSubCategory.objects.get_or_create(name=sub_category_name)

# Panels data for "Popular Tests"
panels_data = [
    {
        "name": "6 Panel Urine Drug Test",
        "price": 84,
        "about": """
A 6-panel drug test is a type of drug screening that looks for the presence of six different drugs or classes of drugs in a person's system. It is similar to the 5-panel drug test but includes an additional substance. The specific drugs included in a 6-panel drug test may vary, but commonly, they cover:

- Marijuana (THC): Cannabis or marijuana.
- Cocaine: A powerful stimulant drug.
- Opiates: This category includes drugs like heroin and prescription opioids.
- Amphetamines: Stimulant drugs affecting the central nervous system.
- Phencyclidine (PCP): A hallucinogenic drug.
- Benzodiazepines: Medications that act as sedatives, such as diazepam (Valium) or alprazolam (Xanax).

The 6-panel drug test is often used in various settings, including workplace drug testing, probation and parole programs, and other situations where testing for a broader range of substances is deemed necessary. Keep in mind that drug testing panels can be customized based on specific requirements or concerns, so the exact composition of a 6-panel drug test can vary depending on the organization or entity conducting the test.
"""
    },
    # The remaining panels follow the same structure
    {
        "name": "7 Panel Urine",
        "price": 95,
        "about": ("""
A 7-panel drug test is a type of drug screening that looks for the presence of seven different drugs or classes of drugs in a person's system. The specific substances included in a 7-panel drug test may vary depending on the testing requirements of the organization or entity conducting the drug test. However, it typically covers a broader range of drugs compared to a 5-panel or 6-panel test.

A standard 7-panel drug test often includes:

- Marijuana (THC): Cannabis or marijuana.
- Cocaine: A powerful stimulant drug.
- Opiates: This category includes drugs like heroin and prescription opioids.
- Amphetamines: Stimulant drugs affecting the central nervous system.
- Phencyclidine (PCP): A hallucinogenic drug.
- Benzodiazepines: Medications that act as sedatives, such as diazepam (Valium) or alprazolam (Xanax).
- Barbiturates: Central nervous system depressants, which can include drugs like phenobarbital.

The 7-panel drug test is used in various settings, including workplace drug testing, probation and parole programs, and other situations where testing for a broader range of substances is necessary. Keep in mind that drug testing panels can be customized based on specific requirements, so the exact composition of a 7-panel drug test can vary.
""")
    },
    {
        "name": "8 Panel Urine Drug Test",
        "price": 84,
        "about": ("""
An 8-panel drug test is a type of drug screening that looks for the presence of eight different drugs or classes of drugs in a person's system. Like other drug tests, the specific substances included in an 8-panel drug test can vary based on the testing requirements of the organization or entity conducting the test. However, it typically covers a wider range of drugs compared to tests with fewer panels.

A standard 8-panel drug test often includes:

- Marijuana (THC): Cannabis or marijuana.
- Cocaine: A powerful stimulant drug.
- Opiates: This category includes drugs like heroin and prescription opioids.
- Amphetamines: Stimulant drugs affecting the central nervous system.
- Phencyclidine (PCP): A hallucinogenic drug.
- Benzodiazepines: Medications that act as sedatives, such as diazepam (Valium) or alprazolam (Xanax).
- Barbiturates: Central nervous system depressants.
- Methamphetamines: Stimulant drugs, including methamphetamine.

The 8-panel drug test is employed in various settings, including workplace drug testing, probation and parole programs, and other situations where a comprehensive screening for a broad range of substances is necessary. As always, the specific substances included in a drug test can be tailored to meet the needs and concerns of the organization conducting the test.
""")
    },
    {
        "name": "9 Panel Urine",
        "price": 85,
        "about": ("""
A 9-panel drug test is a type of drug screening that checks for the presence of nine different drugs or classes of drugs in a person's system. The specific substances included in a 9-panel drug test can vary based on the testing requirements of the organization or entity conducting the test. However, a typical 9-panel drug test often covers a broad spectrum of drugs, including those commonly abused.

A standard 9-panel drug test often includes:

- Marijuana (THC): Cannabis or marijuana.
- Cocaine: A powerful stimulant drug.
- Opiates: This category includes drugs like heroin and prescription opioids.
- Amphetamines: Stimulant drugs affecting the central nervous system.
- Phencyclidine (PCP): A hallucinogenic drug.
- Benzodiazepines: Medications that act as sedatives, such as diazepam (Valium) or alprazolam (Xanax).
- Barbiturates: Central nervous system depressants.
- Methamphetamines: Stimulant drugs, including methamphetamine.
- Methadone: A synthetic opioid often used in the treatment of opioid addiction.

The 9-panel drug test is utilized in various settings, including workplace drug testing, probation and parole programs, and other situations where a comprehensive screening for a wide range of substances is necessary. It's important to note that the specific substances included in a drug test can be customized based on the needs and concerns of the organization conducting the test.
""")
    }
]

# Insert or update panels for "Popular Tests"
for panel_data in panels_data:
    DrugPanel.objects.update_or_create(
        sub_category=sub_category,
        name=panel_data["name"],
        defaults={'about': panel_data["about"], 'price': panel_data["price"]},
    )

print("Popular Test Panels have been populated successfully.")

