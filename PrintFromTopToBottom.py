# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/5/24'

# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，每层从左到右（即层次遍历/在图里是广度优先算法，利用队列）
    # 例：[1,[2,[4,[8],[9]],[5]],[3,[6],[7]]] --> 1,2,3,4,5,6,7,8,9
    def PrintFromTopToBottom(self, root):
        if root == None:
        	return



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
	tree1 = createTree(List1)
	printTree(tree1)
	print("")

	s = Solution()
	s.PrintFromTopToBottom(tree1)