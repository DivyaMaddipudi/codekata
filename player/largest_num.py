n = int(input())
lis = [int(x) for x in input().split()][:n]
lis.sort(reverse = True)
for i in lis:
    print(i,end="")
