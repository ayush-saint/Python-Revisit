# let say we have a list =[1,2,2,3,2,3,4,5], now identify the most repetive elements in the list?_____use dictionaries 
# find most repetitive element using dictionary

nums = [1,2,2,3,2,3,4,5]

num_counter = {}

# Count frequency
for i in nums:
    if i in num_counter:
        num_counter[i] += 1
    else:
        num_counter[i] = 1

# Find maximum frequency
temp = 0
final_result = None

for k, v in num_counter.items():
    if v > temp:
        temp = v
        final_result = k

print("Frequency Dictionary:", num_counter)
print("Most Repeated Element:", final_result)
