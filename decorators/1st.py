def hello_decorator(func):
    def inner1(*args,**kwargs):
        print("before execution")
        return_value=func(*args,**kwargs)
        print("after execution")
        return return_value
    return inner1


@hello_decorator
def sum_two(a,b):
    print("inside the function")
    return a+b
a,b=1,2
print(sum_two(10,20))
