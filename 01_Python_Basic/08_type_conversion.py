x = 9              #Integer
y = 7.3            #Float
z = "Hello!"       #String

print(type(x))
#if we multiply/add interger with float. The answer will be in float.

#implicit type conversion:
x=x+y
print(x ,"the type of x is:", type(x)) 

#explicit type conversion:
#age= input("what is your age? ")
#age=int(age)
#print(type(age))
    #another way:
#print(age, type(str(age)))
#integer don't convert point numbers(18.5)
#to get point numbers(18.5), we need to write float to convert it into float no.
#age=input("what is your age? ")
#print(age, type(float(age)))

#name
name=input("what is your name? ")
print(name, type(str(name)))