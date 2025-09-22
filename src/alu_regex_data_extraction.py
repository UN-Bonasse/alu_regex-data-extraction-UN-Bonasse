"""
ALU Regex Data Extraction — UN-Bonasse

This file contains functions to extract structured data from text
using regular expressions (regex).

Data types:
- Emails
- URLs
- Phone numbers
- Credit card numbers
- Times (12-hour and 24-hour)
- HTML tags
- Hashtags
- Currency amounts
"""

import re

# ------------------------------
# EMAIL EXTRACTION
# ------------------------------
def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)


# ------------------------------
# URL EXTRACTION (improved)
# ------------------------------
def extract_urls(text):
    """
    Extract URLs but avoid capturing common trailing punctuation like commas,
    periods, closing parentheses, quotes, etc. Also normalize by stripping
    any leftover trailing punctuation from matches.
    """
    # don't include spaces or common trailing punctuation in the match
    url_pattern = r'https?://[^\s\)\]\}\>,"]+'
    matches = re.findall(url_pattern, text)

    # Defensive cleanup: remove trailing punctuation that might still remain
    cleaned = [m.rstrip('.,;:)]}>\'"') for m in matches]
    return cleaned



# ------------------------------
# PHONE NUMBER EXTRACTION
# ------------------------------
def extract_phone_numbers(text):
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(phone_pattern, text)


# ------------------------------
# CREDIT CARD EXTRACTION
# ------------------------------
def extract_credit_cards(text):
    credit_card_pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
    return re.findall(credit_card_pattern, text)


# ------------------------------
# TIME EXTRACTION
# ------------------------------
def extract_times(text):
    # 12-hour and 24-hour formats
    time_pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'
    return re.findall(time_pattern, text)


# ------------------------------
# HTML TAG EXTRACTION
# ------------------------------
def extract_html_tags(text):
    html_pattern = r'<[^>]+>'
    return re.findall(html_pattern, text)


# ------------------------------
# HASHTAG EXTRACTION
# ------------------------------
def extract_hashtags(text):
    hashtag_pattern = r'#\w+'
    return re.findall(hashtag_pattern, text)


# ------------------------------
# CURRENCY EXTRACTION
# ------------------------------
def extract_currency(text):
    currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(currency_pattern, text)


# ------------------------------
# DEMO / TEST RUN
# ------------------------------
if __name__ == "__main__":
    sample_text = """
    Emails: user@example.com, first.last@company.co.uk
    URLs: https://www.example.com, https://sub.example.org/page
    Phones: (123) 456-7890, 123-456-7890, 123.456.7890
    Credit Cards: 1234 5678 9012 3456, 1234-5678-9012-3456
    Times: 14:30, 2:30 PM
    HTML: <p>, <div class="example">, <img src="image.jpg" alt="desc">
    Hashtags: #example, #ThisIsAHashtag
    Currency: $19.99, $1,234.56
    """

    print("Emails found:", extract_emails(sample_text))
    print("URLs found:", extract_urls(sample_text))
    print("Phone numbers found:", extract_phone_numbers(sample_text))
    print("Credit cards found:", extract_credit_cards(sample_text))
    print("Times found:", extract_times(sample_text))
    print("HTML tags found:", extract_html_tags(sample_text))
    print("Hashtags found:", extract_hashtags(sample_text))
    print("Currency amounts found:", extract_currency(sample_text))
