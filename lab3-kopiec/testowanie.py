from kopiec import MaxHeap
import timeit
import matplotlib.pyplot as plt
import sys
import random
import gc

sys.setrecursionlimit(10000)
random_num_list = [random.randint(0, 300000) for i in range(100000)]
N_list = [i*5000 for i in range(1,21)]
random_num_list = [random.randint(0, 300000) for i in range(100000)]
N_list = [i*5000 for i in range(1,21)]
print(N_list)

creating_heap_results = []
deleting_heap_results = []

gc_old = gc.isenabled() # pobierz aktualny stan odśmiecania

heap2 = MaxHeap(n=2)
heap3 = MaxHeap(n=3)
heap4 = MaxHeap(n=4)

for  num, heap in enumerate((heap2, heap3, heap4)):
    print('heap', num)
    gc.disable() # wyłącz odśmiecanie
    creating_heap_results_temp = []
    deleting_heap_results_temp = []
    for n in N_list:
        arr = random_num_list[:n]
        # Tworzenie kopca
        start = timeit.default_timer()
        for num in arr:
            heap.push(num)
        stop = timeit.default_timer()
        creating_heap_results_temp.append(stop-start)

        # Usuwanie
        start = timeit.default_timer()
        for i, num in enumerate(arr):
            heap.pop()
        stop = timeit.default_timer()
        deleting_heap_results_temp.append(stop-start)
        


    if gc_old: gc.enable() 
    # print(creating_heap_results_temp)
    creating_heap_results.append(creating_heap_results_temp)
    deleting_heap_results.append(deleting_heap_results_temp)

plt.plot(N_list,creating_heap_results[0],label='Kopiec 2-arny')
plt.plot(N_list,creating_heap_results[1],label='Kopiec 3-arny')
plt.plot(N_list,creating_heap_results[2],label='Kopiec 4-arny')
plt.legend()
plt.xlabel("Długość listy")
plt.ylabel("Czas tworzenia")
plt.grid()
# plt.show()
plt.savefig("images/tworzenie.png")
plt.close()

plt.plot(N_list,deleting_heap_results[0],label='Kopiec 2-arny')
plt.plot(N_list,deleting_heap_results[1],label='Kopiec 3-arny')
plt.plot(N_list,deleting_heap_results[2],label='Kopiec 4-arny')
plt.legend()
plt.xlabel("Długość listy")
plt.ylabel("Czas usuwania")
plt.grid()
# plt.show()
plt.savefig("images/usuwanie.png")
plt.close()
