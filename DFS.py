#DFS algorithm


n=int(input())
graph={}
for i in range(n):
    lst=list(input().split(" "))
    
    emp_lst=[]
    for k in lst:
        emp_lst.append(int(k))
    graph[i]=emp_lst
print(graph)


def dfs(graph,m):
    stack=[]
    visited=[]
    stack.append(m)
    visited.append(m)
    while stack:
        k=stack.pop()
        result=k 
        print(result, end=" ")
        for j in graph[k]:
            if j not in visited:
                stack.append(j)
                visited.append(j)
dfs(graph,0)