def insertion_sort(array):

    for i in range(len(array)):
        key = array[i]
        j = i - 1

        while j>=0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key
    return array

array = [21, 4, 19, 16, 54, 86, 70]
array = insertion_sort(array)

for i in range(len(array)):
    print(array[i], end=", ")