def selection_sort(array):

    for i in range(len(array)):

        min_index = i

        for j in range(i, len(array)):
            if array[min_index] > array[j]:
                min_index = j
    
        array[i], array[min_index] = array[min_index], array[i]

    return array

array = [21, 4, 19, 16, 54, 86, 70]
array = selection_sort(array)

for i in range(len(array)):
    print(array[i], end=", ")