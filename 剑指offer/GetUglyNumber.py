# coding=utf-8

__author__ = 'LY'
__time__ = '2018/6/12'

# 把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

class Solution:
	def GetUglyNumber_Solution(self, index):
		'''返回第index个丑数'''
		if index == 0:
			return 0
		# 保存前N个丑数
		uglyNum = [1]
		# 起始下标都为0
		idx2, idx3, idx5 = 0, 0, 0
		# 再存index-1个数即可
		for i in range(index-1):
			n2, n3, n5 = uglyNum[idx2]*2, uglyNum[idx3]*3, uglyNum[idx5]*5
			Min = min(n2, n3, n5)
			uglyNum.append(Min)
			idx2 += (Min == n2)
			idx3 += (Min == n3)
			idx5 += (Min == n5)
		return uglyNum[-1]

	def isUgly(self, num):
		'''判断num是否是丑数'''
		if num <= 0:
			return False
		for i in [2,3,5]:
			while num % i == 0:
				num = num / i
		if num == 1:
			return True
		else:
			return False

	def nthSuperUglyNumber(self, index, primes):
		'''超级丑数
		Args:
			index: n
			primes: 列表
		当某个数的因子只有primes中的元素时，作为超级丑数，求出第n个超级丑数
		'''
		if index == 0 or not primes:
			return 0
		if index == 1:
			return 1
		uglyNum = [1]
		lens = len(primes)
		# idx为列表，保存每次基数下标
		idx = [0] * lens
		# num保存每次乘积值
		num = [0] * lens
		for i in range(index-1):
			# 更新每次乘积值
			for k in range(lens):
				num[k] = uglyNum[idx[k]] * primes[k]
			Min = min(num)
			uglyNum.append(Min)
			# 更新基数下标值
			for k in range(lens):
				idx[k] += (Min == num[k])
		return uglyNum[-1]

if __name__ == '__main__':
	n = 6
	s = Solution()
	print(s.isUgly(n))
	print(s.GetUglyNumber_Solution(n))
	primes = [2,3,5]
	print(s.nthSuperUglyNumber(n, primes))
