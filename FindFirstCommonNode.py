# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/20'

# 输入两个链表，找出它们的第一个公共结点。

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def FindFirstCommonNode(self, pHead1, pHead2):
		if not pHead1 or not pHead2:  
			return None  
		p1, p2 = pHead1, pHead2  
		while p1 != p2:  
			p1 = pHead2 if not p1 else p1.next  
			p2 = pHead1 if not p2 else p2.next  
		return p1 

	def ceateList(self, arr):
		node = ListNode(arr[0])
		head = p = node
		for i in range(1,len(arr)):
			node = ListNode(arr[i])
			p.next = node
			p = node
		return head

	def printList(self, head):
		p = head
		while p!=None:
			print(p.val, end=' ')
			p = p.next

if __name__ == '__main__':
	arr3 = [11,12,13]
	arr2 = [6,8,7,9,0,2,3,4,5]
	s = Solution()
	head2 = s.ceateList(arr2)
	head3 = s.ceateList(arr3)
	i = 1
	p = head2
	while i <= 5:
		p = p.next
		i += 1
	head1 = p
	s.printList(head1)
	print("")
	s.printList(head2)
	print("")
	s.printList(head3)
	print("")
	con = s.FindFirstCommonNode(head1, head2)
	print(con.val)
	con3 = s.FindFirstCommonNode(head3, head2)
	print(con3)