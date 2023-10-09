import spacy

# Load the large English NER model
nlp = spacy.load("en_core_web_sm")

# Define a function to capture the information from text using Named Entity Recognition
def extract_info_3(text, first_names, last_names, addresses, phones, dates_of_birth):
    # Initialize variables to store extracted information
    first_name = ""
    last_name = ""
    address = ""
    phone = ""
    date_of_birth = ""

    # Process the text with spaCy NER model
    doc = nlp(text)

    # Extract the information using Named Entity Recognition
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            # Check if the entity text is a first name
            if not first_name:
                first_name = ent.text.strip()
            else:
                # If we already have a first name, assume the current entity is the last name
                last_name = ent.text.strip()
        elif ent.label_ == "GPE":
            # GPE represents geographical entities, which could include addresses
            address = ent.text.strip()
        elif ent.label_ == "PHONE":
            # PHONE entity type (custom) for phone numbers
            phone = ent.text.strip()
        elif ent.label_ == "DATE":
            # DATE entity type for dates, which could include date of birth
            date_of_birth = ent.text.strip()

    # Append the extracted information to the pre-defined lists
    first_names.append(first_name)
    last_names.append(last_name)
    addresses.append(address)
    phones.append(phone)
    dates_of_birth.append(date_of_birth)
