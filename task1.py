array = []
e = int(input("enter first number: "))
d = int(input("enter difference: "))
a = int(input("enter amount of elements: "))



array.append(e)

for i in range (2, a+1):
    array.append(e+((i-1)*d))

print(array)





