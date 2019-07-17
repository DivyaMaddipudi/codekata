num1, num2 = [int(x) for x in input().split()]
y = []
z=[]
count = 0
val = 0
for num in range(num1, num2):
    if num > 1:  
        for i in range(2,num2):
            if num%i == 0:
                break
            else:
                z.append(num)
print(z)