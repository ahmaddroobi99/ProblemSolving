class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert
# a new node with the given key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


# A utility function to do inorder tree traversal


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# A utility function to search a given key in BST
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root

    # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)
# Driver program to test the above functions
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80
def deleteNode(root, key):
    # Base Case
    if root is None:
        return root

    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)

    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif (key > root.key):
        root.right = deleteNode(root.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's
        # content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree"
)
inorder(root)

print
"\nDelete 20"
root = deleteNode(root, 20)
print
"Inorder traversal of the modified tree"
inorder(root)

print
"\nDelete 30"
root = deleteNode(root, 30)
print
"Inorder traversal of the modified tree"
inorder(root)

print
"\nDelete 50"
root = deleteNode(root, 50)
print
"Inorder traversal of the modified tree"
inorder(root)