class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(n):
    return n.height if n else 0


def update(n):
    n.height = 1 + max(height(n.left), height(n.right))


def balance(n):
    return height(n.left) - height(n.right)


def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    update(y)
    update(x)
    return x


def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    update(x)
    update(y)
    return y


def insert(n, key):
    if n is None:
        return Node(key)

    if key < n.key:
        n.left = insert(n.left, key)
    else:
        n.right = insert(n.right, key)

    update(n)
    b = balance(n)

    if b > 1 and key < n.left.key:
        print(f"Right rotation at {n.key} (LL case)")
        return rotate_right(n)

    if b < -1 and key > n.right.key:
        print(f"Left rotation at {n.key} (RR case)")
        return rotate_left(n)

    if b > 1 and key > n.left.key:
        print(f"Left-Right rotation at {n.key} (LR case)")
        n.left = rotate_left(n.left)
        return rotate_right(n)

    if b < -1 and key < n.right.key:
        print(f"Right-Left rotation at {n.key} (RL case)")
        n.right = rotate_right(n.right)
        return rotate_left(n)

    return n


def inorder(n):
    return inorder(n.left) + [n.key] + inorder(n.right) if n else []


def preorder(n):
    return [n.key] + preorder(n.left) + preorder(n.right) if n else []


root = None

for k in [10, 20, 30, 40, 50, 25]:
    print("Insert", k)
    root = insert(root, k)
    print("Inorder :", inorder(root))
    print("Preorder:", preorder(root))
    print("Root:", root.key, "| height:", root.height)
