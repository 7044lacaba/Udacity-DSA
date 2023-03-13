class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        n = Node(new_val)
        current = self.root
        while True:
            if n.value > current.value:
                # check if any values right side
                if current.right == None:
                   current.right = n
                   break
                else:
                    current = current.right
            elif n.value < current.value:
                # check if any values left side
                if current.left == None: 
                   current.left = n
                   break
                else:
                    current = current.left
            else:
                break

    def search(self, find_val):
        current = self.root
        while True:
            if find_val < current.value:
                if current.left == None:
                    break
                else:
                    current = current.left
            elif find_val > current.value:
                if current.right == None:
                    break
                else:
                    current = current.right
            else:
                return True


        return False
  
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))