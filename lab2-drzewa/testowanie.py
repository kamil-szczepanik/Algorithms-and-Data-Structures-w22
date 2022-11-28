from BinaryTree import BST, AVL
import time
import timeit
import matplotlib.pyplot as plt
import numpy as np
import sys
import random
sys.setrecursionlimit(10000)
random_num_list = [random.randint(0, 30000) for i in range(10000)]
N_list = [i*250 for i in range(1,41)]
# print(N_list)

creating_tree_results = []
searching_tree_results = []
deleting_tree_results = []
import gc
gc_old = gc.isenabled() # pobierz aktualny stan odśmiecania

bst_tree = BST()
avl_tree = AVL()

for  tree in (bst_tree, avl_tree):
    gc.disable() # wyłącz odśmiecanie
    creating_tree_results_temp = []
    searching_tree_results_temp = []
    deleting_tree_results_temp = []
    for n in N_list:
        arr = random_num_list[:n]
        # Tworzenie drzewa
        start = timeit.default_timer()
        for num in arr:
            tree.insert(num)
        stop = timeit.default_timer()
        creating_tree_results_temp.append(stop-start)

        # Szukanie
        start = timeit.default_timer()
        for num in arr:
            tree.search(num)
        stop = timeit.default_timer()
        searching_tree_results_temp.append(stop-start)

        # Usuwanie
        start = timeit.default_timer()
        for num in arr:
            tree.delete(num)
        stop = timeit.default_timer()
        deleting_tree_results_temp.append(stop-start)


    if gc_old: gc.enable() 
    # print(creating_tree_results_temp)
    creating_tree_results.append(creating_tree_results_temp)
    searching_tree_results.append(searching_tree_results_temp)
    deleting_tree_results.append(deleting_tree_results_temp)

plt.plot(N_list,creating_tree_results[0],label='BST')
plt.plot(N_list,creating_tree_results[1],label='AVL')
plt.legend()
plt.xlabel("Długość listy")
plt.ylabel("Czas tworzenia")
plt.grid()
# plt.show()
plt.savefig("tworzenie.png")
plt.close()


plt.plot(N_list,searching_tree_results[0],label='BST')
plt.plot(N_list,searching_tree_results[1],label='AVL')
plt.legend()
plt.xlabel("Długość listy")
plt.ylabel("Czas szukania")
plt.grid()
# plt.show()
plt.savefig("szukanie.png")
plt.close()

plt.plot(N_list,deleting_tree_results[0],label='BST')
plt.plot(N_list,deleting_tree_results[1],label='AVL')
plt.legend()
plt.xlabel("Długość listy")
plt.ylabel("Czas usuwania")
plt.grid()
# plt.show()
plt.savefig("usuwanie.png")
plt.close()
