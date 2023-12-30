def age(a):
    try:
        assert a>=18
    except:
        print(" your age is Not eigiable for vote")
    else:
        print(" your age is Eigiable for vote")
a=int(input("Enter your age :"))
age(a)                