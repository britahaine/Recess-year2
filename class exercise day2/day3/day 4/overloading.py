from multipledispatch import dispatch

@dispatch(int, int,int)
def add(a, b,c):
    print("Adding integers:", a + b + c)

@dispatch(str, str)
def add(a, b):
    print("Concatenating strings:", a + b)

@dispatch(float, float)
def add(a, b):
    print("Adding floats:", a + b)

add(2, 3,5)            
add("hello ", "there")  
add(1.5, 2.3)        
