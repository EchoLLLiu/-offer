# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/20'

# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。

class TreeNode:
	'''二叉树节点的定义'''
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class OperationTree:
	'''二叉树操作'''
	def create(self, List):
		'''二叉树插入操作'''
		root = TreeNode(List[0])
		lens = len(List)
		if lens >= 2:
			root.left = self.create(List[1])
		if lens >= 3:
			root.right = self.create(List[2])
		return root

	def PreOrder(self, root):
		'''打印二叉树(先序)'''
		if root == None:
			return 
		print(root.val, end=' ')
		self.PreOrder(root.left)
		self.PreOrder(root.right)

	def TreeDepth(self, root):
		if not root:
			return 0
		left = self.TreeDepth(root.left)
		right = self.TreeDepth(root.right)
		return max(left, right) + 1

	def IsBalanced_Solution(self, pRoot):
		if not pRoot:
			return True
		child = self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right) 
		sub = abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right))
		if sub <= 1:
			return True and child 
		else: return False

if __name__ == '__main__':
	List1 = [1,[2,[4,[8],[9]],[5]],[3,[6],[7]]]
	op = OperationTree()
	tree1 = op.create(List1)
	print('先序打印：',end = '')
	op.PreOrder(tree1)
	print("")
	print(op.TreeDepth(tree1))
	print(op.IsBalanced_Solution(tree1))