#find if a number is present in an array
arr=[4,6,1,8,7,10,15,3,2,11,19,18,13]
def ele_present(arr,a):
    if a in arr:
        return True
    else:
        return False
x=ele_present(arr,11)
print(x)

#method_2
arr=[4,6,1,8,7,10,15,3,2,11,19,18,13]
def ele_present(arr,a):
    for k in arr:
        if(k==a):
            return True
        # else:
        #     return False
    return False

x=ele_present(arr,11)
print(x)