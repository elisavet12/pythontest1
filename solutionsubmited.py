

# 1. Length
# The length should be 20
str='ballfromtheotherside'
print("Length of str=", len(str))

# 2. Positions
# Now, show the third letter
str='ballfromtheotherside'
print(str[3])

# 3. Index
# Display the position of the first match with the letter a
# It should print 1
s="bananabananabanana"
print("First position of the letter a = ", str.index('a'))

# 4. Count
# Count at least 5 letters a
s="bananabananabanana"
print("It has ", s.count("a"))

# 5. Print in rows
# Print every letter of the string
s="bananabananabanana"
for s in "bananabananabanana":
  print(s)

# 6. For the next exercise, leave the value of `str` as it is
# and use methods to change the given string to lower case, 
# print it, then change it to upper case and print it
str="HeLLo, hoW aRe You?"
str=str.lower()
print(str)

str=str.upper()
print(str)


