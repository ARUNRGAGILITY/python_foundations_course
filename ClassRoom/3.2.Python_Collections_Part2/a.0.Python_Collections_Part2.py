# Python Collection Part2 

from collections import UserList, UserString, UserDict

# UserList
# UserList is a class that acts like a Python list but can be easily subclassed.
# It is useful when you want to create a new list type that has some added functionality.
class MyList(UserList):
    # Example of adding a method to clear all elements from the list
    def clear_all(self):
        self.data.clear()

my_list = MyList([1, 2, 3])
my_list.append(4)  # Works like a regular list
my_list.clear_all()  # Now the list is empty
print("MyList:", my_list)  # MyList: []

# UserString
# UserString is a class that acts like a Python string but can be easily subclassed.
# It is useful when you want to create a new string type with added functionality.
class MyString(UserString):
    # Example of adding a method to reverse the string
    def reverse(self):
        self.data = self.data[::-1]

my_string = MyString("Hello")
my_string.reverse()  # The string is now reversed
print("MyString:", my_string)  # MyString: olleH

# UserDict
# UserDict is a class that acts like a Python dictionary but can be easily subclassed.
# It is useful for creating a new dictionary type with added functionality.
class MyDict(UserDict):
    # Example of adding a method to get keys as a list
    def keys_list(self):
        return list(self.keys())

my_dict = MyDict({'a': 1, 'b': 2})
my_dict['c'] = 3  # Works like a regular dictionary
keys = my_dict.keys_list()  # Now we can get keys as a list
print("MyDict keys:", keys)  # MyDict keys: ['a', 'b', 'c']


# Few extensions to basic List, String and Dictionary using
# UserList, UserString and UserDict

from collections import UserList, UserString, UserDict

# MyList extends UserList
class MyList(UserList):
    
    def clear_all(self):
        """Remove all items from the list."""
        self.data.clear()

    def multiply(self, factor):
        """Multiply all numerical items by the given factor."""
        for i in range(len(self.data)):
            self.data[i] *= factor

    def info(self):
        """Return a summary of the list."""
        return f"MyList with {len(self.data)} items."

my_list = MyList([1, 2, 3])
my_list.multiply(2)  # Multiplies each item by 2: [2, 4, 6]
info = my_list.info()  # Gets summary info
print(info)  # MyList with 3 items.

# MyString extends UserString
class MyString(UserString):

    def reverse(self):
        """Reverse the string."""
        self.data = self.data[::-1]

    def is_palindrome(self):
        """Check if the string is a palindrome."""
        return self.data == self.data[::-1]

    def append(self, suffix):
        """Append a suffix to the string."""
        self.data = self.data + suffix

my_string = MyString("level")
print(my_string.is_palindrome())  # True, since "level" is a palindrome
my_string.append("_suffix")
print(my_string)  # level_suffix

# MyDict extends UserDict
class MyDict(UserDict):

    def keys_list(self):
        """Return the keys of the dictionary as a list."""
        return list(self.keys())

    def values_sum(self):
        """Return the sum of the values in the dictionary."""
        return sum(self.values())

    def invert(self):
        """Invert the dictionary to create a new dictionary with values as keys."""
        self.data = {value: key for key, value in self.data.items()}

my_dict = MyDict({'a': 1, 'b': 2, 'c': 3})
total = my_dict.values_sum()  # Returns the sum of the values: 6
my_dict.invert()  # Inverts the dictionary: {1: 'a', 2: 'b', 3: 'c'}
print("Inverted MyDict:", my_dict)  # Inverted MyDict: {1: 'a', 2: 'b', 3: 'c'}
