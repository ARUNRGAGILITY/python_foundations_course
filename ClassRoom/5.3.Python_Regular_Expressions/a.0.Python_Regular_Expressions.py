# Python Regular Expressions

'''
Basic pattern matching.
Using character sets to match a range of characters.
Predefined character classes for digits, whitespaces, etc.
Quantifiers to specify the number of occurrences.
Wildcard and dot (.) character.
Grouping patterns and using alternation.
Anchors for start and end of strings.
Escaping special characters.
Non-capturing groups, positive lookaheads, and lookbehinds.
Flags for case-insensitive and multiline matching.
'''

import re

# Basic Patterns
match = re.search('hello', 'hello world!')
print("Basic Pattern:", match.group() if match else 'Not found')

# Character Sets
match = re.search('h[aeiou]llo', 'hello world!')
print("Character Set:", match.group() if match else 'Not found')

# Predefined Character Classes
digits = re.findall('\d', 'abc123def')
print("Digits:", digits)

# Quantifiers
multiple_as = re.search('a{2,4}', 'aaaabc')  # Matches between 2 to 4 'a's
print("Quantifiers:", multiple_as.group() if multiple_as else 'Not found')

# Wildcard
wildcard = re.search('a.b', 'acb')  # Matches any character between 'a' and 'b'
print("Wildcard:", wildcard.group() if wildcard else 'Not found')

# Groups
group = re.search('(abc){2}', 'abcabc')
print("Groups:", group.group() if group else 'Not found')

# Alternation
alternation = re.search('cat|dog', 'I have a cat')
print("Alternation:", alternation.group() if alternation else 'Not found')

# Anchors
start = re.search('^start', 'start here')  # Checks if string starts with 'start'
end = re.search('end$', 'at the end')      # Checks if string ends with 'end'
print("Anchors - Start:", start.group() if start else 'Not found')
print("Anchors - End:", end.group() if end else 'Not found')

# Escaping Special Characters
escape = re.search('\$\d+', '$100')  # Escaping dollar sign
print("Escape Special Char:", escape.group() if escape else 'Not found')

# Non-capturing Groups and Lookarounds
non_capturing = re.search('(?:abc){2}', 'abcabc')  # Non-capturing group
lookahead = re.search('Windows(?=95|98|NT|2000)', 'Windows2000')  # Positive lookahead
lookbehind = re.search('(?<=95|98|NT|2000)Windows', '2000Windows')  # Positive lookbehind
print("Non-capturing Group:", non_capturing.group() if non_capturing else 'Not found')
print("Lookahead:", lookahead.group() if lookahead else 'Not found')
print("Lookbehind:", lookbehind.group() if lookbehind else 'Not found')

# Flags
case_insensitive = re.search('python', 'Python', re.IGNORECASE)  # Case-insensitive search
multiline = re.search('^start', 'no match\nstart here', re.MULTILINE)  # Multiline search
print("Flag - Case Insensitive:", case_insensitive.group() if case_insensitive else 'Not found')
print("Flag - Multiline:", multiline.group() if multiline else 'Not found')


# Validating email address with Regular expression Pattern
# re.match
import re
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
email = "example@example.com"

if re.match(email_pattern, email):
    print("Valid email")
else:
    print("Invalid email")
# output: Valid email

# Extracting the date text using re.findall()
text = "The event will take place on 12-05-2024. Another event on 15-06-2024."
dates = re.findall(r'\d{2}-\d{2}-\d{4}', text)
print(dates)  # Output: ['12-05-2024', '15-06-2024']
# output: ['12-05-2024', '15-06-2024']

# Splitting a string with pattern and re.split()
text = "Hello, world! How are you doing? Good, I hope."
words = re.split(r'[,.!?]\s*', text)
print(words)
# output: ['Hello', 'world', 'How are you doing', 'Good', 'I hope', '']

import re
log_entry = "Error:FileNotFound; User:JohnDoe, Date:2023-04-01 Time:14:33"
# Pattern matches a comma, semicolon, or space
pattern = r"[,; ]+"
# Splitting the log entry based on the pattern
entries = re.split(pattern, log_entry)
print(entries)
# output: ['Error:FileNotFound', 'User:JohnDoe', 'Date:2023-04-01', 'Time:14:33']

# sensitive emails are changed, before this information is shared
# redacting
import re

text_with_emails = "Contact us at support@example.com or feedback@example.org for more info."
# Pattern to match email addresses
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Replacing email addresses with '<redacted>'
anonymized_text = re.sub(email_pattern, '<redacted>', text_with_emails)
print(anonymized_text)
# Contact us at <redacted> or <redacted> for more info.


# matching html tags
html = "<div>Hello, world!</div><p>This is a paragraph.</p>"
tags = re.findall(r"<(\w+)>", html)
print(tags)  # Output: ['div', 'p']

# extracting url from text
text = "Check out https://example.com and http://example.org for more info."
urls = re.findall(r"https?://[^\s]+", text)
print(urls)  # Output: ['https://example.com', 'http://example.org']

# finding hashtags in tweet
tweet = "This is a #sample tweet with #hashtags."
hashtags = re.findall(r"#(\w+)", tweet)
print(hashtags)  # Output: ['sample', 'hashtags']

# validating password length
password = "SecurePass123"
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

if re.match(pattern, password):
    print("Password is strong.")
else:
    print("Password is weak.")

# extracting phone numbers
