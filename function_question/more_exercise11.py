marks=[[45,21,42,63],[12,42,42,53],[42,90,78,13],[94,89,78,76],[87,55,98,99]]
index=0
while index<len(marks):
	j=len(marks[index])
	var=0
	max=0
	while var<j:
		if max<marks[index][var]:
			max=marks[index][var]
		var=var+1
	index=index+1
	print max
