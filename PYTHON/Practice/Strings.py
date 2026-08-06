s=" python programming "
print(s[0])
print(s[0:5]) #until 5th letters
print(s[:5]) # until 5th letters
print(s[7:])    #from 7th letter
print(s[::-1]) # prints every -1 step reverse
print(s[::2]) # prints every 2 step forward


print(s.len())
print(s.strip())
print(s.split())
print(s.lower())
print(s.upper())
print(s.find("python"))
print(s.count('p'))
print(s.capitalize())


prize=1234.5678
print(f"{prize:,.3f}")
# adds thousands-separators and rounds to 3 decimals
print(f"{prize:.2f}")
# rounds to 2 decimal places
print(f'{prize:>10}') # after occupying prize digits remaining numbers keeps left side  {  1234.5678} # 2 space kept left side
print(f'{print:<10}') # after occupying prize digits remaining numbers keeps right side  {1234.5678  } # 2 space kept right side
print(f'{prize:^10}') # prize will be in middle with in 10 spaces

s = "the,quick,,brown,fox"
print(s.split(','))

#Join()
print('-'.join([1,2,3,45,6,7]))
#separator.join(iterable object) returns 1-2-3-45-6-7

#concatenation
print("Jinka"+"mahesh")
print("Jinka"*4)

#Checking String Content
print("123".isdigit()) # true (all are digits)
print("12d".isdigit()) # false (all are not digits)
print("abc".isalpha()) # every character is alphabet
print("123abd".isalpha()) # every character is not alphabet
print("1234anhgsdb".isalnum()) # every charcater is combination of alphabet and numbers
print("1234jhfd$^$&%".isalnum()) #every character is not combination os alphabet and numbers
print("  ".isspace()) #every character is a whitespace character
print("\t\n".isspace()) #every character is a whitespace character
print("h   ".isspace()) # every charcater is not whitespace character
print("MAHESH".isupper()) # all are uppercase letters
print("mahesh".lower()) #all are lowercase letters
print("Mahesh Jinka".istitle()) # each word starts with capitol letter
print("76478.975".isdecimal()) # it is decimal value


#Escape characters
print("ertyui\nrthjkl") # new line
print("ertyuk\tdvbnm") #tab
print("\"Hi\" Mahesh") # \" makes compiler to think sentence not finished yet
print(r"c:\new\folder") # Raw string ,compiler think these are literal character and ignores escape sequence

'''
\n    # newline
\t    # tab
\\    # literal backslash
\'    # literal single quote
\"    # literal double quote
\r    # carriage return
\b    # backspace
'''

#Unicode
print(ord(a))
print(ord(A))


#lexicographic
print(apple<banana)
#compares with unicode character by character
#if both characters unicodes are equal it will move to nect charcaters else it will stop and compare and returns
print(Apple<apple) #uppercase have lesser unicode than  lowercase


#Join
a=["Hi","Jinka","Mahesh"]
print("".join(a))
print(" ".Join(a))
print(",".join(a))


#Splitting with parameters
a="a,b,c,d" 
print(a.split(","))
print(a.split(",",2)) # maxsplit limits how many splits happen

#string multiplication
print("-"*40)

#zFill() - padding numbers with 0's
print("7".zfill(4)) # 0007

#String Immutability
#inefficient method
result=""
for i in range(1000):
    result+=i
print(result)

#Efficient method
print("".join(str(i) for i in range(1000)))

#Encode and Decode
a="Mahesh"
print(a.encode("utf-8"))
print(a.encode("utf-8".decode("utf-8")))


#substring
a="MaheshJinka"
print("Jinka" in a)

print(a.find("Mahesh") !=-1)

#string repitition
print(" | ".join([a]*3))