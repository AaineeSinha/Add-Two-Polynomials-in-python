n1=int(input())
p1=list(map(int,input().split()))
n2=int(input())
p2=list(map(int,input().split()))
m=max(n1,n2)
res=[0]*m
for i in range(n1):res[m-n1+i]+=p1[i]
for i in range(n2):res[m-n2+i]+=p2[i]
print(*res)
