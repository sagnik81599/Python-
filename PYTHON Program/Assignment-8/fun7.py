#7

def is_perfect(num):
    sum=0
    for i in range(1, num):
        if num % i == 0:
            sum=sum+i
    if sum == num:
        print("The number is a perfect number")
    else:
        print("The number is not a perfect number")

is_perfect(6)
is_perfect(8)