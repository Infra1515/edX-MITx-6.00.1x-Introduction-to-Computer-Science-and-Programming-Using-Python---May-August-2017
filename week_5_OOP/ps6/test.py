import string
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
alphabet_lower_cipher = string.ascii_lowercase
alphabet_upper_cipher = string.ascii_uppercase
chars_not_to_be_removed = string.digits + string.punctuation + ' '
shift_dict = {}
k = 7

for i in range(k):
    alphabet_lower_cipher += alphabet_lower[i]
    alphabet_upper_cipher += alphabet_upper[i]

for index, element in enumerate(alphabet_lower):
    shift_dict[element] = alphabet_lower_cipher[index+k]

for index, element in enumerate(alphabet_upper):
    shift_dict[element] = alphabet_upper_cipher[index+k]

word =  "we are taking 6.00.1x"
new_word = ''
#
# for i in range(len(word)):
#
#     new_word += shift_dict[word[i]]
#     print(new_word)
#
for index, element in enumerate(word):
    if element in chars_not_to_be_removed:
        new_word += element
    else:
        new_word += shift_dict[word[index]]
print(new_word)


$ flask\Scripts\pip install flask
$ flask\Scripts\pip install flask-login
$ flask\Scripts\pip install flask-openid
$ flask\Scripts\pip install flask-mail
$ flask\Scripts\pip install flask-sqlalchemy
$ flask\Scripts\pip install sqlalchemy-migrate
$ flask\Scripts\pip install flask-whooshalchemy
$ flask\Scripts\pip install flask-wtf
$ flask\Scripts\pip install flask-babel
$ flask\Scripts\pip install guess_language
$ flask\Scripts\pip install flipflop
$ flask\Scripts\pip install coverage
