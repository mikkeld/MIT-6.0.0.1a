L = [[0, 1, 2], [1, 2, 3]]
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    reversedList = [None] * len(L)
    for i in range(len(L)):
        reversedList[len(L)-i-1]=(list(reversed(L[i])))

    L = []
    L.append(reversedList)

print(deep_reverse(L))
print(L)




