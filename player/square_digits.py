num = int(input())
val = 0
while(num > 0):
    rem = num % 10
    val = val  + (rem*rem)
    num = num//10
print(val)