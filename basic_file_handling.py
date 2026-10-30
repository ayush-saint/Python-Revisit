# open(filename, mode)
# filename - myfile.txt, myfile.json, ...
# mode - read (r), write (w), append (a), .....

with open('myfile.txt', 'r') as f:
    print(f.read())

with open('myfile.txt', 'a') as f:
    f.write('\nthis is the second line')