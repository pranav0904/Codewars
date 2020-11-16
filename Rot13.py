'''
Author: Pranav Khiste

Task:  ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. 
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

'''

import string

def rot13(message):
    alphabet_list = list(string.ascii_lowercase)+list(string.ascii_lowercase)
    sol=''
    
    for i in message:
        if i.isupper():
            letter=i.lower()
            index = alphabet_list.index(letter)
            sol += alphabet_list[index + 13].upper()
        elif i.islower():
            index = alphabet_list.index(i)
            sol += alphabet_list[index + 13]
        else:
            sol += i
    return sol