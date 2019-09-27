obj = {"name":"Ram","RollNo":"12","marks":[{"Maths":"50","English":"49","seci":"79"}],"teacher":{"Maths":"mr rama","english":"ms komal"}}
print (obj["teacher"]["Maths"])
print (obj["marks"]["Maths"])



obj = {"name":"Ram","RollNo":"12","marks":{"Maths":"50","English":"49","seci":"79"},"teacher":{"Maths":"mr rama","english":"ms komal"}}
var= str(obj)
print ("max"),(obj["marks"]["seci"])
print ("min"),(obj["marks"]["English"])

