n = int(input())
lis = [int(x) for x in input().split()][:n]
val =[]
size = len(lis)
for i in range(size):
    k = i + 1
    for j in range(k, size):
        if lis[i] == lis[j] and lis[i] not in val:
            val.append(lis[i])
for i in lis:
    if i not in val:
        print(i)

        
