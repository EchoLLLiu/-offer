# coding=utf-8

__author__ = 'LY'
__time__ = '2018/7/13'

# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

class TreeNode:
	def __init__(self, x):
		self.val = x
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

class Solution:
	def Print(self, pRoot):
		if not pRoot:
			return []
		# 队列，用来实现层次遍历
		queue1 = []
		queue2 = []
		queue1.append(pRoot)
		res = []

		while queue1:
			res1 = []
			while queue1:
				p = queue1.pop(0)
				res1.append(p.val)
				if p.left:
					queue2.append(p.left)
				if p.right:
					queue2.append(p.right)
			if res1 != []:
				res.append(res1) 
			res2 = []
			while queue2:
				q = queue2.pop(0)
				res2.append(q.val)
				if q.left:
					queue1.append(q.left)
				if q.right:
					queue1.append(q.right)
			if res2 != []:
				res.append(res2) 
		return res

if __name__ == '__main__':
	List1 = [1,[2,[4,[8],[9]],[5]],[3,[6],[7]]]
	op = OperationTree()
	tree1 = op.create(List1)
	print('先序打印：',end = '')
	op.PreOrder(tree1)
	print("")

	s = Solution()
	print(s.Print(tree1))