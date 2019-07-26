def addShift(lst, key):
    answer = []
    for element in lst:
        element = element + key
        while element >= 10:
            element = element - 10
        answer.append(element)
    return answer
print(addShift([21, 3, 51, 16, 2, 45], key = int(input("What is your key?"))))
