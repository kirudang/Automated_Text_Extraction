# Import Regular Expression
import re

# Create empty lists to store our data
first_names = []
last_names = []
addresses = []
phones = []
dates_of_birth = []

# Define a function to capture the information from text file using Regular Expression
def extract_info_1(text, first_names, last_names, addresses, phones, dates_of_birth):
    # Use regular expressions to search for the relevant information in the text
    Address_keys = ["Location", "Located at", "Address", "Residence", "Premises", "Residential address"]
    BOD_keys = ["Born on", "DOB", "Birth date", "Date of birth"]
    Phone_keys = ["Phone", "Telephone", "Contact number", "Call at", "Phone number", "Mobile number"]
    First_Name_keys = ["First name", "Given name", "First", "Given", "Tenant", "First and last name"]
    Last_Name_keys = ["Last name", "Family name", "Surname", "Last"]

    for keyword in Address_keys:
        matches = re.findall(keyword + "\s*:\s*(.*)", text, re.IGNORECASE)
        if matches:
            addresses.extend(matches)

    for keyword in BOD_keys:
        matches = re.findall(keyword + "\s*:\s*(.*)", text, re.IGNORECASE)
        if matches:
            dates_of_birth.extend(matches)

    for keyword in Phone_keys:
        matches = re.findall(keyword + "\s*:\s*(.*)", text, re.IGNORECASE)
        if matches:
            phones.extend(matches)

    for keyword in First_Name_keys:
        matches = re.findall(keyword + "\s*:\s*(.*)", text, re.IGNORECASE)
        if matches:
            first_names.extend(matches)

    for keyword in Last_Name_keys:
        matches = re.findall(keyword + "\s*:\s*(.*)", text, re.IGNORECASE)
        if matches:
            last_names.extend(matches)

# Apply function
extract_info_1(text, first_names, last_names, addresses, phones, dates_of_birth)
