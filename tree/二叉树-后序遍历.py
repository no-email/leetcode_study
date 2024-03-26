# -*- coding: utf-8 -*-
# @Author  : loubeibei
# @Time    : 2024/3/26 10:38

class TreeNode:
    def __init__(self,val,left=None,rigth=None):
        self.val = val
        self.left = left
        self.right = rigth

def postorderTraversal(root:TreeNode):
    res = []
    def postorder(root):
        if not root:
            return
        postorder(root.left)
        postorder(root.rigth)
        res.append(root.val)
    postorder(root)
    return res


def postorderTraversal(root:TreeNode):
    res = []
    stack = []
    prev = None                                 #保存前一个访问的节点,用于确定当前节点的右子树是否访问完毕
    while root or stack:                        #根节点或者栈不为控
        while root:
            stack.append(root)                  #将当前树的根节点入栈
            root = root.left                    #继续访问左子树\找到最左侧节点
        node = stack.pop()                      #遍历到最左侧,当前节点无左子树时,将最左侧节点谭树
        #如果当前节点无右子树或者右子树访问完毕
        if not node.right or node.right ==prev:
            res.append(node.val)    #访问该节点
            prev = node             #记录前一节点
            root = None             #将当前节点标记为控
        else:
            stack.append(node)      #右子树尚未访问完毕,将当前节点重新压回栈中
            root = node.right       #继续访问右子树
    return res