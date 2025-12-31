#function(block of code that does a specific task and can be reused whenever needed)- contains input, logic, output 
#here in function hello() - input nothing; logic print; output hello world


def hello():
    print("hello world")

hello()

#using input ; here in function hello(name) - input is name 
def hello(name):
    print(f"hello {name}")

hello("don")

#using input ; here in function hello(x,y) - input is x,y
def sum_numbers(x,y):
    print(x+y)

sum_numbers(2,3)

#function with return value 
# advantages of using return = return gives a value you can reuse, print just shows it on the screen.
def sum_of_numbers(x,y):
    return x+y
result = sum_of_numbers(2,4)
print(result)
