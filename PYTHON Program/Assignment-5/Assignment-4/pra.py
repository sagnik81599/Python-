emp="Suman"
empid="EI"
desination="Manager"
salary='75450.50'
s1="{} with {} as {} get salary rs. {}"
print(s1.format(emp,empid,desination,salary))
list2=[1,5,2,8,3]
list2.sort()
print(list2)
tup_s=("BCA","MCA","JAVA")
for i in tup_s:
    print(i)
list_s=list(tup_s)
list_s.append("Python")
tup_s=tuple(list_s)
print(tup_s)
str="BCA"
print(str.replace('B','M'))
sag="Adamas"
print(sag[-3:])

print(type(sag))
