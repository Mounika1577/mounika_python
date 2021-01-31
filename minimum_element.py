#find minimum element in an array
arr=[4,6,1,8,7]
def min(arr):
    min=1000000
    for i in range(len(arr)):
        if(arr[i]<min):
            min=arr[i]
    return min
x=min(arr)
print(x)
