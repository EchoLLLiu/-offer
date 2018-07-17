# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/5/21'

# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
    	'''合并两个递增链表'''
    	if pHead1 == None:
    		return pHead2
    	if pHead2 == None:
    		return pHead1
    	# head为头结点
    	head = ListNode(None)
    	p = head
    	p1 = pHead1
    	p2 = pHead2
    	while p1!=None and p2!=None:
    		if p1.val <= p2.val:
    			p.next = p1
    			p = p.next
    			p1 = p1.next
    		else:
    			p.next = p2
    			p = p.next
    			p2 = p2.next
    	if p1 != None:
    		p.next = p1
    	if p2 != None:
    		p.next = p2
    	return head.next


if __name__ == '__main__':
	listnode1 = [1,3,5,7,9]
	head1 = ListNode(listnode1[0])
	p = head1
	for i in range(1,len(listnode1)):
		node = ListNode(listnode1[i])
		p.next = node
		p = node
	q = head1
	while q != None:
		print(q.val, end=" ")
		q = q.next
	print("")

	listnode2 = [0,2,4,6,8]
	head2 = ListNode(listnode2[0])
	p = head2
	for i in range(1,len(listnode2)):
		node = ListNode(listnode2[i])
		p.next = node
		p = node
	q = head2
	while q != None:
		print(q.val, end=" ")
		q = q.next
	print("")	
    
	s = Solution()
	head = s.Merge(head1,head2)
	q = head
	while q != None:
		print(q.val, end=" ")
		q = q.next
	print("")	