"""implementing sorting algorithm for sorting officer Azampay(sarafu)"""


def b_sorting(array):
    def swapping(i, j):
        array[i], array[j] = array[j], array[i]

    n = len(array)
    swapped = True

    x = -1
    while swapped:
        x = x + 1
        swapped = False

        for i in range(1, n-x):
            if array[i-1] > array[i]:
                swapping(i-1,i)
                swapped = True
    return array

