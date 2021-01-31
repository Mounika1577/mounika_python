#find maximum element's index between two given indices
arr=[4,6,1,8,7,10,15,3,2,11,19,18,13]
def max_index(arr,a,b):
    max=-1
    for i in range(a,b):
        if(arr[i]>max):
            max=arr[i]
            index=i
            break
    return index
d=max_index(arr,5,12)
print(d)