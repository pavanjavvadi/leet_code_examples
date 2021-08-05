def bubble_sort(array):

    l = len(array)
    for i in range(l-1, 0, -1):
        for j in range(0, i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1]= array[j + 1], array[j]
    
    return array

array = [21, 4, 19, 16, 54, 86, 70]
array = bubble_sort(array)

for i in array:
    print(i, end=", ")