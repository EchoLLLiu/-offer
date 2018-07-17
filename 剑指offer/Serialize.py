# coding=utf-8

__author__ = 'LY'
__time__ = '2018/7/15'

# 请实现两个函数，分别用来序列化和反序列化二叉树
# 思路：先序顺序将二叉树节点保存在列表中，每个节点结束用“！”表示，空节点用“#！”表示

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
	def __init__(self):
		self.li = []

	def preSave(self, root):
		if not root:
			self.li.append("#!")
			return
		self.li.append(str(root.val)+"!")
		self.preSave(root.left)
		self.preSave(root.right)

	def Serialize(self, root):
		self.preSave(root)
		return ''.join(self.li)

	def Deserialize(self, s):
		if not s:
			return 
		s = s.split('!')
		del s[-1]
		root, index = self.createTree(s, 0)
		return root

	def createTree(self, s, index):
		if s[index] == '#':
			return None, index+1
		root = TreeNode(int(s[index]))
		index += 1
		root.left, index = self.createTree(s, index)
		root.right, index = self.createTree(s, index)
		return root, index


if __name__ == '__main__':
	List1 = [1,[2,[4,[8],[9]],[5]],[3,[6],[7]]]
	op = OperationTree()
	tree1 = op.create(List1)
	print('先序打印：',end = '')
	op.PreOrder(tree1)
	print("")

	s = Solution()
	ss = s.Serialize(tree1)
	print(ss)
	root = s.Deserialize(ss)
	op.PreOrder(root)
