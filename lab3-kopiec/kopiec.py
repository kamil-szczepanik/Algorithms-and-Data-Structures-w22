import math
from random import randrange
import sys

class Heap:

  def __init__(self, arn):
    self.size = 0
    self.Heap = [0]*(100)
    self.Heap[0] = -1*sys.maxsize
    self.FRONT = 1
    self.arn = arn

  def parent(self,pos):
    return pos//self.arn
  
  def swap(self,fpos,spos):
    self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

  def insert(self, element):
    self.Heap[self.size] = element

    current = self.size
    while self.Heap[current] > self.Heap[self.parent(current)]:
      self.swap(current, self.parent(current))
      current = self.parent(current)

    self.size +=1

  def print(self):
    i = 0
    root = 0
    print(self.size)
    tab = math.floor(math.log(self.size,self.arn)) +2
    print(tab)
    print("start")
    while(i<self.size):
      j=0
      print('   '*(3**(tab-1)+tab),end='')
      while(j<math.pow(self.arn,root)):
        print(str(self.Heap[i]) + ' '*(3**(tab)) ,end='')
        if(j%3==2):
          print('||',end='')
        print(' '*(3**(tab)) ,end='')
        
        j+=1
        i+=1
        if(i==self.size):
          break
      tab-=1
      root+=1
      print("")
      print(tab)
      print(' nowa linia \n')

if __name__ == '__main__':
  heap = Heap(3)
  for i in range(20):
    heap.insert(randrange(100))

  heap.print()
  