# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/5/15'

# 依据二叉树的前序遍历和中序遍历，重建树

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
        	return
        root = TreeNode(pre[0])
        rootIndex = tin.index(root.val)
        # 左右孩子列表长度
        # leftLen = len(tin[:rootIndex])
        # rightLen = len(tin[rootIndex+1:])
        #print(leftLen, rightLen)
        root.left = self.reConstructBinaryTree(pre[1:rootIndex+1], tin[:rootIndex])
        root.right = self.reConstructBinaryTree(pre[rootIndex+1:], tin[rootIndex+1:])
        # 重点！！！
        return root

    def printPreTree(self, root):
    	if root == None:
    		return
    	print(root.val, end = " ")
    	self.printPreTree(root.left)
    	self.printPreTree(root.right)   	

if __name__ == '__main__':
	pre = [1,2,4,7,3,5,6,8]
	tin = [4,7,2,1,5,3,8,6]
	s = Solution()
	root = s.reConstructBinaryTree(pre, tin)
	#print(root.val)
	s.printPreTree(root)
