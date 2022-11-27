from BinaryTree import BST, AVL
import time
import timeit
import matplotlib.pyplot as plt
import numpy as np
import sys
import random
sys.setrecursionlimit(10000)
random_num_list = [random.randint(0, 30000) for i in range(10000)]
N_list = [i*1000 for i in range(1, 11)]
print(N_list)

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
plt.show()
# plt.savefig("wykres1.png")

plt.plot(N_list,searching_tree_results[0],label='BST')
plt.plot(N_list,searching_tree_results[1],label='AVL')
plt.legend()
plt.xlabel("Długość listy")
plt.ylabel("Czas szukania")
plt.show()

plt.plot(N_list,deleting_tree_results[0],label='BST')
plt.plot(N_list,deleting_tree_results[1],label='AVL')
plt.legend()
plt.xlabel("Długość listy")
plt.ylabel("Czas usuwania")
plt.show()

# f = plt.figure()
# f.set_figwidth(16)
# f.set_figheight(12)
# f.tight_layout(pad=100.0)

# plt.subplot(221)
# plt.plot(N,Wyniki[0], color="blue")
# plt.title('Bubble')
# plt.xlabel("Długość listy")
# plt.ylabel("Czas sortowania")
# plt.grid(True)

# plt.subplot(222)
# plt.plot(N,Wyniki[1], color="orange")
# plt.title('Selection')
# plt.xlabel("Długość listy")
# plt.ylabel("Czas sortowania")
# plt.grid(True)

# plt.subplot(223)
# plt.plot(N,Wyniki[2], color="green")
# plt.title('Merge')
# plt.xlabel("Długość listy")
# plt.ylabel("Czas sortowania")
# plt.grid(True)

# plt.subplot(224)
# plt.plot(N,Wyniki[3], color="red")
# plt.title('Quick')
# plt.xlabel("Długość listy")
# plt.ylabel("Czas sortowania")
# plt.grid(True)
# # plt.show()
# plt.savefig("wykres2.png")
# plt.close()
