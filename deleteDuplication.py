# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/25'

# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
# 思路：递归。递归出口：当pHead.next == None时。
# （1）若pHead.next的值与pHead值相等，在比较pHead.next.next，直到找到与pHead不等的点，继续做以该不等点为头结点的删除重复数字操作。
# （2）若pHead.next的值与pHead值不等，继续做以该不等点为头结点的删除重复数字操作

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def deleteDuplication(self, pHead):
		if not pHead or not pHead.next:
			return pHead
		if pHead.val == pHead.next.val:
			p = pHead.next.next
			while p and p.val == pHead.val:
				p = p.next
			return self.deleteDuplication(p)
		else:
			pHead.next = self.deleteDuplication(pHead.next)
			return pHead

		

	def create(self, List):
		head = ListNode(List[0])
		p = head
		i = 1
		while i < len(List):
			node = ListNode(List[i]) 
			p.next = node
			p = node
			i += 1
		return head

	def Print(self, head):
		p = head
		while p!= None:
			print(p.val, end=' ')
			p = p.next
		print("")

if __name__ == '__main__':
	List = [1,2,3,3,4,4,5]
	s = Solution()
	head = s.create(List)
	s.Print(head)
	head2 = s.deleteDuplication(head)
	s.Print(head2)