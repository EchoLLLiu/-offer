# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/5/20'

# 输入一个链表，输出该链表中倒数第k个结点。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def FindKthToTail(self, head, k):
		'''	可以用两个指针，一个指针遍历到第k个结点的时候，第二个指针再走到第一个节点，
			然后两个指针的距离始终保持k-1，这样，当第一个指针的next==NULL，也就是走到最后一个节点的时候，
			第二个指针对应的位置，就是倒数第k个结点。'''
		if head == None or k <= 0:
			return None
		p1 = head
		p1Count = 1
		p2 = head
		while p1 != None and p1Count < k:
			p1 = p1.next
			p1Count += 1
		# 当k大于链表长度时
		if p1 == None:
			return None
		while p1.next != None:
			p1 = p1.next
			p2 = p2.next
		return p2 

	# def FindKthToTail(self, head, k):
	# 	'''统计链表个数，输出第n-k个（注意是返回节点，不是返回节点的值）'''
	# 	# 链表为空或k小于0
	# 	if head == None or k <= 0:
	# 		return None
	# 	p = head
	# 	lens = 0
	# 	while p!= None:
	# 		lens += 1
	# 		p = p.next
	# 	# k值大于链表长度
	# 	if k > lens:
	# 		return None
	# 	i = 0
	# 	q = head
	# 	while i < lens-k:
	# 		q = q.next
	# 		i += 1
	# 	return q


if __name__ == '__main__':
	listnode = [1,2,3,4,5,6,7,8]
	head = ListNode(listnode[0])
	p = head
	for i in range(1,len(listnode)):
		node = ListNode(listnode[i])
		p.next = node
		p = node
	q = head
	while q != None:
		print(q.val, end=" ")
		q = q.next
	print("")
	s = Solution()
	p=s.FindKthToTail(head,3)
	print(p.val)

        