#qn1
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

print("Shoe size:", Shoes["size"])

#qn2
Shoes["brand"] = "Adidas"
print( Shoes)

#qn3
Shoes["type"] = "sneakers"
print("Updated dictionary:", Shoes)

#qn4
keys_list = list(Shoes.keys())
print("Keys:", keys_list)

#qn5
values_list = list(Shoes.values())
print("Values:", values_list)

#qn6
if "size" in Shoes:
    print("Key 'size' exists in the dictionary.")
else:
    print("Key 'size' does not exist in the dictionary.")

#qn7
for key, value in Shoes.items():
    print(key,value      )
    
    #qn8
    Shoes.pop("color", None)
print("Dictionary after removing 'color':", Shoes)

#qn9
Shoes.clear()
print("Emptied dictionary:", Shoes)

#qn10
original_dict = {
    "name": "Alice",
    "age": 30,
    "city": "Kampala"
}

copied_dict = original_dict.copy()
print("Original dictionary:", original_dict)
print("Copied dictionary:", copied_dict)

#qn11
student = {
    "name": "John",
    "age": 22,
    "courses": {
        "math": 85,
        "science": 90,
        "history": 78
    }
}

print("Nested dictionary:", student)


