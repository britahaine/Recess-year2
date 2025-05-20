#qn1
x = ("samsung", "iphone", "tecno", "redmi")
print("My favorite phone brand is:", x[1])

#qn2
print("The second last item  is:", x[-2])

#qn3
y=list(x) #change tuple to a list
y[1]="itel"
x=tuple(y)  #change list back to a tuple
print(x)

#qn4
y=list(x)
y.append("Huawei")
x=tuple(y)
print(x)

#qn5
for brand in x:
    print(brand)
    
    #qn6
    y=list(x)
    y.remove("redmi")
x=tuple(y)
print(x)

#qn7
cities_list = ["Kampala", "Entebbe", "Gulu", "Mbarara", "Jinja"]
cities = tuple(cities_list)
print("Cities tuple:", cities)

#qn8
x = ("samsung", "iphone", "tecno", "redmi")
brand1, brand2, brand3, brand4 = x
print("Brand 1:", brand1)
print("Brand 2:", brand2)
print("Brand 3:", brand3)
print("Brand 4:", brand4)

#qn9
cities = ("Kampala", "Entebbe", "Gulu", "Mbarara", "Jinja")
print(cities[1:4])

#qn10
first_name = ("Ainamatsiko ")
second_name= ("Shine")
print (first_name + second_name)

#qn11
colors = ("red", "green", "blue")
colors= colors * 3
print( colors)

#qn12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
thistuple= thistuple.count(8)
print("Number of times 8 appears:", thistuple)








