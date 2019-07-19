p=list(map(str,input()))
m=n=0
for i in range(0,len(p)-1):
  q=p[i]
  if int(q)!=0:
   for j in range(i+1,i+2):
    q=q+p[j]
    if int(q)<27 and int(q)>0:
        n=n+1
    elif int(q)==0: 
        n=n-1
    else: 
        break
if n!=1: 
    m=n%2
print(n+m+1)