"""implementing bubble  sorting algorithm for sorting officer Azampay(sarafu)"""


def b_sorting(array):
    def swapping(i, j):
        array[i], array[j] = array[j], array[i]

    n = len(array)
    swapped = True

    x = -1
    while swapped:
        x = x + 1
        swapped = False

        for i in range(1, n):
            if array[i-1] > array[i]:
                swapping(i-1,i)
                swapped = True
    return array

"""implementing selection sorting"""

def selection_sorting(array):
    for i in range(len(array)):
        minimum = i

        for j in range(i+1,len(array)):
            if array[j] < array[minimum]:
                minimum = j

        array[minimum], array[i] = array[i],array[minimum]
    return array

print(selection_sorting([1,4,42,432,2,43,34]))



