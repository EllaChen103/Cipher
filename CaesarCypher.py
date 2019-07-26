def shift(message, key):
    answer = []
    for element in message:
        element = ord(element)
        if 97 <= element < 123:
            element = element + key
            while element >= 123:
                element = element - 26
        element = chr(element)
        answer.append(element)
    return "".join(answer)
print(shift(input("What is your message?"), int(input("What is your key?"))))
