def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("select operations,")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
choice=int(input("Enter choice (1/2/3/4)"))
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if (choice==1):
    print "The sum of num1 and num2 is:"
    sum=add(num1,num2)
    print (sum)
elif(choice==2):
    print "The subtraction of num1 and num2 is:"
    sub=sub(num1,num2)
    print (sub)   
elif (choice==3):
    print "The multiplication of num1 and num2 is:"
    mul=mul(num1,num2)
    print (mul)    
else:
    print("the division of two given number is:")
    div=div(num1,num2)
    print(div)



