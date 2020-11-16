'''
Author: Pranav Khiste

Task:  Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.

For example:
persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.
'''

def persistence(n):
    ls=list(str(n))
    if len(ls) <= 1:
        return 0
    
    cnt=0
    while len(ls) > 1:
        res=1
        for i in ls:
            res *= int(i)
        ls = list(str(res))
        cnt += 1
    return cnt

print(persistence(39))