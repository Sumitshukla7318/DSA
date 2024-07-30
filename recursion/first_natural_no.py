'''
def printN(n):
    if n>0:
        print(n)
        printN(n-1)
printN(10)
'''

def printN(n):
    if n > 0:
        printN(n - 1)
        print(n)

printN(10)

def printOdd(n):
    if n > 0:
        printOdd(n - 1)
        print(2*n-1)

printOdd(10)

def printEven(n):
    if n > 0:
        printEven(n - 1)
        print(2*n)

printEven(10)


