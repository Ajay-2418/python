#A function is a block of code which only runs when it is called.

#You can pass data, known as parameters, into a function.

#A function can return data as a result.



def palidrome(num):
    str_num = str(num)


    return str_num == str_num[::-1]


number = input("Enter Number:")

if palidrome(number):
    print("This Number is Palidrome")
else:
    print("This Number is Not Palidrome")
