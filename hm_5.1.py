import string
import keyword

symbols = set(string.punctuation)
digit = set(string.digits)
uppercase_letters = set(string.ascii_uppercase)
kwlist = set(keyword.kwlist)
name = ''

symbols.remove('-')
print(uppercase_letters)
user_input = input("Enter your text: ")

if user_input in kwlist:
    print('No')
else:
    for char in user_input:
        if (char in symbols
                or char in digit
                or char in uppercase_letters):
            print('invalid char')
            break
        else:
            name += char

if user_input == name:
    print(name + ' is valid')
else:
    print('invalid name')
