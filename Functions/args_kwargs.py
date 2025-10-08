'''When you define a function, you can use **kwargs to accept a variable number of named (keyword) arguments.'''
#ex:

data = [{
    "Name" : "Ajay",
    "Age" : "21",
    "Number" :"43"

},
{
    "Name" : "Anitha",
    "Age" : "20",
    "Number" :"43"

},]

def api (**kwargs):
    print(kwargs)

for records in data:
    api(**records)