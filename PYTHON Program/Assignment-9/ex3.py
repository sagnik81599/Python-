try:
    l1=[1,2,5,7]
    i=int(input("Enter index: "))
    print("Element is:",l1[i])
except IndexError:
    print("Index Error")