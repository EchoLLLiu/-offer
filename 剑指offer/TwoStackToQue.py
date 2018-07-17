# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/5/15'

# 两个栈实现队列
# 思想：入队：将元素压入stack1
#       出队：判断stack1与stack2是否为空，是则抛出异常；否继续：stack2不为空，stack2.pop(),否则,将stack1中元素倒入stack2中，留stack1中栈底元素弹出

class Solution:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []
	def push(self, node):
		'''入队操作'''
		self.stack1.append(node)
	def pop(self):
		'''出队操作'''
		if len(self.stack1) == 0 and len(self.stack2) == 0:
			print('队列为空!')
			return
		if len(self.stack2) != 0:
			return self.stack2.pop()
		else:
			while len(self.stack1) > 1:
				self.stack2.append(self.stack1[-1])
				del self.stack1[-1]
			return self.stack1.pop()

if __name__ == '__main__':
	a = [1,2,3,4,5]
	s = Solution()
	for node in a:
		s.push(node)
	for i in range(5):
		print(s.pop())
