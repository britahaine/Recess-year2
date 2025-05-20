#qn1
beverages = set(("Coffee", "Tea", "Juice"))
print( beverages)

#qn2
beverages.add("oner")
beverages.add("milk")
print(beverages)

#qn3
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Yes, 'microwave' is in the set.")
else:
    print("No, 'microwave' is not in the set.")
    
#qn4
mySet.remove("kettle")
print(mySet)

#qn5
for y in beverages:
    print(y)
    
#qn6
my_set = {"apple", "banana", "cherry", "ovacado"}
my_list = ["mango", "grape"]

my_set.update(my_list)
print( my_set)

#qn7
age = {23}
first_name = {"Britah"}

combined_set = age.union(first_name)
print("Combined set:", combined_set)

