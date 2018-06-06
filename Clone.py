# coding=utf-8

__author__ = 'LY'
__time__ = '2018/6/6'

# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。

class RandomListNode:
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution:
	# 返回 RandomListNode
	def Clone(self, pHead):
		'''一个节点一个节点拷贝'''
		if pHead == None:
			return pHead
		p = pHead
		newhead = RandomListNode(pHead.label)
		newhead.next = pHead.next
		newhead.random = pHead.random

		newp = newhead
		p = p.next

		while p!=None:
			currentNode = RandomListNode(p.label)
			currentNode.next = p.next
			currentNode.random = p.random
			newp.next = currentNode
			newp = newp.next
			p = p.next
		return newhead


	def createList(self, List):
		if List == []:
			return None
		head = RandomListNode(List[0])
		p = head

		for i in range(1,len(List)):
			currentNode = RandomListNode(List[i])
			p.next = currentNode
			p.random = currentNode
			p = p.next
		return head

	def printList(self, head):
		p = head
		while p!=None:
			print(p.label, end=' ')
			p = p.next

if __name__ == '__main__':
	List = [1,2,3,4,5]
	s = Solution()
	head = s.createList(List)
	s.printList(head)
	print("")
	newhead = s.Clone(head)
	s.printList(newhead)