#There are 2 type of loops:

#1: while loops:
x=0
while (x<10):
    print(x)
    x=x+3

#2: For loop:
for x in range(3,9):
    print(x)
    
#Array

days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
for d in days:
    #if (d=="fri"): break #loop stops
    if (d=="fri"): continue #skips d
    print(d)