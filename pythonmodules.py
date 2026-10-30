
# modules and library are the same thing 
# import ing modules : meaning to import all the information python module has
# import math : meaning to import all the information math module has, so that i can use math's properties and operation

import math
print(math.sqrt(100))

import math as m 
print(m.sqrt(225))

# getting random number 
import random
print(random.random())
print(random.randint(1000,9999))

list=["blue","white","balck","green","purple","pink"]
random.shuffle(list)
print(list)
print(random.choice(list))

# other modules/libraries : json, os, requests