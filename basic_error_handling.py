# there are many types of error in python like syntax error , typing error , ..........

print("hello world ")
ls = [1, 2, 3]
print(ls[2])

# try except example

try:
    print("hello world ")   # fixed bracket
    x = int("abc")          # this will cause ValueError
except ValueError:
    print("Error: Give right input / correct the syntax")

