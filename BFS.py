n=int(input())
graph={}
for i in range(n):
    lst=list(input().split(" "))
    
    emp_lst=[]
    for k in lst:
        emp_lst.append(int(k))
    graph[i]=emp_lst
print(graph)


def bfs(graph,m):
    queue=[]
    visited=[]
    queue.insert(0,m)
    visited.append(m)
    while queue:
        k=queue.pop()
        result=k 
        print(result, end=" ")
        for j in graph[k]:
            if j not in visited:
                queue.insert(0,j)
                visited.append(j)
bfs(graph,0)