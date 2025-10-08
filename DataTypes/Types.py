''' Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType 
'''


x = "Hello World" #str data type
y = 20            # int data type
z = 20.5          # float data type
a = 1j            # complex data type
b = ['apple', 'banana', 'mango', 122] # list data type
c = {'apple', 'banana', 'mango', 122} # set data type
d = ('apple', 'banana', 'mango', 122) # tuple data type
dict = {'Name': "Ajay", "Age": 21}    # dict data type

froz = ({"apple", "banana", "cherry"}) # forzenset

print(5 > 10) # bool

n = None

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print((dict))
print((froz))
print()
print((a))
print((b))
print((c))
print((d))
print((dict))
print((froz))