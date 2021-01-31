#Dijkstra's Algorithm

graph=[[0,7,9,0,0,14],[7,0,10,15,0,0],[9,10,0,11,0,2],[0,15,11,0,6,0],[0,0,0,6,0,9],[14,0,2,0,9,0]]
V=len(graph)
src=int(input())
d(src)=0
d=[sys.maxint]*V
visited=[False]*V 
for i in range(V):
    u=minDistance(d,visited)        #current vertex
    visited[u]=True
    for j in range(V):
        if(visited[j]==False and d[u]+graph[u][j]<d[j] and graph[u][j]>0):
            d[j]=d[u]+graph[u][j]
print(d)



def minDistance(dist,visited):
    min=sys.maxint
    for v in range(len(dist)):
        if(dist[v]<min and dist[v]==False):
            min=dist[v]
            min_index=v 
    return min_index