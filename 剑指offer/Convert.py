# coding=utf-8

__author__ = 'LY'
__time__ = '2018/6/6'

# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
# 思想：按照中序遍历将二叉搜索树的节点放入列表中，再进行指针变换操作。这里left—>prior , right—>next

class TreeNode:
	'''二叉搜索树节点的定义'''
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution:
	'''二叉搜索树操作'''
	def Convert(self, pRootOfTree):
	    # 借助列表
	    # 当二叉搜索树为空时
	    if pRootOfTree == None:
	    	return None
	    # 当二叉搜索树只有一个根节点时
	    if pRootOfTree and not pRootOfTree.left and not pRootOfTree.right:
	    	return pRootOfTree
	    # 当二叉搜索树含有两个及以上节点时
	    preList = []
	    preList = self.PreOrder(pRootOfTree, preList)	
	    preList[0].left = None
	    preList[0].right = preList[1]
	    for i in range(1,len(preList)-1):
	    	preList[i].left = preList[i-1]
	    	preList[i].right = preList[i+1]
	    preList[-1].left = preList[-2]
	    preList[-1].right = None
	    head = preList[0]
	    return head

	def PreOrder(self, root, preList):
		# 将节点按中序顺序保存到列表中
		if root == None:
			return
		self.PreOrder(root.left, preList)
		preList.append(root)
		self.PreOrder(root.right, preList)
		return preList

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

if __name__ == '__main__':
	List = [1,2,3]
	root = None
	s = Solution()
	for val in List:
		root = s.insert(root,val)
	print('中序打印二叉搜索树：', end = ' ')
	s.printTree(root)
	print('')
	head = s.Convert(root)
	p = head
	while p!=None:
		print(p.val, end=' ')
		p = p.right
