import random


class Node:
  def __init__(self,data):
    self.left = None
    self.right = None
    self.data = data

  def insert(self,data):
    if self.data:
      if data < self.data:
        if self.left is None:
          self.left = Node(data)
        else:
          self.left.insert(data)
      elif data > self.data:
        if self.right is None:
          self.right = Node(data)
        else:
          self.right.insert(data)
    else:
      self.data = data


  def PrintTree(self):
    if self.left:
      self.left.PrintTree()
    print(self.data, end=" < ")
    if self.right:
      self.right.PrintTree()

if __name__ == '__main__':
  root = Node(5000)
  for i in range(100):
  
    intTemp = random.randint(1,10000)
    root.insert(intTemp)
  root.PrintTree()