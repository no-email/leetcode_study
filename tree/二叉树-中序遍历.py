# -*- coding: utf-8 -*-
# @Author  : loubeibei
# @Time    : 2024/3/26 09:49

class TreeNode:
    def __init__(self,val,left=None,rigth=None):
        self.val = val
        self.right = rigth
        self.left = left

def inorderTraversal(root:TreeNode):
    res = []
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
    inorder(root)
    return res

def inorderTraversal1(root:TreeNode):
    if not root:
        return []
    res = []
    stack = []

    while root or stack:            #跟节点或栈不为空
        while root:
            stack.append(root)      #将当前根节点入栈
            root = root.left        #找到最左侧讲诶点
        node = stack.pop()          #遍历到最左侧，当前节点无左自节点时，将节点弹出

        res.append(node.val)        #访问该节点
        root = node.right           #尝试访问该节点的右子树
    return res