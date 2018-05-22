# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/5/21'

# 输入一个链表，反转链表后，输出链表的所有元素。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        '''反转链表（头插法建立新链表）'''
        p = pHead
        # cur指向下一个待插入的节点
        cur = None
        # rhead指向新链表的头节点
        rHead = None
        while p!=None:
        	cur = p.next
        	p.next = rHead
        	rHead = p
        	p = cur
        return rHead

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
	rhead = s.ReverseList(head)
	q = rhead
	while q != None:
		print(q.val, end=" ")
		q = q.next
	print("")