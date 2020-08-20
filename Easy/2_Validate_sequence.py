import sys
N = list(map(int,input().split()))
M = list(map(int,input().split()))

n = len(N)
m = len(M)

i=0
j=0
while i<m and j<n:
    num = M[i]
    if num==N[j]:
        i+=1
    j+=1
if i!=m:
    print(False)
else:
    print(True)
    
    
    