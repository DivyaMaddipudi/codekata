def Repeat(lis): 
    size = len(lis) 
    repeated = [] 
    for i in range(size): 
        k = i + 1
        for j in range(k, size): 
            if lis[i] == lis[j] and lis[i] not in repeated: 
                repeated.append(lis[i]) 
    for k in repeated:
        print(k,end=" ")
n = int(input())
lis = [int(x) for x in input().split()][:n]
Repeat(lis)