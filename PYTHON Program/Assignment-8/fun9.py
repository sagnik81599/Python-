def GCD(x,y):
    if y==0:
        return x
    else:
        return GCD(y,x%y)
    
res=GCD(7,2)
print(res)
    