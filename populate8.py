import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from drugtest.models import DrugSubCategory, DrugPanel

# Ensure the "DOT Drug Tests" subcategory exists
dot_sub_category_name = "DOT Drug Tests"
dot_sub_category, created = DrugSubCategory.objects.get_or_create(name=dot_sub_category_name)

# New panels data
dot_panels_data = [
    {
        "name": "DOT Drug Test",
        "about": """
A DOT drug test refers to a drug test that adheres to the regulations set forth by the U.S. Department of Transportation (DOT). These regulations mandate drug testing for individuals working in safety-sensitive positions within transportation industries such as aviation, trucking, railroads, mass transit, pipelines, and maritime.

DOT drug tests typically screen for the following substances:

- Marijuana (THC)
- Cocaine
- Amphetamines
- Opiates
- Phencyclidine (PCP)
- Ecstasy
- Expanded Opiates

The testing process usually involves urine sample collection and laboratory analysis. Employers subject to DOT regulations must follow specific protocols outlined by the DOT, including chain of custody procedures and laboratory accreditation requirements. The purpose of these drug tests is to ensure the safety of transportation operations by identifying and deterring drug use among employees who perform safety-sensitive duties.
        """,
        "price": 55
    },
    {
        "name": "DOT BAT",
        "about": """
A DOT BAT refers to a Breath Alcohol Technician certified by the U.S. Department of Transportation (DOT). These technicians are responsible for administering breath alcohol tests to individuals working in safety-sensitive positions within transportation industries, such as aviation, trucking, railroads, mass transit, pipelines, and maritime.

DOT BATs are trained and certified to conduct breath alcohol testing in accordance with DOT regulations, which include specific procedures for breathalyzer equipment calibration, testing protocols, and documentation requirements. They must adhere strictly to these regulations to ensure the accuracy and reliability of the test results.

Breath alcohol testing is conducted to detect the presence of alcohol in an individual's system, which could impair their ability to perform safety-sensitive duties. The DOT has set legal limits for alcohol concentration in breath for safety-sensitive employees, and testing positive above these limits can result in disciplinary action, including removal from safety-sensitive duties and possible termination.
        """,
        "price": 75
    },
    {
        "name": "USCG Drug Test",
        "about": """
A USCG drug test is a drug test conducted under the authority of the United States Coast Guard (USCG). Similar to the DOT drug test, the USCG drug test is designed to detect the presence of illegal drugs or controlled substances in individuals who hold positions within the maritime industry that are regulated by the USCG.

The USCG mandates drug testing for individuals working in safety-sensitive positions within the maritime industry, including commercial vessel operators, crew members, and other personnel who perform duties critical to maritime safety and security.

USCG drug tests typically screen for a standard panel of substances, including:

- Marijuana (THC)
- Cocaine
- Amphetamines
- Opiates
- Phencyclidine (PCP)
- Ecstasy
- Expanded Opiates

The testing process usually involves urine sample collection and laboratory analysis, following specific protocols outlined by the USCG. These protocols include chain of custody procedures, laboratory accreditation requirements, and strict adherence to testing guidelines to ensure the accuracy and reliability of test results.

The purpose of USCG drug testing is to maintain safety and security within the maritime industry by deterring and identifying drug use among personnel who hold safety-sensitive positions. Individuals who test positive for prohibited substances may face disciplinary action, including removal from safety-sensitive duties and possible termination.
        """,
        "price": 85
    },
    {
        "name": "DOT Physical",
        "about": """
A DOT physical, also known as a DOT medical examination or DOT physical exam, is a medical evaluation required by the U.S. Department of Transportation (DOT) for individuals seeking to obtain or maintain a commercial driver's license (CDL) or certain other positions regulated by the DOT.

The DOT physical is conducted by a certified medical examiner who assesses the individual's overall health and physical fitness to ensure they meet the medical standards set forth by the DOT. The purpose of the DOT physical is to ensure that commercial drivers and other safety-sensitive employees are medically fit to perform their duties safely.

During the DOT physical exam, the medical examiner typically evaluates the following:

- Medical history: The examiner reviews the individual's medical history, including any past illnesses, injuries, or surgeries.
- Physical examination: The examiner conducts a thorough physical examination, assessing vital signs, vision, hearing, reflexes, and overall physical fitness.
- Drug and alcohol testing: In addition to the physical examination, individuals may also be required to undergo drug and alcohol testing as part of the DOT physical.
- Medical conditions: The examiner evaluates any medical conditions that could affect the individual's ability to safely operate commercial vehicles, such as cardiovascular disease, diabetes, or respiratory issues.

After completing the examination, the medical examiner provides the individual with a Medical Examiner's Certificate (MEC), also known as a DOT medical card, if they meet the DOT's medical standards. This certificate is typically valid for a specific period, often two years, although shorter validity periods may be assigned if the individual has a medical condition that requires monitoring.

Overall, the DOT physical is an important component of ensuring the safety and health of commercial drivers and other safety-sensitive employees in transportation-related positions.
        """,
        "price": 149
    },
]

# Insert or update panels
for panel in dot_panels_data:
    obj, created = DrugPanel.objects.update_or_create(
        sub_category=dot_sub_category,
        name=panel['name'],
        defaults={'about': panel['about'], 'price': panel['price']},
    )

print("DOT panels have been populated successfully.")
