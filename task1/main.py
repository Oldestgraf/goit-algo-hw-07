class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def search_max_value(root):
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.val

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

# Пошук значення
val =  4
result = search(root, val)
if result:
    print(f"У дереві знайдено значення {result.val}")
else:
    print(f"У дереві не знайдено значення {val}")

# Пошук найбільшого значення
max_value = search_max_value(root)
print(f"Найбільше значення у дереві: {max_value}")
