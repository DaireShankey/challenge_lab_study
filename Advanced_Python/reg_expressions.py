# regex_example.py
import re

# Sample text
text = "Contact us at support@example.com or sales@example.com"

# Find all email addresses in the text
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print("Emails found:", emails)

# Replace all email addresses with a placeholder
masked_text = re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b', "[EMAIL]", text)
print("Masked text:", masked_text)
