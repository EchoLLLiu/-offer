# coding=utf-8

__author__ = 'LY'
__time__ = '2018/6/6'

# 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

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

	def FindPath(self, root, expectNumber):
		'''返回二维列表，内部每个列表表示找到的路径'''
		if root == None:
			return 
		# 保存所有路径
		res = []
		# 保存当前路径
		path = []
		self.Find(root, expectNumber, res, path)
		return res

	def Find(self, root, target, res, path):
		if root == None:
			return
		path.append(root.val)
		isLeaf = (root.left == None and root.right == None)
		if isLeaf and target == root.val:
			res.append(path[:])
		if root.left:
			self.Find(root.left, target-root.val, res, path) 
		if root.right:
			self.Find(root.right, target-root.val, res, path)
		path.pop()

if __name__ == '__main__':
	List1 = [1,[2,[4,[8],[9]],[5]],[3,[6],[4]]]
	op = OperationTree()
	tree1 = op.create(List1)
	print('先序打印：',end = '')
	op.PreOrder(tree1)
	print("")
	res = op.FindPath(tree1, 8)
	print(res)