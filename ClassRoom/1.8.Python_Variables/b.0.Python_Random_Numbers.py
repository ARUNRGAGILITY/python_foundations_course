import random
import string

# Random number generation

# Generate a random integer between 1 and 10
rand_int = random.randint(1, 10)
print("Random Integer between 1 and 10:", rand_int)  # Output: e.g., 7

# Generate a random float between 0 and 1
rand_float = random.random()
print("Random Float between 0 and 1:", rand_float)  # Output: e.g., 0.562321

# String manipulation based on random functions

# Generate a random string of specific length
length_of_string = 5
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length_of_string))
print("Randomly generated string:", random_string)  # Output: e.g., 'a3k9N'

# Shuffle a string
# Convert the string to a list, shuffle it, then rejoin back into a string
sample_string = "HelloWorld"
string_list = list(sample_string)
random.shuffle(string_list)
shuffled_string = ''.join(string_list)
print("Shuffled string:", shuffled_string)  # Output: e.g., 'rloHWlelod'

# Other Random Operations

# Choose a random element from a list
sample_list = ['apple', 'banana', 'cherry', 'date']
random_element = random.choice(sample_list)
print("Randomly selected element from list:", random_element)  # Output: e.g., 'banana'

# Generate a random sample of elements from a list
random_sample = random.sample(sample_list, 2)
print("Randomly selected sample from list:", random_sample)  # Output: e.g., ['date', 'apple']

# Generate a random number within a range using random.uniform()
# Generates a float number between 1 and 100
rand_uniform = random.uniform(1, 100)
print("Random Float between 1 and 100:", rand_uniform)  # Output: e.g., 55.67321

print("Random Float xx.yy between 1 and 100:", round(rand_uniform,2))  # Output: e.g., 55.67

# Note: Outputs will vary each time you run this code due to the nature of random number generation.
