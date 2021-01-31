#s=input()
#s="ABABABABABAB"
def dup(s):
    emp=" "
    count=0
    if(len(s)>0):
        emp=emp+s[0]
    else:
        return(count,emp)
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            count=count+1
        else:
            emp=emp+s[i+1]

    return(count,emp)
x=input()
y,z=dup(x)
print(y,z)