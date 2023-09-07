def func_input(n):
    list =  []
    for i in range(int(n)):
        buffer = int(input("enter element: "))
        list.append(buffer)
    return list



n = int(input("enter length of list: "))
a = int(input("enter min value: "))
b = int(input("enter max value: "))
index_list = []

# list = [1, 5, 7, 91, -39, 85, 38, 12, -87, 0, 8, 3, 15]   #output: 2, 6, 7, 10, 12
# a = 7
# b = 40


if a > b :
    temp = a
    a = b
    b = temp

list = func_input(n)
#print(list)

for i in range (len(list)):
    if ((list[i] <= b) and (list[i] >= a)):
        index_list.append(i)

print(index_list)
