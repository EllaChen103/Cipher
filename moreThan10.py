def moreThan10 (lst):

    alphabet = list(map(chr, range(97, 123)))
    print(alphabet)

    for element in lst:
        if element > 10 and element%2 == 0:
            print(element)


moreThan10([20,3,30,23, 35, 8])