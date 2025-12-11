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
