def checkSum(lst, x):
    addEnd = 1
    while (sum(lst) + addEnd) % x != 0:
        addEnd += 1
    lst.append(addEnd)
    return lst

answer = checkSum(list(range(10)), int(input("What is x?")))
print(answer)

