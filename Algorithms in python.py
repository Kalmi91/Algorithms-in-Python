from math import factorial


################ Factorials ################

### vol 1
def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact
print(iterative_factorial(5))

### vol 2
def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n -1)
        temp = temp * n
    return temp
print(recur_factorial(5))

### vol 3
def recur_factorial1(n):
    if n == 1: return n
    else: return n * recur_factorial1(n - 1)
print(recur_factorial1(5))

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
print(permute('Ab', ''))
# This is more steps

################ Something somewhere is wrong, but I can't see ################
def permutations(str):
    for p in range(factorial(len(str))):
        #print(str)
        print(''.join(str))
        i = len(str) - 1
        #print(i)
        while i > 0 and str[i - 1] > str[i]:
            #print(i)
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