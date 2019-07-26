def shift(message, key):
    answer = []
    for element in message:
        element = ord(element)
        element = element ^ key
        element = chr(element)
        answer.append(element)
    return "".join(answer)


#to encode
print(shift(input("What is your message?"), int(input("What is your key?"))))
#to decode
print(shift("lrwwb;rh;i~zwwb;yz ;zo;osrh", 27))