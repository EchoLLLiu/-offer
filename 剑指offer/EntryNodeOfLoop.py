# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/25'

# 一个链表中包含环，请找出该链表的环的入口结点。
# 思路：对方法2进行手写推导即可

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# def EntryNodeOfLoop(self, pHead):
	# 	if not pHead or not pHead.next:
	# 		return None
	# 	temp = []
	# 	p = pHead
	# 	while p not in temp and p:
	# 		temp.append(p)
	# 		p = p.next
	# 	return p

	def EntryNodeOfLoop(self, pHead):
		if not pHead or not pHead.next:
			return None
		p1 = pHead
		p2 = pHead
		while  p1 and  p1.next:
			p2 = p2.next
			p1 = p1.next.next
			if p1 == p2:
				break
		p2 = pHead
		while p1 != p2:
			p1 = p1.next
			p2 = p2.next
		return p1.val

	def create(self, List):
		head = ListNode(List[0])
		p = head
		i = 1
		while i < len(List):
			node = ListNode(List[i]) 
			p.next = node
			p = node
			i += 1
		q = head.next.next
		p.next = q
		print(p.next.val)
		return head

	def Print(self, head):
		p = head
		while p!= None:
			print(p.val, end=' ')
			p = p.next
		print("")

if __name__ == '__main__':
	List = [1,2,3,4,5]
	s = Solution()
	head = s.create(List)
	# s.Print(head)
	print(s.EntryNodeOfLoop(head))
