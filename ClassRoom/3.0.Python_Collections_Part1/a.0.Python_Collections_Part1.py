# Python Collections Part1

'''
Python Collections Module
1. Counters
2. DefaultDict
3. OrderedDict
4. ChainMap
5. NamedTuple
6. DeQue
7. UserList
8. UserString
9. UserDict

'''

from collections import Counter, defaultdict, OrderedDict
from collections import namedtuple, deque, ChainMap, UserDict, UserList, UserString

# Counter
# A Counter is a dict subclass for counting hashable objects.
counter = Counter(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])
print(counter)  # Counter({'apple': 2, 'orange': 2, 'pear': 1, 'banana': 1})

# defaultdict
# A defaultdict works exactly like a regular dict, but it is initialized with a function (“default factory”) that takes no arguments and provides the default value for a nonexistent key.
default_dict = defaultdict(int)
default_dict['apple'] += 1
print(default_dict)  # defaultdict(<class 'int'>, {'apple': 1})

# OrderedDict
# An OrderedDict is a dict that remembers the order that keys were first inserted.
ordered_dict = OrderedDict()
ordered_dict['banana'] = 2
ordered_dict['apple'] = 4
ordered_dict['pear'] = 1
print(ordered_dict)  # OrderedDict([('banana', 2), ('apple', 4), ('pear', 1)])

# ChainMap
# A ChainMap groups multiple dictionaries into a single mapping.
dict1 = {'apple': 1, 'banana': 2}
dict2 = {'orange': 3, 'apple': 4}
chain_map = ChainMap(dict1, dict2)
print(chain_map)  # ChainMap({'apple': 1, 'banana': 2}, {'orange': 3, 'apple': 4})

# namedtuple
# namedtuple factory function for creating tuple subclasses with named fields.
Point = namedtuple('Point', ['x', 'y'])
point = Point(11, y=22)
print(point)  # Point(x=11, y=22)

# deque
# deque is a list optimized for inserting and removing items.
deq = deque([1, 2, 3])
deq.appendleft(0)
deq.append(4)
print(deq)  # deque([0, 1, 2, 3, 4])

# UserList
# UserList is a wrapper around list objects for easier list subclassing.
user_list = UserList([1, 2, 3])
user_list.append(4)
print(user_list)  # [1, 2, 3, 4]

# UserString
# UserString is a wrapper around string objects for easier string subclassing.
user_string = UserString("Python")
print(user_string)  # Python

# UserDict
# UserDict is a wrapper around dictionary objects for easier dict subclassing.
user_dict = UserDict({'apple': 1, 'banana': 2})
user_dict['pear'] = 3
print(user_dict)  # {'apple': 1, 'banana': 2, 'pear': 3}

