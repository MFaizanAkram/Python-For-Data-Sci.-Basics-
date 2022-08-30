#Defining a function:
# 1

def print_faizan():
    print("I am learning python with aammar")
    print("I am learning python with aammar")
    print("I am learning python with aammar")      

print_faizan()

# 2
def print_hamza():
    text="I am studying Alevel from TMUC"
    print(text)
    print(text)
    print(text)
    print(text)

print_hamza()   

# 3
def print_zeeshan(text):
    print(text) 
    print(text)
    print(text)

print_zeeshan("He is my elder brother")

#Defining a function with if, else and elif statements:
def school_calculator(age, text):
    if age==5:
            print("faizan can join the school")
    elif age>5:
            print("he should go to higher school")
    else:
            print("he is still a baby")
school_calculator(5, "faizan")

#Defining a function of Future:
def future_age(age):
    new_age=age+20
    return new_age
    print(new_age)
future_predicted_age=future_age(3) 
print(future_predicted_age)