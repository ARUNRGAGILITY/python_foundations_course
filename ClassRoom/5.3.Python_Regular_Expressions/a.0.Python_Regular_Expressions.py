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
