# coding=utf-8

__author__ = 'LY'
__time__ = '2018/7/12'

# 给定一颗二叉搜索树，请找出其中的第k小的结点。例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。
# 思路：中序遍历存储二叉搜索树，返回第k-1个节点

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class OperationTree:
	'''二叉搜索树操作'''
	def insert(self, root, val):
		'''二叉搜索树插入操作'''
		if root == None:
			root = TreeNode(val)
		elif val < root.val:
			root.left = self.insert(root.left, val)
		elif val > root.val:
			root.right = self.insert(root.right, val)
		return root

	def printTree(self, root):
		# 打印二叉搜索树(中序打印，有序数列递增)
		if root == None:
			return 
		self.printTree(root.left)
		print(root.val, end = ' ')
		self.printTree(root.right)

class Solution:
	# 返回对应节点TreeNode
	def __init__(self):
		self.tree = []

	def KthNode(self, pRoot, k):
		if k <= 0 or (pRoot==None):
			return None

		self.midTree(pRoot)
		if len(self.tree) < k:
			return None
		return self.tree[k-1] 

	def midTree(self, pRoot):
		if not pRoot:
			return None
		self.midTree(pRoot.left)
		self.tree.append(pRoot.val)
		self.midTree(pRoot.right)
 


if __name__ == '__main__':
	List = [8,6,10,5,7,9,11]
	root = None
	op = OperationTree()
	for val in List:
		root = op.insert(root,val)
	print('中序打印二叉搜索树：', end = ' ')
	op.printTree(root)
	print('')       

	s = Solution()
	print(s.KthNode(root,1))