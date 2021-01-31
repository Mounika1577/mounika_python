#adding numbers in an array

# arr=[1,2,3,4,5]
# def add(arr):
#     sum=0
#     for i in range(len(arr)):
#         sum=sum+arr[i]
#     return sum
# x=add(arr)
# print(x)

# #find minimum element in an array
# arr=[4,6,1,8,7]
# def min(arr):
#     min=1000000
#     for i in range(len(arr)):
#         if(arr[i]<min):
#             min=arr[i]
#     return min
# x=min(arr)
# print(x)

# #find maximum element's index between two given indices
# arr=[4,6,1,8,7,10,15,3,2,11,19,18,13]
# def max_index(arr,a,b):
#     max=-1
#     for i in range(a,b):
#         if(arr[i]>max):
#             max=arr[i]
#             index=i
#             break
#     return index
# d=max_index(arr,5,12)
# print(d)

#find if a number is present in an array
# arr=[4,6,1,8,7,10,15,3,2,11,19,18,13]
# def ele_present(arr,a):
#     if a in arr:
#         return True
#     else:
#         return False
# x=ele_present(arr,11)
# print(x)

#method_2
# arr=[4,6,1,8,7,10,15,3,2,11,19,18,13]
# def ele_present(arr,a):
#     for k in arr:
#         if(k==a):
#             return True
#         # else:
#         #     return False
#     return False

# x=ele_present(arr,11)
# print(x)

# arr=[1,2,3,4,5,6]
# def rotate_left(arr):
#     for i in range(len(arr)-1):
#         temp=arr[i-1]
#         arr[i-1]=arr[i]
#         #arr[i]=arr[i+1]
#         arr[i]=temp
#     return arr
# arr=rotate_left(arr)
# print(arr)

