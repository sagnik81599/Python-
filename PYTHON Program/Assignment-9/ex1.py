try:
    n=int(input("Enter a number: "))
    d=int(input("Enter a dividor"))
    print(n/d)
 
except ZeroDivisionError:
    print("Dividor must not be a 0")       