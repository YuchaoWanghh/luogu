l,m=map(int,input().split())
z=[]
for i in range(m):
    z.append(list(map(int,input().split())))
road=[1]*(l+1)
for i in range(m):
    start=z[i][0]
    end=z[i][1]
    for j in range(start,end+1):
        road[j]=0
count=0
for i in range(len(road)):
    if road[i]==1:
        count+=1
print(count)