#items syntax 

items = ["speaker", "mic","laptop"]
#printing list and list's element

print(items[0])
print(items[-1])
print(items[0:2])
#replacing elements in list 

items[2]="pc"
#printing whole list 

print(items)
#to add element 

items.append("charger")
#to remove element 

items.remove("mic")
#deleting elements in list

del items[2]
#clearing entire list 

items.clear()
print("earbuds" in items)
#cheaking if the items is in list or not 

print(len(items)) 
#cheaking the length of the list 

scores=[70,35,30]

for i in scores:
    print(i/2)
#for loop way - to divide each element of scores by 2 

print([i/2 for i in scores])
#-----list comprehension-----used to make a new list using previous list in python (shorter way than for loop)