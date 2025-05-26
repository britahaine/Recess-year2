try:
    result=5/0
except ZeroDivisionError:
    print("can not divide by zero")
else:
    print("division sucessful: ",result)
finally:
    print("run complete")
    
    
    