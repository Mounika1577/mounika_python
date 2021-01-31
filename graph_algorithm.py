n=int(input())
graph={}
for i in range(n):
    lst=list(input().split(" "))
    
    emp_lst=[]
    for k in lst:
        emp_lst.append(int(k))
    graph[i]=emp_lst
print(graph)

#m=int(input())                 to print the adjacent nodes of vertex m
#r=int(input())
#if r in graph[m]:
#	print["True"]
#else:
#	print["False"]
#print(graph[m])
	
