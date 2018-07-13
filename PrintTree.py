# coding=utf-8

__author__ = 'LY'
__time__ = '2018/7/13'

# 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

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
		# 栈，存储奇数行树节点，从右往左存
		stack1 = []
		# 栈，存储偶数行树节点，从左往右存
		stack2 = []
		res = []

		stack1.append(pRoot)
		while stack1:
			res1 = []
			while stack1:
				p = stack1.pop()
				res1.append(p.val)
				if p.left:
					stack2.append(p.left)
				if p.right:
					stack2.append(p.right)
			if res1!=[]:
				res.append(res1)
			res2 = []
			while stack2:
				q = stack2.pop()
				res2.append(q.val)
				if q.right:
					stack1.append(q.right)
				if q.left:
					stack1.append(q.left)
			if res2!=[]:
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