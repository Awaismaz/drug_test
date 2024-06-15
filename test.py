from zeep import Client

# Path to the WSDL file (update with the correct path)
wsdl_path = "LabcorpOTS.wsdl"

# Create a SOAP client using Zeep
client = Client(wsdl=wsdl_path)

# Example: Calling the Locate Collection Sites API
# Replace 'your_zip_code' with the actual zip code
response = client.service.locateCollectionSites(userId='ESITESTING', password='Solutions4mee!', zip='10001', distance=99)
# response = client.service.changePassword(userId='ESITESTING', password='solutions4me', newPassword='Solutions4mee!')


# Process the response
# The exact processing will depend on the structure of the response
print(response)
