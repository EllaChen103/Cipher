def checksum(lst, x):
    add_to_end = 1
    while (sum(lst) + add_to_end) % x != 0:
        add_to_end += 1
    lst.append(add_to_end)
    return lst

answer = checksum(list(range(10)), int(input("What is x?")))
print(answer)

