def convertor(str1):
    vals = {"I":1,"V":5,"X":10,"XL":50,"C":100,"D":500,"M":1000}
    num = 0
    for i in range(len(str1)):
        print(vals[str1[i]])
        print(vals[str1[i-1]])
        if i > 0 and vals[str1[i]] > vals[str1[i-1]]:
            num = num + vals[str1[i]] - 2 * vals[str1[i-1]]
        else:
            num += vals[str1[i]]
    return num
str1 = input()
print(convertor(str1))
