from math import factorial


################ Factorials ################

### vol 1
def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact
#print(iterative_factorial(5))

### vol 2
def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n -1)
        temp = temp * n
    return temp
#print(recur_factorial(5))

### vol 3
def recur_factorial1(n):
    if n == 1: return n
    else: return n * recur_factorial1(n - 1)
#print(recur_factorial1(5))

################ Recursive Vs Iterative ################
################ Recursive Function Swap 2 letters ################

def permute(string, pocket=''):
    if len(string) == 0:
        print((pocket))
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)
#print(permute('ABC', ''))
# This is more steps

################ Iterative ################

def permutations(str):
    for p in range(factorial(len(str))):
        #print(''.join(str))
        i = len(str) - 1
        while i > 0 and str[i - 1] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i
            while str[i - 1] > str[q]:
                q += 1
            temp = str[i - 1]
            str[i - 1] = str[q]
            str[q] = temp
s = 'abc'
s = list(s)
permutations(s)
# This is less steps



################ 8 Queens Problem ################

# Iterative
def test(intizsor):
    masikint = 1
    for i in range(intizsor):
        masikint = masikint * (i + 1)
    return masikint

#print(test(5))

# Recursive
def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number-1)

#print(factorial(5))

################ Algorithms within Data Structures ################

# Linear Search
def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

arr = [2, 5, 8, 9 ,10 ,16, 22]
target = 16

print(search(arr, target))

# Iterative binary search
def binary_itr(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
    return start

arr = [2, 5, 8, 9 ,10 ,16, 22]
target = 16