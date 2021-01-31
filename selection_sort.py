arr=[4,1,3,9,7]
def find_min(arr,a,b):
    res=a
    min=arr[a]
    for i in range(a,b):
        if(arr[i]<min):
            min=arr[i]
            res=i
    return res    
def select(arr):
    for i in range(len(arr)):
        x=find_min(arr,i,len(arr))
        print(arr[x],i)
        temp=arr[x]
        arr[x]=arr[i]
        arr[i]=temp
        
    print(arr)

select(arr)