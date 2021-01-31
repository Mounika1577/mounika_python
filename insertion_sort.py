arr=[12,11,13,5,6]

def rotate(arr,a,b):
    temp=arr[b]
    for k in range(a,b+1):
        temp2=arr[k]
        arr[k]=temp
        temp=temp2
    return (arr)

for j in range(1,len(arr)):
    for i in range(j-1,-1,-1):
        if(arr[i]<arr[j]):
            arr=rotate(arr,i+1,j)
            break
        elif(i==0):
            arr=rotate(arr,i,j)

print(arr)
