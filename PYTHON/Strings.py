#Creating strings
s1 = 'hello'
s2 = "hello"
s3 = '''multi
line'''
s4 = """also
multi line"""

#Indexing and Slicing
s = "Hello, World"

print(s[0])      # 'H'
print(s[-1])     # 'd' — negative indexing from the end
print(s[0:5])    # 'Hello' — slice [start:end), end excluded
print(s[:5])     # 'Hello' — omit start = from beginning
print(s[7:])     # 'World' — omit end = to the end
print(s[::-1])   # 'dlroW ,olleH' — reverse the string
print(s[::2])    # 'Hlo ol' — step of 2

#Strings are immutable
#for immutable inplace assignment is not possible
s = "hello"
s[0] = "H"   # TypeError — can't modify a string in place
s = "Hello"  # this creates a NEW string, doesn't modify the old one

#Common string methods
s = "  Hello World  "

print(s.strip())        # "Hello World" — removes leading/trailing whitespace
print(s.lower())        # "  hello world  "
print(s.upper())        # "  HELLO WORLD  "
print(s.replace("World", "Python"))  # "  Hello Python  "
print(s.split())        # ['Hello', 'World'] — splits on whitespace by default
print("-".join(["a", "b", "c"]))  # "a-b-c"
print(s.strip().startswith("Hello"))  # True
print(s.strip().endswith("World"))    # True
print(s.find("World"))   # index where found, or -1 if not found
print(s.count("l"))      # counts occurrences

#f-strings
name = "Mahesh"
score = 92.567

print(f"Name: {name}")
print(f"Score: {score:.2f}")     # 2 decimal places → 92.57
print(f"{name.upper()}")          # can call methods inside {}
print(f"{score:>10}")             # right-align in 10-char width
print(f"{score:,.2f}")            # comma separators for large numbers with 2 deciamals
pct = 0.4567
print(f"{pct:.1%}")                          # 45.7%  -- percent formatting built in
'''Breaking down {pct:.1%}

The format spec after the : is .1%. Two parts:

% — percentage type: This tells Python to do two things automatically:
Multiply the value by 100
Append a % symbol
.1 — precision: Number of digits after the decimal point (in the percentage form, not the original number).'''

# Debug shortcut (3.8+) — prints both the expression and its value
x = 42
print(f"{x=}")                               # x=42

#String concatenation
a = "Hello"
b = "World"
print(a + " " + b)     # "Hello World"
print(a * 3)             # "HelloHelloHello" — repetition

#Checking string content
print("123".isdigit())     # True
print("abc".isalpha())     # True
print("abc123".isalnum())  # True
print("   ".isspace())     # True


#Escape characters
print("Line1\nLine2")   # \n = newline
print("Tab\there")       # \t = tab
print("She said \"hi\"") # \" = literal quote
print("C:\new\folder") # considers /n as new line
print(r"C:\new\folder")  # raw string — ignores escape sequences, prints backslashes literally

#String comparison (lexicographic, character by character)
print("apple" < "banana")   # True — compares by Unicode value
print("Apple" < "apple")    # True — uppercase letters have lower Unicode values than lowercase

#str.join()
words = ["Python", "is", "great"]
print(" ".join(words))    # "Python is great"
print("".join(words))     # "Pythonisgreat"
print(", ".join(words))   # "Python, is, great"
#join() is called on the separator, not the list


#Splitting with a specific delimiter and limit
s = "a,b,c,d"
print(s.split(","))        # ['a', 'b', 'c', 'd']
print(s.split(",", 1))     # ['a', 'b,c,d'] — maxsplit limits how many splits happen

#String multiplication with formatting
print("-" * 30)   # a divider line, common in printed reports


#zfill() — padding numbers with zeros
print("7".zfill(3))    # "007"

#String immutability performance note
# Inefficient — creates a new string object on every iteration
result = ""
for i in range(1000):
    result += str(i)

# Better — join is more efficient for many concatenations
result = "".join(str(i) for i in range(1000))

#Encoding/decoding basics
s = "hello"
encoded = s.encode("utf-8")     # b'hello' — bytes object
decoded = encoded.decode("utf-8")  # back to "hello"
text = "café"
encoded = text.encode("utf-8")     # str -> bytes
print(encoded)                      # b'caf\xc3\xa9'
print(type(encoded))                # <class 'bytes'>

decoded = encoded.decode("utf-8")  # bytes -> str
print(decoded)                      # café

b = b"hello"          # byte string literal
print(type(b))         # <class 'bytes'>
print(b + text.encode())  # concatenation works only bytes-to-bytes


#str.title() vs str.capitalize()
s = "the quick brown fox"
print(s.capitalize())  # "The quick brown fox" — only first letter of whole string
print(s.title())       # "The Quick Brown Fox" — first letter of EVERY word

#Checking substrings
s = "hello world"
if "world" in s:      # preferred, Pythonic way
    print("found")

# vs using .find() and checking for -1 — works but less readable
if s.find("world") != -1:
    print("found")

#String repetition with separators
print(" | ".join(["a"] * 3))   # "a | a | a"