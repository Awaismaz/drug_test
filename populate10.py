import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from drugtest.models import DrugSubCategory, DrugPanel

# Ensure the "DNA Testing" subcategory exists
dna_testing_sub_category_name = "DNA Testing"
dna_testing_sub_category, created = DrugSubCategory.objects.get_or_create(name=dna_testing_sub_category_name)

# New panels data
dna_testing_panels_data = [
    {
        "name": "Legal DNA Test",
        "about": """
A legal paternity test is a type of DNA test used to determine the biological relationship between a man and a child, typically for legal purposes such as establishing parental rights, child support obligations, inheritance claims, or immigration cases. Unlike a home paternity test, which may not be admissible in court, a legal paternity test must adhere to specific guidelines and requirements to ensure its validity and acceptability in legal proceedings.

Here are some key features of a legal paternity test:

- Chain of custody: A legal paternity test requires strict adherence to a chain of custody procedure to document the handling and transfer of the DNA samples from collection to testing. This ensures the integrity and reliability of the results.
- Certified collection: DNA samples must be collected by a trained and certified professional, such as a phlebotomist or a healthcare provider, to ensure proper collection procedures and maintain the chain of custody.
- Identification verification: Both the alleged father and child (and sometimes the mother) must provide valid identification at the time of sample collection to confirm their identities.
- Documentation: Detailed documentation, including consent forms, identification records, and chain of custody documentation, must accompany the DNA samples throughout the testing process.
- Accredited laboratory: The DNA testing must be performed by an accredited laboratory using validated testing methods and equipment to ensure accurate and reliable results.
- Court-admissible results: The results of a legal paternity test are typically admissible in court and can be used as evidence to establish legal paternity or to support legal proceedings related to paternity, such as child support or custody cases.

It's important to note that the requirements for legal paternity testing may vary by jurisdiction, so it's advisable to consult with an attorney or legal expert familiar with the laws and regulations in your area if you require a legal paternity test for a specific purpose.
        """,
        "price": 350
    },
    {
        "name": "Home DNA Test",
        "about": """
A home DNA test is a convenient and accessible option for individuals who wish to determine biological relationships or explore their genetic ancestry without involving healthcare professionals or visiting a laboratory. Not valid in court. These tests typically involve collecting DNA samples at home using a simple kit provided by the testing company. Here's how a home DNA test generally works:

- Ordering the test: Individuals can order a home DNA test online or purchase it from a retail store. The test kit typically includes instructions, collection materials, and a prepaid return envelope.
- Sample collection: The individual follows the instructions provided in the kit to collect DNA samples, usually by swabbing the inside of the cheek to collect saliva or using a saliva collection tube provided in the kit. Some tests may require blood samples obtained through a finger prick.
- Registering the kit: Many home DNA testing companies require users to register their test kit online before sending in the samples. This registration process typically involves providing personal information and a unique identifier found on the kit.
- Returning the samples: After collecting the samples, they are placed in the provided containers or envelopes and sent back to the testing company using the prepaid return envelope.
- Analysis: Once the samples reach the testing laboratory, the DNA is extracted and analyzed to determine genetic information. Depending on the type of test, the analysis may focus on specific genetic markers related to ancestry, paternity/maternity, health predispositions, or traits.
- Results: The individual receives the results of the DNA test typically within a few weeks, either through an online portal or mailed report. The results may include information about genetic ancestry, biological relationships, health traits, or predispositions to certain health conditions, depending on the type of test ordered.

It's important to note that while home DNA tests can provide valuable information, they may have limitations compared to tests conducted by healthcare professionals or in accredited laboratories. Factors such as sample quality, testing methods, and interpretation of results may vary between different testing companies. Additionally, individuals should carefully consider privacy concerns and the potential emotional implications of DNA testing before deciding to proceed with a home DNA test.
        """,
        "price": 210
    },
]

# Insert or update panels
for panel in dna_testing_panels_data:
    obj, created = DrugPanel.objects.update_or_create(
        sub_category=dna_testing_sub_category,
        name=panel['name'],
        defaults={'about': panel['about'], 'price': panel['price']},
    )

print("DNA Testing panels have been populated successfully.")
