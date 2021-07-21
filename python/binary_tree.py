class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def binary_tree(arr):
    if len(arr) == 0:
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = binary_tree(arr[:mid])
    root.right = binary_tree(arr[mid+1:])
    return root
