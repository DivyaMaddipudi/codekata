n=int(input())
lis=list(map(int,input().split()))[:n]
val=[]
count=0
for i in range(len(lis)):
    if lis[i] in val:           
        count=1                 
        val=lis[i]
        break
    else:
        val.append(lis[i])      
if count==0:
    print("unique")
else:
    print(val)
