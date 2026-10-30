# there are many types of error in python like syntax error , typing error , ..........

print("hello world ")
ls = [1, 2, 3]
print(ls[2])

# try except example : The try block tests code; if an error occurs, control jumps to except instead of stopping

try:
    print("hello world ")   
    x = int("abc")          
except ValueError:
    print("Error: Give right input / correct the syntax")

