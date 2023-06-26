def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n=int(input())
x=[]
y=[]
z=[]
for i in range(1,n+1):
    t_x,t_y,t_z=map(int,input().split())
    x.append((t_x,i))
    y.append((t_y,i))
    z.append((t_z,i))
x.sort()
y.sort()
z.sort()

parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i

edges=[]
for i in range(n-1):
    edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))
edges.sort()

result=0
for e in edges:
    cost,a,b=e
    if find_parent(parent,a)!=find_parent(parent,b):
        result+=cost
        union_parent(parent,a,b)

print(result)