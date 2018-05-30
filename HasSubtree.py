# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/5/24'

# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def HasSubtree(self, pRoot1, pRoot2):
		'''判断pRoot2是否是pRoot1的子结构'''
		if pRoot1 == None or pRoot2 == None:
			return False
		res = self.SubTree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
		return res

	def SubTree(self, pRoot1, pRoot2):
		'''查找B树根节点在A树中的位置，并返回'''
		if pRoot2 == None:
			return True
		if pRoot1 == None:
			return False
		if pRoot1.val != pRoot2.val:
			return False
		return self.SubTree(pRoot1.left, pRoot2.left) and self.SubTree(pRoot1.right, pRoot2.right)   

def createTree(List):
	if len(List) == 0:
		return 
	boot = TreeNode(List[0])
	if len(List)>=2:
		boot.left = createTree(List[1])
	if len(List)>=3:
		boot.right = createTree(List[2])
	return boot

def printTree(boot):
	'''前序遍历输出树'''
	if boot == None:
		return
	print(boot.val, end = ' ')
	printTree(boot.left)
	printTree(boot.right)

if __name__ == '__main__':
	List1 = [1,[2,[4,[8],[9]],[5]],[3,[6],[7]]]
	List2 = [3,[6],[7]]
	tree1 = createTree(List1)
	tree2 = createTree(List2)
	printTree(tree1)
	print("")
	printTree(tree2)
	print("")

	s = Solution()
	print(s.HasSubtree(tree1, tree2))

	#printTree(tree3.val)