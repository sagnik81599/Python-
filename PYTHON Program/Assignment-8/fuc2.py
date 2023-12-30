#2 TO FIND THE SUM OF ALL ELEMENTS OF A LIST USING FUNCTION
def find_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num
    print(sum)

list1 = [8,2,3,0,7]
print("Sum is :")
find_sum(list1)