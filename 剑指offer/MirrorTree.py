# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/5/26'

# 操作给定的二叉树，将其变换为源二叉树的镜像。[1,[2,[4,[8],[9]],[5]],[3,[6],[7]]]-->[1,[3,[7],[6]],[2,[5],[4,[9],[8]]]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # 递归交换左右子树，返回镜像树
        if root == None:
        	return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root

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
	mirr = s.Mirror(tree1)
	printTree(mirr)


