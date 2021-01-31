#adding numbers in an array

arr=[1,2,3,4,5]
def add(arr):
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
    return sum
x=add(arr)
print(x)