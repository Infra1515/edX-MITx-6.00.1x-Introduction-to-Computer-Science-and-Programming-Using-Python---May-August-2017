def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
  vowels = 'aeiou'
  no_vowels = []


  for letter in list(s):
     if letter not in vowels and letter not in vowels.upper():
         no_vowels.append(letter)
  print(''.join(no_vowels))
