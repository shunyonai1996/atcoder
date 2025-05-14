import collections

Q = int(input())
S = []
c = collections.Counter(S)

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        S.append(query[1])
    elif query[0] == 2:
        min(query[2], c[query[1]])
    else:
        print(max(S) - min(S))


# 解説の回答
import heapq
from collections import defaultdict

mx=[]
mn=[]
cnt=defaultdict(int)

q=int(input())
for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        x=query[1]
        cnt[x]+=1
        heapq.heappush(mx,-x)
        heapq.heappush(mn,x)

    if query[0]==2:
        x,c=query[1:]
        cnt[x]=max(0,cnt[x]-c)

    if query[0]==3:
        while cnt[-mx[0]]==0:
        heapq.heappop(mx)
        while cnt[mn[0]]==0:
        heapq.heappop(mn)
        print(-mx[0]-mn[0])