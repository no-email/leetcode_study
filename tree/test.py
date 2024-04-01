# -*- coding: utf-8 -*-
# @Author  : loubeibei
# @Time    : 2024/3/27 17:25
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root):
    if root is None:
        return []

    result = []
    stack = []
    current_node = root

    while current_node is not None or stack:
        while current_node is not None:
            result.append(current_node.val)
            stack.append(current_node)
            current_node = current_node.left

        current_node = stack.pop()
        current_node = current_node.right

    return result

# 示例用法
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

result = preorder_traversal(root)
print(result)
