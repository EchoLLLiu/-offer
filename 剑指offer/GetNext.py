# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/26'

# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
# 思路：(1)如果该节点为根节点，则返回右子树的最左子节点；否则，(2)若该节点为左叶子节点，则返回其父节点，(3)若为右叶子节点，则判断其父节点是否是父节点的父节点的左右孩子。

class TreeLinkNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution:
    def GetNext(self, pNode):
    	if not pNode:
    		return pNode
    	# (1)
    	if pNode.right:
    		p = pNode.right
    		while p.left:
    			p = p.left
    		return p
    	# (2)
    	while pNode.next:
    		tmp = pNode.next
    		if pNode == tmp.left:
    			return tmp
    		# (3)
    		pNode = tmp





	