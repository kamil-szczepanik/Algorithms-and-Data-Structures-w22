from algorithms import selection_sort, merge_sort, bubbleSort, quickSort



def get_N_words_from_file(filename, N):

    with open(filename,'r', encoding='utf8', errors='ignore') as file:
        
        array = [None] * N

        index = 0
        for line in file:
            for word in line.split():
                array[index] = ''.join([i for i in word if i.isalpha()])
                if array[index] != '':
                    index += 1
                if index == N:
                    return array


arr = get_N_words_from_file('pan-tadeusz.txt', 50)


quickSort(arr, 0, len(arr)-1)
print(arr)

