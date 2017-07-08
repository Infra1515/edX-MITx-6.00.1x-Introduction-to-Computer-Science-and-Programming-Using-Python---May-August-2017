# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the letters occur
# in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart.
# If you've spent more than a few hours on this problem,
# we suggest that you move on to a different part of the course.
# If you have time, come back to this problem after you've had a break and cleared your head.

test = s[0]      # seed with first letter in string s
best = ''        # empty var for keeping track of longest sequence

for n in range(1, len(s)):    # have s[0] so compare to s[1]
    if len(test) > len(best):
        best = test
    if s[n] >= s[n-1]:
        test = test + s[n]    # add s[1] to s[0] if greater or equal
    else:                     # if not, do one of these options
        test = s[n]

if len(test) > len(best):
    best = test

print ("Longest substring in alphabetical order is:", best)
