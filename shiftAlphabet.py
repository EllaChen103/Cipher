def shift(alphabet, key):
    answer = []
    for element in alphabet:
        element = ord(element)
        element = element + key
        while element >= 123:
            element = element - 26
        element = chr(element)
        answer.append(element)
    return answer
print(shift(list(map(chr, range(97, 123))), int(input("What is your key?"))))
