def add_numbers(x,y):
    result=x+y
    print("sum: ", result)
add_numbers(10,2)
    # get product
def get_product(x,y,z):
    result=x*y*z
    print("product: ", result)
get_product(1,2,3)

#return
def get_status(a,b):
    return a+b,a-b
sum_value,subtract_value =get_status(2,5)
print("sum: ",sum_value)
print("subtract: ",subtract_value)
#division
def devide_number(x,y):
    return x/y
answer=devide_number(10,2)
print("answer: ",answer )
    