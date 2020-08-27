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