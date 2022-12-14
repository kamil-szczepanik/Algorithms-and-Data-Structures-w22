import math
import random
from io import StringIO

class MaxHeap:

    def __init__(self, n):
        self.T = []
        self.n = n
    
    def size(self): return len(self.T)

    def parent(self,k): return (k-1)//self.n

    def child(self, index, position):
        return index*self.n + (position+1)

    def get(self, k):
        return self.T[k]

    def get_max(self):
        if self.size() == 0:
            return None
        return self.T[0]

    def down_heap(self, k): # max heapify
        biggest = k
        for i in range(self.n):
            child = self.child(k, i)
            if (child < self.size() and self.get(child) > self.get(biggest)):
                biggest = child
        if (biggest != k):
            self.swap(biggest, k)
            self.down_heap(biggest)

    def pop(self):
        if self.size() == 0:
            return None
        biggest = self.get_max()
        self.T[0] = self.T[-1]
        del self.T[-1]
        self.down_heap(0)
        return biggest
    
    def swap(self, k, j):
        self.T[k], self.T[j] = self.T[j], self.T[k]

    def up_heap(self, k):
        while (k != 0):
            parent_idx = self.parent(k)
            if self.get(parent_idx) < self.get(k):
                self.swap(parent_idx, k)
            k = parent_idx

    def push(self, element):
        element_idx = self.size()
        self.T.append(element)
        self.up_heap(element_idx)

    def print(self):
        width = (self.n+3)*len(self.T)
        output = StringIO()
        last_row = -1

        for i, num in enumerate(self.T):
            if i:
                row = int(math.floor(math.log((self.n-1)*i+1, self.n)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = self.n**row
            col_width = int(math.floor((width * 1.0) / columns))
            output.write(str(num).center(col_width, " "))
            last_row = row
        print (output.getvalue())
        print ('=' * width)

if __name__ == '__main__':
    heap2 = MaxHeap(n=2)
    heap3 = MaxHeap(n=3)
    heap4 = MaxHeap(n=4)
    num_of_elements = 18
    random_num_list = [random.randint(0, 99) for i in range(num_of_elements)]
    for num in random_num_list:
        heap2.push(num)
        heap3.push(num)
        heap4.push(num)
    # print(heap2.pop())
    print(' - Heap 2-ary')
    print("Number of elements:", num_of_elements)
    heap2.print()
    print(' - Heap 3-ary')
    print("Number of elements:", num_of_elements)
    heap3.print()
    print(' - SHeap 4-ary')
    print("Number of elements:", num_of_elements)
    heap4.print()
    