#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """
    list_pascal = []
    if n <= 0:
        return list_pascal
    prev_array = []

    for i in range(n):
        array = []

        if i == 0:
            list_pascal.append([1])
        elif i == 1:
            prev_array = [1, 1]
            list_pascal.append(prev_array)
        else:
            array.append(1)
            for j in range(1, i):
                array.append(prev_array[j - 1] + prev_array[j])
            array.append(1)
            list_pascal.append(array)
            prev_array = array

    return list_pascal
