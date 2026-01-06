#parameterized function are used when we need to execute the sane function with different values

"""def add(a,b):
    print(a+b)

add(4,6)
add(5,7)


#return statement
def addition(a,b):
    return a+b

#if we use the return statement first need to assign this to a variable
result=addition(5,5)
print(result)"""


"""a=int(input("enter first number"))
b=int(input("enter second number"))
def subtraction():
    return a-b
print(subtraction())"""


#calculator
#it will return multiple return values
"""def new_function(a,b):
    return a+b,a-b,a*b,a/b
result1,result2,result3,result4=new_function(10,5)
print(result1,result2,result3,result4)"""


#variable length function
#each and every time of invoking we can modify the number of values of parameters
"""def find_maximum(*args):
    return max(args) # max : it is a build in function used to make the mathematical calculation easy
maximum=find_maximum(2)
print(maximum)"""

#anonymous function : function without name
#lambda keyword is used

add=lambda x,y:x+y
print(add(10,20))