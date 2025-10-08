#The while Loop
    #With the while loop we can execute a set of statements as long as a condition is true.

a = 1

while a < 10:
    print(a)
    a += 1


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# The Foor Loop
    #A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

a = 5

for  i in range (1,a+1):
    for j in range(1,i + 1):
        print("*",end=" ")
    print()