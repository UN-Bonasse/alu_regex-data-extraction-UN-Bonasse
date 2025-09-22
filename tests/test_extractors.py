"""
Unit tests for ALU Regex Data Extraction — UN-Bonasse
"""

import pytest
from src.alu_regex_data_extraction import (
    extract_emails,
    extract_urls,
    extract_phone_numbers,
    extract_credit_cards,
    extract_times,
    extract_html_tags,
    extract_hashtags,
    extract_currency
)

# ------------------------------
# Sample text for testing
# ------------------------------
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

# ------------------------------
# TEST FUNCTIONS
# ------------------------------
def test_extract_emails():
    result = extract_emails(sample_text)
    assert "user@example.com" in result
    assert "first.last@company.co.uk" in result

def test_extract_urls():
    result = extract_urls(sample_text)
    assert "https://www.example.com" in result
    assert "https://sub.example.org/page" in result

def test_extract_phone_numbers():
    result = extract_phone_numbers(sample_text)
    assert "(123) 456-7890" in result
    assert "123-456-7890" in result
    assert "123.456.7890" in result

def test_extract_credit_cards():
    result = extract_credit_cards(sample_text)
    assert "1234 5678 9012 3456" in result
    assert "1234-5678-9012-3456" in result

def test_extract_times():
    result = extract_times(sample_text)
    assert "14:30" in result
    assert "2:30 PM" in result

def test_extract_html_tags():
    result = extract_html_tags(sample_text)
    assert "<p>" in result
    assert '<div class="example">' in result
    assert '<img src="image.jpg" alt="desc">' in result

def test_extract_hashtags():
    result = extract_hashtags(sample_text)
    assert "#example" in result
    assert "#ThisIsAHashtag" in result

def test_extract_currency():
    result = extract_currency(sample_text)
    assert "$19.99" in result
    assert "$1,234.56" in result

