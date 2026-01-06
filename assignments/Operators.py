#Read 2 numbers from user and (a)perform basic calculator operations (+, -, *, /, %)  and print results
# (b)print results of checking if first number is greater than second number,
# first number is lesser than second number.

a=int(input("Enter first number : "))
b=int(input("Enter second number : "))

#(a) Basic calculator operations
print("Addition : ",a+b)
print("Subtraction : ",a-b)
print("Multiplication : ",a*b)
print("Division : ",a/b)
print("Modulo : ",a%b)

#(b) Comparison results
print("First Number is greater than second : ",a>b)
print("First Number is less than second : ",a<b)
