import sys
import os
def add(num1,num2):
    a=num1+num2
    return a
def sub(num1,num2):
    s=num1-num2
    return s
def mul(num1,num2):
    m=num1*num2
    return m 
num1=float(sys.argv[1])
operation=sys.argv[2]
num2=float(sys.argv[3])
if operation=="add":
    print(add(num1,num2))
elif operation=="sub":
    print(sub(num1,num2))
else:
    print(mul(num1,num2))
# export password="pass"
# export token="token"
name=os.getenv("password")
token=os.getenv("token")
print(token)
print(name)

# calculator.py 5 add 10

