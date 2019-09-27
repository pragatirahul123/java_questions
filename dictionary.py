a={0: 10, 1: 20}
a[2] = 30
print (a)
str1=str(obj)

print (obj["teacher"]["Maths"])
print (obj["marks"]["Maths"]

#dict1 = {"one":1, "two":2, "three": {"five": 3.1, "four": 3.2 }}
#str1 = str(dict1)
#print (dict1["three"]["four"])

import json 
  
# list conversion to Array 
print(json.dumps(['Welcome', "to", "GeeksforGeeks"])) 
  
# tuple conversion to Array 
print(json.dumps(("Welcome", "to", "GeeksforGeeks"))) 
  
# string conversion to String 
print(json.dumps("Hi")) 
  
# int conversion to Number 
print(json.dumps(123)) 
  
# float conversion to Number 
print(json.dumps(23.572)) 
  
# Boolean conversion to their respective values 
print(json.dumps(True)) 
print(json.dumps(False)) 
  
# None value to null 
print(json.dumps(None)) 
["Welcome", "to", "GeeksforGeeks"]
["Welcome", "to", "GeeksforGeeks"]
"Hi"
123
23.572
true
false
null


