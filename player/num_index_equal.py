n = int(input())
lis = [int(x) for x in input().split()][:n]
size = len(lis)
for i in range(size):
    if i == lis[i]:
        print(lis[i],end=" ")
