#Arithmetic Operators
a, b = 10, 3

print(a + b)   # 13  addition
print(a - b)   # 7   subtraction
print(a * b)   # 30  multiplication
print(a / b)   # 3.333...  true division (always float)
print(a // b)  # 3   floor division
print(a % b)   # 1   modulo (remainder)
print(a ** b)  # 1000  exponentiation

#Comparison Operators
print(a == b)  # False — equal to
print(a != b)  # True  — not equal to
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False

#Logical Operators
x = True
y = False

print(x and y)  # False — both must be True
print(x or y)   # True  — at least one True
print(not x)    # False — flips the value


#Assignment Operators
x = 5
x += 3   # x = x + 3  → 8
x -= 2   # x = x - 2  → 6
x *= 2   # x = x * 2  → 12
x /= 4   # x = x / 4  → 3.0
x //= 1  # floor divide in place
x **= 2  # power in place
x %= 5   # modulo in place


#Bitwise Operators
a, b = 5, 3   # binary: 101, 011

print(a & b)   # 1   AND
print(a | b)   # 7   OR
print(a ^ b)   # 6   XOR
print(~a)      # -6  NOT (inverts all bits)
print(a << 1)  # 10  left shift (multiply by 2)
print(a >> 1)  # 2   right shift (divide by 2)

#Identity Operators
a = [1, 2]
b = [1, 2]
c = a

print(a is b)      # False — different objects, same value
print(a is c)      # True  — same object
print(a is not b)  # True

#Membership Operators
nums = [1, 2, 3]
print(2 in nums)      # True
print(5 not in nums)  # True


#Operator precedence
print(2 + 3 * 4)      # 14, not 20 — * before +
print((2 + 3) * 4)    # 20 — parentheses override
#Rough order (high to low): ** → unary -/+ → *, /, //, % → +, - → comparisons → not → and → or

#Chained comparisons
x = 5
print(1 < x < 10)          # True — same as (1 < x) and (x < 10)
print(1 < x < 10 < 20)     # True — chains any length

#Walrus operator
# Normal way
n = 10
if n > 5:
    print(n)

# Walrus way — assign AND use in one expression
if (n := 10) > 5:
    print(n)  # 10

#in / not in
print("cat" in "concatenate")  # True — substring check

#Ternary-style
age = 20
status = "adult" if age >= 18 else "minor"

#Augmented assignment on mutable objects — subtle trap
a = [1, 2]
b = a
a += [3]      # this MODIFIES the list in place
print(b)      # [1, 2, 3] — b changed too!

a = [1, 2]
b = a
a = a + [3]   # this creates a NEW list
print(b)      # [1, 2] — b unaffected