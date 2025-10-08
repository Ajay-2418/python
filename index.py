"""age = int(input("Enter your age:"))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")"""


# Check if a number is palindrome in Python

'''password = "1234"
a = 0
max = 3
while a < max:
    user = input("Enter Password:")
    if user == password:
        print("Password correct")
    else:
        print("Incorrect Password")
        a +=1
    if a == max:
        print("Limt are reched")
'''



text = input("")

d = 0
a = 0
for i in text:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        a+=1

print("Diits:",d, "Alphabets",a)

