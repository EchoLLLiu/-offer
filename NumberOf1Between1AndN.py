# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/19'

# 求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
# 为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
# ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数。

# 思路：从右往左，从1开始编号。
#     （1）当第i位的数字>1时，从1~n中第i位上为1的个数为：(n//10^i + 1) * 10^(i-1)
#     （2）当第i位的数字<1时，从1~n中第i位上为1的个数为：(n//10^i) * 10^(i-1)
#     （3）当第i位的数字=1时，从1~n中第i位上为1的个数为：(n//10^i) * 10^(i-1) + (n%10^i-1*10^(i-1)+1)

class Solution:
	def NumberOf1Between1AndN_Solution(self, n):
		count = 0
		tmp = n
		i = 1
		while tmp != 0:
			# a为每位上的数字
			a = tmp % 10
			rem = n % (10**i)
			con = n // (10**i)
			base = 10**(i-1)
			if a > 1:
				count += (con + 1) * base
			elif a < 1:
				count += con * base
			else:
				count += con * base + (rem - 1*base + 1)
			tmp = tmp // 10
			i += 1
		return count

if __name__ == '__main__':
	num = 1999
	s = Solution()
	print(s.NumberOf1Between1AndN_Solution(num))