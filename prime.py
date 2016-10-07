from math import sqrt

def primer(number):
    lst = range (2,number+1)

    for i in range(2,int(sqrt(number))+1):
        lst = list(filter(lambda x: x==i or x % i, lst))

    return lst

print (primer(100))

