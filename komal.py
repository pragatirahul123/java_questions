import json
a ={"name":"John", 
   "age":31, 
    "Salary":25000} 
b = json.dumps(a) 
print(b) 
print type(a)
print type(b)
