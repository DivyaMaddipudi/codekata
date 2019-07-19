n = int(input())
lis = [int(x) for x in input().split()][:n]
size = len(lis)
val = []
for i in range(size):
    if i == lis[i]:
        val.append(lis[i])
w = len(val)
if w == 0:
    print("-1")
else:
    for i in val:
        print(i,end=" ")
    
