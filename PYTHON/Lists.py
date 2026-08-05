#Creating lists
nums = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
empty = []
nested = [[1, 2], [3, 4]]

#Indexing and Slicing
nums = [10, 20, 30, 40, 50]

print(nums[0])       # 10
print(nums[-1])      # 50
print(nums[1:3])     # [20, 30]
print(nums[:3])       # [10, 20, 30]
print(nums[::-1])     # [50, 40, 30, 20, 10] — reversed
print(nums[::2])      # [10, 30, 50] — step of 2

#Lists are mutable
nums = [1, 2, 3]
nums[0] = 100
print(nums)   # [100, 2, 3] — modified in place, no new object created

#Common list methods
nums = [3, 1, 4, 1, 5]

nums.append(9)         # [3, 1, 4, 1, 5, 9] — add to end
nums.insert(0, 100)    # [100, 3, 1, 4, 1, 5, 9] — insert at index
nums.remove(1)         # removes FIRST occurrence of value 1
nums.pop()             # removes and RETURNS last item
nums.pop(0)            # removes and returns item at index 0
nums.sort()             # sorts in place
nums.sort(reverse=True) # descending
nums.reverse()          # reverses in place
nums.count(1)            # counts occurrences of 1
nums.index(4)             # returns index of first occurrence of 4
nums.extend([6, 7])       # appends multiple items
nums.clear()               # empties the list

#sort() vs sorted()
nums = [3, 1, 2]
nums.sort()          # modifies nums in place, returns None
new_list = sorted(nums)  # returns a new sorted list, original unaffected (works on any iterable)

#List comprehensions
#Structure: [expression for item in iterable if condition]
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# with transformation + condition
result = [x*2 if x % 2 == 0 else x for x in range(5)]
# [0, 1, 4, 3, 8]

#Nested list comprehensions
matrix = [[1, 2], [3, 4]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4]

#Copying lists
a = [1, 2, 3]
b = a              # ❌ same object — modifying b modifies a too
b = a.copy()        # ✅ shallow copy — new list, but nested objects still shared
b = a[:]             # ✅ another way to shallow copy
import copy
b = copy.deepcopy(a)  # ✅ true independent copy, including nested lists

#Checking membership and length
nums = [1, 2, 3]
print(2 in nums)     # True
print(len(nums))      # 3


#Unpacking
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4]   # first=1, rest=[2, 3, 4]


#Shallow copy trap with nested lists
#.copy() and [:] only copy the outer list — inner lists are still shared references. Only copy.deepcopy() truly separates everything.
a = [[1, 2], [3, 4]]
b = a.copy()          # shallow copy
b[0][0] = 100
print(a)               # [[100, 2], [3, 4]] — a changed too!

#List as a stack and queue
# Stack (LIFO) — use append/pop, both O(1)
stack = []
stack.append(1)
stack.append(2)
stack.pop()      # removes 2

# Queue (FIFO) — pop(0) is O(n), inefficient for large lists
from collections import deque
queue = deque()
queue.append(1)
queue.popleft()   # O(1) — proper way to do queues in Python


#+ vs extend() vs append()
a = [1, 2]
a.append([3, 4])    # [1, 2, [3, 4]] — adds the list AS ONE ELEMENT
a.extend([3, 4])     # [1, 2, 3, 4]  — adds each element individually
b = a + [5, 6]         # creates a NEW list, doesn't modify a


#List multiplication trap with nested lists
grid = [[0] * 3] * 3   # looks like a 3x3 grid, but...
grid[0][0] = 1
print(grid)   # [[1,0,0],[1,0,0],[1,0,0]] — all rows are the SAME object!

# Correct way
grid = [[0] * 3 for _ in range(3)]   # each row is independently created


#Time complexity summary
#append()     # O(1)
#pop()          # O(1) from end, O(n) from front/middle
#insert(0, x)  # O(n) — shifts everything
#in (membership) # O(n) — linear search
#len()          # O(1)
#sort()          # O(n log n)