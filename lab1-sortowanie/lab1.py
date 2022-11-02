from algorithms import selection_sort, merge_sort, bubbleSort, quickSort



def get_N_words_from_file(filename, N):

    with open(filename,'r', encoding='utf8', errors='ignore') as file:
        
        array = [None] * N

        index = 0
        for line in file:
            for word in line.split():
                array[index] = word#''.join([i for i in word if i.isalpha()])
                index += 1
                if index +1 == N:
                    return array


arr = get_N_words_from_file('pan-tadeusz.txt', 50)
print(arr)

