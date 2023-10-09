# Import Regular Expression
import re

# Define a function to capture the information from text file using Regular Expression
def extract_info_2(text, first_names, last_names, addresses, phones, dates_of_birth):
    # RULES
    # Address pattern
    # example: 123 Main St, Toronto, ON, M4B 1B3
    address_pattern = re.compile(r"""
        # Match the street address, which may include house/apartment number, street name, and street type
        (\d+\s+\b[A-Z][a-z]+\b\s+\b[A-Z][a-z]+\b)
        \s*,\s*
        # Match the city, which should start with an uppercase letter
        ([A-Z][a-z]+)\s*,\s*
        # Match the province abbreviation, which should be two uppercase letters
        (ON)\s*
        # Match the postal code, which should be formatted as A1A 1A1
        (\b[A-Z]\d[A-Z]\s?\d[A-Z]\d\b)
        """, re.VERBOSE)

    # Phone number pattern
    # example: (123) 456-7890 or 123-456-7890 or 1234567890 or these phones with +1
    phone_pattern = re.compile(r"""
        (?:
            # match a phone number starting with the country code (1)
            1\s*[\.-]?\s*\(?(\d{3})\)?[\.-]?\s*(\d{3})[\.-]?\s*(\d{4})
            |
            # match a phone number without the country code
            \(?(\d{3})\)?[\.-]?\s*(\d{3})[\.-]?\s*(\d{4})
        )
        """, re.VERBOSE)

    dob_pattern = re.compile(r"""
        # Match dates in the format YYYY-MM-DD
        (\d{4})-(\d{2})-(\d{2})
        |
        # Match dates in the format MTH DD, YYYY
        (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{1,2}),\s+(\d{4})
        |
        # Match dates in the format Month DD YYYY
        (January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})\s+(\d{4})
        """, re.VERBOSE)

    # Extract information using the new regex patterns
    address_matches = address_pattern.findall(text)
    if address_matches:
        addresses.extend(address_matches)

    phone_matches = phone_pattern.findall(text)
    if phone_matches:
        phones.extend(["-".join(filter(None, match)) for match in phone_matches])

    dob_matches = dob_pattern.findall(text)
    if dob_matches:
        dates_of_birth.extend(["-".join(filter(None, match)) for match in dob_matches])


# Apply function
extract_info_2(text, first_names, last_names, addresses, phones, dates_of_birth)
