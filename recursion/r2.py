'''
def sumN(n):
    if n==0:
        return 0
    else:
        return n+sumN(n-1)
print(sumN(5))
'''
'''
def sumN(n):
    if n==0:
        return 0
    else:
        return 2*n-1+sumN(n-1)
print(sumN(5))
'''
'''
def sumN(n):
    if n==0:
        return 0
    else:
        return 2*n+sumN(n-1)
print(sumN(5))
'''
'''
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
'''


def sumN(n):
    if n==1:
        return 1
    else:
        return n*n+sumN(n-1)
print(sumN(5))
        










