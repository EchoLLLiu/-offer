# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/5/30'

# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
# 但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
# 模拟栈的弹出过程

class Solution:
	def IsPopOrder1(self, pushV, popV):
		# 模拟栈弹出过程来实现
		stack = []
		while popV:
			# 如果入栈顺序为1,2,3,4,5 出栈顺序为1,2,3,4,5
			if pushV and pushV[0] == popV[0]:
				pushV.pop(0)
				popV.pop(0)
			# 否则比较出栈顺序栈底元素与辅助栈栈顶元素是否相等
			elif stack and popV[0] == stack[-1]:
				stack.pop()
				popV.pop(0)
			# 如果stack为空，pushV不为空，将pushV的栈底元素加入到stack中
			elif pushV:
				tmp = pushV.pop(0)
				stack.append(tmp)
			else:
				return False
		return True

	def IsPopOrder2(self, pushV, popV):
		stack = []
		while pushV:
			stack.append(pushV.pop(0))
			while stack:
				if stack[-1] == popV[0]:
					popV.pop(0)
					stack.pop()
				else: break
		while popV:
			if popV[0] == stack[-1]:
				stack.pop()
				popV.pop(0)
			else: break
		return stack == []

if __name__ == '__main__':
	pushV = [1,2,3,4,5]
	#popV1 = [4,5,3,2,1]
	#popV2 = [4,3,5,1,2]
	#popV3 = [1,2,3,4,5]
	popV4 = [4,3,2,1,5]
	s = Solution()
	#print(s.IsPopOrder1(pushV, popV1))
	#print(s.IsPopOrder1(pushV, popV2))
	#print(s.IsPopOrder1(pushV, popV3))
	print(s.IsPopOrder1(pushV, popV4))
	#print(s.IsPopOrder2(pushV, popV1))
	#print(s.IsPopOrder2(pushV, popV2))
	#print(s.IsPopOrder2(pushV, popV3))
	#print(s.IsPopOrder2(pushV, popV4))

