# problem 1
# Assume s is a string of lower case characters.
# Write a program that counts up the number of
# vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#  For example, if s = 'azcbobobegghakl', your program should print: 5

vowels = ('a','e','i','o','u')
i = 0

for ch in s:
    if ch in vowels:
        i += 1
print('Number of vowels:', i)
