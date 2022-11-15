from algorithms import selection_sort, merge_sort, bubbleSort, quickSort
from utils import get_N_words_from_file
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.setrecursionlimit(10000)
N = [100, 500, 1000, 2000, 3000, 5000, 10000, 15000]
Wyniki = []
import gc
gc_old = gc.isenabled() # pobierz aktualny stan odśmiecania

for i in range(1,5):
  gc.disable() # wyłącz odśmiecanie
  print(i)
  wynikiTemp = []
  for n in N:
    arr = get_N_words_from_file('pan-tadeusz.txt', n)
    start = time.process_time() # pobierz aktualny czas
    if(i==1):
      bubbleSort(arr)
    elif(i==2):
      selection_sort(arr)
    elif(i==3):
      merge_sort(arr)
    else:
        quickSort(arr,0,len(arr)-1)
    stop = time.process_time()
    wynikiTemp.append(stop-start)
  if gc_old: gc.enable() 
  print(wynikiTemp)
  Wyniki.append(wynikiTemp)
print(Wyniki)
plt.plot(N,Wyniki[0],label='Bubble')
plt.plot(N,Wyniki[1],label='Selection')
plt.plot(N,Wyniki[2],label='Merge')
plt.plot(N,Wyniki[3],label='Quick')
plt.legend()
plt.xlabel("Długość listy")
plt.ylabel("Czas sortowania")
# plt.show()
plt.savefig("wykres1.png")
plt.close()

f = plt.figure()
f.set_figwidth(16)
f.set_figheight(12)
f.tight_layout(pad=100.0)

plt.subplot(221)
plt.plot(N,Wyniki[0], color="blue")
plt.title('Bubble')
plt.xlabel("Długość listy")
plt.ylabel("Czas sortowania")
plt.grid(True)

plt.subplot(222)
plt.plot(N,Wyniki[1], color="orange")
plt.title('Selection')
plt.xlabel("Długość listy")
plt.ylabel("Czas sortowania")
plt.grid(True)

plt.subplot(223)
plt.plot(N,Wyniki[2], color="green")
plt.title('Merge')
plt.xlabel("Długość listy")
plt.ylabel("Czas sortowania")
plt.grid(True)

plt.subplot(224)
plt.plot(N,Wyniki[3], color="red")
plt.title('Quick')
plt.xlabel("Długość listy")
plt.ylabel("Czas sortowania")
plt.grid(True)
# plt.show()
plt.savefig("wykres2.png")
plt.close()
