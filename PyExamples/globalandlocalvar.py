#global var
total=0
def sum(arg1,arg2):
#total=local variable
    total=arg1+arg2;
    print"Inside the functon local total:",total
    return total;
sum(10,14)
print"Outside the function global total:",total

