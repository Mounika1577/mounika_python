lst=input()
index=input()
list_splt=list(map(int,lst.split()))
index_splt=list(map(int,index.split()))
a=index_splt[0]
b=index_splt[1]
list_splt[b],list_splt[a]=list_splt[a],list_splt[b]
#list_splt[a]=list_splt[b]

print(list_splt)    