import random
try:
    size = int(input("Size ->"))
    begin = int(input("Begin ->"))
    finish = int(input("Finish ->"))
    list = []
    klist = []

    for i in range(size):
        list.append(random.randint(begin, finish))

    list.sort()
    for item in list:
        print(item, end=" ")
    print()

    #dict = (f"min = {list[:1]}, max = {list[-1]}")
    #print(dict)

    for item in list:
        for j in range(1, i -1):
            if item // j:
                klist.append(item)




    #kount = len(list)
    #print()

    data = {1: lambda lst: max(lst), 2: lambda lst: min(lst), 3: lambda lst: list[::-1], 4: lambda sie: all(size % i != 0 for i in range(2, int(size ** .5) + 1))}
    print(f"max = {data[1](list)}, min = {data[2](list)}")

    #print(f"min = {data[2](list)}")
    print(data[3](list))
    print()
    print(f"easy number = {data[4](list)}")






    #lis = tuple(list)
    #print(lis[:1], lis[size - 1])
except Exception as ex:
    print(f"Error: {ex}")