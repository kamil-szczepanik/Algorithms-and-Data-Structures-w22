import random
import numpy as np


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 1

    def get_level_order(self, root):
        h = root.height
        level_list = []
        for i in range(1, h+1):
            level_list.append(self.get_current_level(root, i))
        return level_list
    
    
    # Print nodes at a current level
    def get_current_level(self, root, level):
        if root is None:
            return 
        if level == 1:
            curr_level= root.data
        elif level > 1:
            l = self.get_current_level(root.left, level-1)
            r = self.get_current_level(root.right, level-1)
            curr_level = l,r

        return curr_level

    def print_tree(self, root):
        print('------------')
        level_list = self.get_level_order(root)
        tree_height = len(level_list)
        width = np.power(2, tree_height)
        
        for i in range(1, len(level_list)+1):
            print(i)
            width = width//2
            indent =  (width-1)*"    "
            to_print = self.print_level_list("", level_list[i-1], i, width, tree_height, indent)
            print(to_print)
            

    def print_level_list(self, text, level_list, dim, width, tree_height, indent):
        if level_list is None:
                return indent  +  "____"
        if dim == 1:
            if level_list is None:
                return indent  +  "____"
            else:
                return indent  + (4-len(str(level_list)))*" " +str(level_list)
        else:
            # if level_list[0] is not None and level_list[1] is not None:
            text+=  self.print_level_list(text, level_list[0], dim-1, width, tree_height, indent) + indent + "    " + self.print_level_list(text, level_list[1], dim-1, width, tree_height, indent) 
        return text


    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = f"{self.data}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data, end=" < ")
        if self.right:
            self.right.PrintTree()


class BST():
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)

        root.height = 1 + max(self.get_height(root.left),
                        self.get_height(root.right))
        return root

    def find_most_left(self, root):
        if root is None or root.left is None:
            return root
        return self.find_most_left(root.left)

    def search(self, data):
        return self._search(self.root, data)
    
    def _search(self, root, data):
        if not root:
            return root
        if root.data == data:
            return root
        if data < root.data:
            return self._search(root.left, data)
        if data > root.data:
            return self._search(root.right, data)

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, root, data):
        if not root:
            return root
        if data < root.data:
            root.left = self._delete(root.left, data)
        elif data > root.data:
            root.right = self._delete(root.right, data)
        else:
            if root.left is None:
                root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))     
                return root.right
            if root.right is None:
                root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))  
                return root.left
            
            most_left_root = self.find_most_left(root.right)
            root.data = most_left_root.data
            root.right = self._delete(root.right, root.data)   

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))         
        
        return root

    def get_height(self, root):
        if not root:
            return 0
        return root.height


class AVL(BST):
    def __init__(self):
        super().__init__()

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def display(self):
        self.root.display()

    def insert(self,data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        root = super()._insert(root, data)

        balance = self.get_balance(root)

        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotation(root)
            else:
                root.left = self.left_rotation(root.left)
                return self.right_rotation(root)

        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotation(root)
            else:
                root.right = self.right_rotation(root.right)
                return self.left_rotation(root)

        return root

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, root, data):
        root = super()._delete(root, data)

        balance = self.get_balance(root)

        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotation(root)
            else:
                root.left = self.left_rotation(root.left)
                return self.right_rotation(root)

        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotation(root)
            else:
                root.right = self.right_rotation(root.right)
                return self.left_rotation(root)

        return root

 
    def left_rotation(self, z):
 
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left),
                         self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                         self.get_height(y.right))

        return y
 
    def right_rotation(self, z):
 
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left),
                        self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                        self.get_height(y.right))

        return y


if __name__ == '__main__':
    bst_tree = BST()
    avl_tree = AVL()
    for i in range(8):
        intTemp = random.randint(1,10000)
        if i == 3:
            x = intTemp
        bst_tree.insert(intTemp)
        avl_tree.insert(intTemp)


    print("BST: \n")
    # bst_tree.root.display()
    bst_tree.root.print_tree(bst_tree.root)
    print('to be deleted: ', x)
    print("Searching: ", x, " - result: ", bool(bst_tree.search(x)))
    print("Searching: ", 1111, " - result: ", bool(bst_tree.search(1111)))
    bst_tree.delete(x)
    print('height: ', bst_tree.get_height(bst_tree.root))
    # bst_tree.root.display()

    print("==================\nAVL: \n")
    # avl_tree.root.display()
    print("Searching: ", x, " - result: ", bool(avl_tree.search(x)))
    print("Searching: ", 1111, " - result: ", bool(avl_tree.search(1111)))
    print('to be deleted: ', x)
    avl_tree.delete(x)
    print('height: ', avl_tree.get_height(avl_tree.root))
    print('balance: ', avl_tree.get_balance(avl_tree.root))
    # avl_tree.root.display()
    avl_tree.root.print_tree(avl_tree.root)


    # avl_tree.root.PrintTree()
