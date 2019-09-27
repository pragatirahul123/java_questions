def insertionSort(arr): 

    for i in range(1, len(arr)): 
  
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
		j -= 1
        arr[j+1] = key
	print(arr[j+1]) 

arr = [3,5,49,-1,-2,0] 
insertionSort(arr)

print ("Buble short")
def bubbleSort(arr): 
    n = len(arr) 
  
    for i in range(n): 
  
        for j in range(0, n-i-1): 
  
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
		print (arr[j])
  
arr = [64, 34, 25, 12, 22, 11, 90] 
  
bubbleSort(arr) 
