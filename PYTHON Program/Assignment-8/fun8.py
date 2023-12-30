def is_palindrome(string):
    string = string.replace(" ", "").lower()
    reverse_string = string[::-1]  # Reverse the string using slicing

    if string == reverse_string:
        return True
    else:
        return False
input_string=input("Enter the number: ")
if is_palindrome(input_string):
    print("The given string is a pallindrome")
else:
    print("The given string is not a pallindrome")
string="madam"
is_palindrome(string)