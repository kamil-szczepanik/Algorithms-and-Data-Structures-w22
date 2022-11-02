def selection_sort(array):
    
    for i in range(len(array)):
        lowest = i
        for j in range(i+1, len(array)):
            if array[lowest]>array[j]:
                lowest = j

        temp = array[i] 
        array[i] = array[lowest]
        array[lowest] = temp
        print(array)

    return array

def merge_sort(array):
    if len(array)>1:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = 0
        j = 0
        k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

    return array
