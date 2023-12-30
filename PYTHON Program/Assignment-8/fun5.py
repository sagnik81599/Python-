#5 WRITE A UFNCTION TO FIND UPPERCASE AND LOWERCASE ELEMENTS FROM A STRING AND PRINT IT

def countChar(string):
    uppercase = 0
    lowercase = 0

    for char in string:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1

    print("The number of uppercase characters is :",uppercase)
    print("The number of lowercase characters is :",lowercase)

str1="We Learn Python PrograM"
countChar(str1)