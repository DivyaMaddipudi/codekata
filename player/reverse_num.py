def reverse(num):
    val = 0
    while(num>0):
        rem = num%10
        val = val * 10 + rem
        num = num//10
    return val
num = int(input())
print(reverse(num))
