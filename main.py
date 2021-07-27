import math

def AWM(arr, pid):
    # to arrange the seats for passengers
    l1 = len(arr)
    for i in range(0, l1):
        for j in arr:
            while l1:
                if check_prime(pid):
                    arr[[i][j]] = "A"
                elif power2n(pid):
                    arr[[i][j]] = "W"
                else:
                    arr[[i][j]] = "M"


def check_prime(pid):
    # to check whether the passenger's id is prime number or not
    length = len(pid)
    li = []
    for i in range(2, length + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            li.append(i)
    return(li)


def Log2(x):
    # to convert the id into log base 2
    if x == 0:
        return True
    return math.log10(x) / math.log10(2)


def power2n(pid):
    #to check the passenger's id is power of 2
    l = len(pid)
    for i in range(l):
        if math.ceil(Log2(i)) == math.floor(Log2(i)):
            return(i)


arr = "[[3, 2], [4, 3], [2, 3], [3, 4]]"
pid = [29, 59, 14, 11, 3, 13, 15, 18, 12, 16, 6, 17, 7, 47, 61, 5, 21, 2, 41, 9, 10, 8, 19, 1, 4]
pid.sort()#sort the passenger's id
arr.split()

check_prime(pid)
power2n(pid)
AWM(arr, pid)
