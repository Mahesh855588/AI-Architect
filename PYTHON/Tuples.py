#Creating tuples
t = (1, 2, 3)
single = (5,)        # ⚠️ comma required — without it, (5) is just an int in parentheses
empty = ()
no_parens = 1, 2, 3   # parentheses are actually optional
#⚠️ Common trap: single = (5) is NOT a tuple — it's just 5. You need the trailing comma: (5,).

#Tuples are immutable
t = (1, 2, 3)
t[0] = 100   # ❌ TypeError — can't modify a tuple
#Once created, a tuple's contents can't change. This is the core distinction from lists.


#But — a tuple can contain mutable objects

t = (1, [2, 3])
t[1].append(4)
print(t)   # (1, [2, 3, 4]) — the LIST inside changed, tuple itself is still "immutable"
#The tuple's references can't be reassigned, but if an element is itself mutable (like a list), that element can still be modified internally.


#Indexing and slicing — same as lists
t = (10, 20, 30, 40)
print(t[0])       # 10
print(t[-1])      # 40
print(t[1:3])     # (20, 30)
print(t[::-1])    # (40, 30, 20, 10)

coords = {(0, 0): "origin", (1, 1): "diagonal"}  # ✅ tuple as dict key
coords2 = {[0, 0]: "origin"}  # ❌ TypeError — list isn't hashable
'''Why use tuples over lists?
Immutability = safer when you want to guarantee data doesn't change (e.g., fixed coordinates, config values)
Faster than lists for iteration and fixed data — less overhead since Python doesn't need to support resizing
Hashable (if all elements are hashable) — so tuples can be used as dictionary keys or set elements; lists cannot'''

#Tuple methods
t = (1, 2, 2, 3)
print(t.count(2))   # 2
print(t.index(3))   # 3
#That's it — no append, remove, sort, etc., since those would require mutation.


#Tuple unpacking
point = (3, 4)
x, y = point
print(x, y)   # 3 4

# Swapping values — classic Python idiom using tuples
a, b = 1, 2
a, b = b, a
print(a, b)   # 2 1


#Unpacking with *
t = (1, 2, 3, 4, 5)
first, *middle, last = t
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5


#Nested tuples
nested = ((1, 2), (3, 4))
print(nested[0][1])   # 2


#Converting between list and tuple
lst = [1, 2, 3]
t = tuple(lst)     # (1, 2, 3)
back_to_list = list(t)   # [1, 2, 3]


#Named tuples
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)   # 3 4 — access by name instead of index


#Tuple vs list
import sys
print(sys.getsizeof((1, 2, 3)))   # smaller
print(sys.getsizeof([1, 2, 3]))   # larger

#Tuple as function return value
def min_max(numbers):
    return min(numbers), max(numbers)   # returns a tuple implicitly

low, high = min_max([3, 1, 4, 1, 5])
print(low, high)   # 1 5


#Tuple concatenation and repetition
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)     # (1, 2, 3, 4) — creates a new tuple
print(t1 * 3)       # (1, 2, 1, 2, 1, 2)


#Comparing tuples
print((1, 2, 3) < (1, 2, 4))   # True — compares element by element
print((1, 2) < (1, 2, 3))       # True — shorter tuple is "less" if it's a prefix

#Why tuples matter for dictionaries/sets
# Multi-key lookup pattern — very common in real code
cache = {}
def compute(a, b):
    key = (a, b)
    if key not in cache:
        cache[key] = a * b
    return cache[key]
#This pattern (using a tuple as a composite dictionary key) shows up constantly in caching/memoization — directly relevant once you hit functools.lru_cache later in your list.
