# -*- coding: utf-8 -*-
# @Author  : loubeibei
# @Time    : 2024/3/26 09:27

class TreeNode:
    def __int__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def preorderTraversal(root):
    res = []
    def preorder(root):
        if not root:
            return
        res.append(root.val)
        preorder(root.left)
        preorder(root.right)
    preorder(root)
    return res


#栈 后入先出，
def preorderTraversal1(root):
    if not root:
        return []
    res = []
    stack = [root]
    while stack:            #栈不为空
        node = stack.pop()  #弹出跟节点
        res.append(node.val)        #访问跟节点
        if node.right:
            stack.append(node.right)    #游节点入栈
        if node.left:
            stack.append(node.left) #左节点入栈
    return res



def preTraversal(root):
    res = []
    def Traversal(root):
        if not root:
            return
        res.append(root.val)
        Traversal(root.left)
        Traversal(root.right)
    Traversal(root)
    return res
def preTraversal2(root):
    res = []
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res
