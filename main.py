import math
"""
from prime import check_prime
from power import power2n
"""
arr = "[[3, 2], [4, 3], [2, 3], [3, 4]]"
pid = [29, 59, 14, 11, 3, 13, 15, 18, 12, 16, 6, 17, 7, 47, 61, 5, 21, 2, 41, 9, 10, 8, 19, 1, 4]
pid.sort()
arr.split()
#print(pid)
"""
def AWM(arr, pid):
    l1 = len(arr)
    for i in range(l1):
        arr = int(string)
    for i in range(l1):
        print(arr)
    for i in range(0,l1):
        for j in arr:
            while l1:
                if check_prime(pid):
                    arr[[i][j]]="A"
                elif power2n(pid):
                    arr[[i][j]]="W"
                else:
                    arr[[i][j]]="M"




AWM(arr, pid)

"""
def check_prime(pid):
    length = len(pid)
    li=[]
    for i in range(2,length+1):
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            li.append(i)
    print(li)


check_prime(pid)


def Log2(x):
    if x == 0:
        return True
    return math.log10(x) / math.log10(2)


def power2n(pid):
    l = len(pid)
    for i in range(l):
        if math.ceil(Log2(i)) == math.floor(Log2(i)):
            print(i)


power2n(pid)

