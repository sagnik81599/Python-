def division(a,b):
    try:
        print("Division is:",a/b)
    except ArithmeticError:
        print("Division must not zero")
a=int(input("Enter divident :"))
b=int(input("Enter dividor :"))
division(a,b)   


       
