# tuples
mytuples = (1,2,3)
 
# accessing tuples
print(mytuples[1])

# adding two tuples 
tp1 = (1,2,3)
tp2 = ("a","b","c")
print(tp1+tp2)

# operations on tuples 
print(tp1*3)    

#tuples unpacking : Tuple unpacking means assigning tuple values to multiple variables in one line.

tp4 =(1,2,3)
a=1
b=2
c=3
a, b, c = (10,20,30)
print(b)

# tuples vs lists : tuple → An ordered, immutable(can't change element) collection of elements written using ( ), less memory required///// List → An ordered, mutable collection of elements written using [ ], high memory usage 

# sets : unique value in list 
list = [1,1,2]
print(set(list))

set1 ={1,2,3} 
set2 ={2,5,6}

# set operation 

print(set1.union(set2))
print(set1.intersection(set2))

