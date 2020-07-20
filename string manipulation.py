# s11='hello! long time no talk lets meetq'
# j=0
# while j<=len(s11)+1:
#     if j==0:
#         n=s11.find('q',j)
#     else:
#         n=s11.find('q',j+1)
#     if n>0:
#         j=n
#         print(n)
#     elif n<0:
#         j=len(s11)+2
#     # else:
#     #     j=j+1
#     #     print(n)


# s11='hello! long time no talk lets meetq'
# j=0
# while j<=len(s11)+1:
#     j=s11.find('q',j)
#     if(j<0):
#         print("search done")
#         break
#     print(j)
#     j=j+1

l1='my name is mounika and i am 20 years old and young'.split()
l2='the temperature in degrees can be two types'.split()
def manipulation(s1):
    empty_string=''
    for i in range(len(s1)):
        empty_string=empty_string+s1[i]+' '
        if((i+1)%4==0) and i<len(s1)-1:
            empty_string=empty_string+'-'
    print(s1)
    print(empty_string)

manipulation(l1)
manipulation(l2)

# def funct(a,b):
    
#     return a+b

# print(funct(8,10))
# print(funct(7,3))

def multiply(x,a):
    for i in range(a+1):
        print(x*i)
        

y=int(input())
z=int(input())
result=multiply(y,z)
print(result)