# dictionary
# list=[] , dictionary={}
student={"name":"raju", "age":21, "gender":"male"}
# these are key-value pair
# these dictionary accept all data types like string , integer , float etc 

# accessing values
print(student["name"]) 


#updating values 
student["name"]="david"

# looping through a dictionary 
for key in student:
    print(key)

for k, v in student.items():
    print(k,v)

