'''
Author: Pranav Khiste

Task:  Write a function that accepts an array of 10 integers (between 0 and 9), 
that returns a string of those numbers in the form of a phone number.
Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

'''

def create_phone_number(n):
    
    index=0
    number=''   #String to return    
    for i in range(0,len(n)+4):
        if i == 0:
            number += '('
        elif i == 4:
            number+=')'
        elif i == 5:
            number += ' '
        elif i == 9:
            number += '-'
        else:
            number += str(n[index])  #appending next index value from the list
            index += 1
            
    #Returning updated string       
    return number

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])