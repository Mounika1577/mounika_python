
def rotate(arr,m,n):
    temp=arr[m]
    for i in range(m,n-1,-1):
        arr[i]=arr[i-1]
    arr[n]=temp
    return arr

arr=[1,4,3,5,6,2]
for i in range(1,len(arr)):
    for j in range(i):
        if(arr[j]>arr[i]):
            arr=rotate(arr,i,j)
    print(arr)