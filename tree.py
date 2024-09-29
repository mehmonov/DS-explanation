class Node:
    def __init__(self, key):
        self.left = None  # Chap bolaga ishora
        self.right = None  # O'ng bolaga ishora
        self.value = key  # Node qiymati

class BinaryTree:
    def __init__(self):
        self.root = None  # Daraxtning ildizini belgilash

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)

    def display_inorder(self):
        result = []
        self.inorder_traversal(self.root, result)
        print("Inorder traversal:", result)

# Binary tree yaratish va ma'lumot qo'shish
bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(20)
bt.insert(3)
bt.insert(7)
bt.insert(15)
bt.insert(30)

# Binary tree'ni inorder traversal orqali ko'rsatish
bt.display_inorder()