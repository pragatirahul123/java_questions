import json
d = {'alpha': 1, 'beta': 2}
s = json.dumps(d)
open("out.json","w").write(s)

with open("out.json") as fd:
	s = json.load(fd)
	print(s)


