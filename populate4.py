import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from drugtest.models import DrugSubCategory, DrugPanel


# Ensure the "Instant Urine Drug Tests" subcategory exists
sub_category_name = "Instant Urine Drug Tests"
sub_category, created = DrugSubCategory.objects.get_or_create(name=sub_category_name)

# Panels data for "Instant Urine Drug Tests"
panels_data = [
    {
        "name": "Instant 5 Panel",
        "about": """
A 5-panel instant drug test typically refers to a drug test that screens for the presence of five commonly abused substances. The term "panel" in drug testing refers to the number of drugs or drug classes being tested for. A 5-panel test usually includes screening for the following substances:

- Cocaine: Cocaine is a stimulant drug that can lead to increased energy, alertness, and euphoria. It is derived from the coca plant.

- Amphetamines/Methamphetamines: Amphetamines and methamphetamines are stimulant drugs that can enhance focus, energy, and alertness. They are often used recreationally.

- Opiates (such as heroin, morphine, and codeine): Opiates are drugs derived from the opium poppy plant, and they can have pain-relieving and sedative effects. Heroin, morphine, and codeine are examples.

- Phencyclidine (PCP): PCP is a hallucinogenic drug that can cause dissociation, hallucinations, and altered perceptions of reality.

- Marijuana (THC): Marijuana, or cannabis, contains the psychoactive compound tetrahydrocannabinol (THC), which can cause euphoria, relaxation, and altered perception.

These tests are often used by employers, law enforcement, and other organizations to quickly screen individuals for drug use. The "instant" aspect of the test implies that results are available shortly after the test is conducted, typically within a few minutes.

It's important to note that drug testing procedures and panels can vary, and there are also tests with a higher number of panels (e.g., 10-panel or 12-panel tests) that screen for a broader range of substances. The choice of the panel depends on the specific requirements of the testing organization.
        """,
        "price": 75
    },
    {
        "name": "Instant 7 Panel xCup",
        "about": """
The "xCup" likely refers to a specific brand or type of drug testing cup that is designed for quick and convenient on-site drug testing. The "7 Panel" designation indicates that the cup is configured to test for the presence of seven different drugs or drug classes. While the specific drugs included can vary, a typical 7-panel drug test might include screening for substances such as:

- Cocaine
- Amphetamines/Methamphetamines
- Opiates (such as heroin, morphine, and codeine)
- Phencyclidine (PCP)
- Marijuana (THC)
- Benzodiazepines
- Methadone

Keep in mind that the composition of a 7-panel test can vary, and additional substances like barbiturates or synthetic opioids may also be included depending on the specific requirements of the testing organization.

The "instant" nature of these tests implies that results are typically available within a few minutes after the test is conducted. These types of drug testing cups are often used in workplaces, clinics, or other settings where rapid and on-site drug screening is needed. It's crucial to follow the manufacturer's instructions for proper use and interpretation of the results.
        """,
        "price": 95
    },
    {
        "name": "Instant 9 Panel",
        "about": """
A 9-panel drug test is a screening tool designed to detect the presence of nine different drugs or drug classes in a person's system. This type of drug test is often used for employment, legal, or healthcare purposes to assess a broader range of substances. The specific drugs included in a 9-panel drug test can vary, but a common configuration may typically screen for:

- Cocaine
- Amphetamines/Methamphetamines
- Opiates (such as heroin, morphine, and codeine)
- Phencyclidine (PCP)
- Marijuana (THC)
- Benzodiazepines
- Barbiturates
- Methadone
- Propoxyphene

It's important to note that the composition of a 9-panel test can vary among different testing providers or manufacturers. Some tests may include additional drugs, such as synthetic opioids or hallucinogens, depending on the testing requirements.

As with other drug tests, the "instant" aspect indicates that the results are typically available shortly after the test is conducted, usually within a few minutes. The testing process often involves using a single device or test kit that is capable of simultaneously screening for multiple substances. Users should carefully follow the instructions provided by the manufacturer for accurate and reliable results.
        """,
        "price": 89
    },
    {
        "name": "Instant 10 Panel xCup",
        "about": """
A 10-panel xCup refers to a specific type of drug testing cup designed to screen for the presence of ten different drugs or drug classes. The "xCup" likely represents a brand or model name for a specific type of drug testing cup, and the "10 Panel" designation indicates the number of substances being tested for. The specific drugs included in a 10-panel drug test can vary, but a common configuration may typically include:

- Amphetamines (AMP)
- Barbiturates (BAR)
- Benzodiazepines (BZO)
- Buprenorphine (BUP)
- Cocaine (COC)
- Marijuana (THC)
- Methadone (MTD)
- Methamphetamine (MET)
- Opiates (OPI)
- Phencyclidine (PCP)

These tests are often used in various settings, including workplaces, healthcare, and legal situations, where a more comprehensive screening for a broader range of substances is required. The "instant" nature of these tests suggests that results are typically available within a few minutes after the test is conducted, providing a quick and convenient way to screen individuals for drug use on-site.

As with any drug testing product, it's important to follow the manufacturer's instructions carefully to ensure accurate and reliable results. The specific drugs included and the sensitivity of the test may vary based on the product and manufacturer.
        """,
        "price": 125
    },
]

# Insert or update panels for "Instant Urine Drug Tests"
for panel_data in panels_data:
    DrugPanel.objects.update_or_create(
        sub_category=sub_category,
        name=panel_data["name"],
        defaults={'about': panel_data["about"], 'price': panel_data["price"]},
    )

print("Instant Urine Drug Panels have been populated successfully.")
