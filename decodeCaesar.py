from CaesarCypher import shift

def decode(message):
    for key in range(0,26):
        print(shift(message, key))

decode(shift(input("What do you want to decode?"), 10))