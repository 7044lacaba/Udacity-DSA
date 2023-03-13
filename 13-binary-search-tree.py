class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        
        current = self.root

        if new_val > current.value:

            # check if any values right side
            # if current.right = None 
            #   current.right = new_val
            #   break
            # else current = current.right

            pass

        elif new_val < current.value:

            # check if any values left side
            # if current.left = None 
            #   current.left = new_val
            #   break
            # else current = current.left
            pass

        else:
            pass

    def search(self, find_val):
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