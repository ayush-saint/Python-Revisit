#dafault parameter 
def hello(name="guest"): #this is called as default parameter just pass the value in function
    print(f"hello {name}")

hello()

hello("ayush")#if you pass value in function call again it will print the last one 


#keyword arguments : where you can pass value in function while calculation and numbers 
def addnumber(x=10,y=22):
    return x+y
print(addnumber())

#scope : accessing value from outside function 
x=100
def printhundred():
    print(x)

printhundred()

#global variable : if you want to access two variable then use it 
def printhundredagain(y):
    global x
    print(x,y)

printhundredagain(10)#value of y is passed

#nested function : function inside another function 
def hello(name):
    print(f"hello {name}")
    
def fav_city(city_name, name):
    hello(name)
    print(f"welcome to {city_name}!")

fav_city("mumbai","david")

