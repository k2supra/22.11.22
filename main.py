import random
try:
    size = int(input("Size ->"))
    begin = int(input("Begin ->"))
    finish = int(input("Finish ->"))
    list = []

    for i in range(size):
        list.append(random.randint(begin, finish))

    list.sort()
    for item in list:
        print(item, end=" ")
    print()

    dict = (f"min = {list[:1]}, max = {list[-1]}")
    print(dict)

    #lis = tuple(list)
    #print(lis[:1], lis[size - 1])
except Exception as ex:
    print(f"Error: {ex}")