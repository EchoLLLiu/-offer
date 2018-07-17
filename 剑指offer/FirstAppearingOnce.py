# coding=utf-8

__author__ = 'LY'
__time__ = '2018/7/12'

# 请实现一个函数用来找出字符流中第一个只出现一次的字符。
# 例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

class Solution:
	# 返回对应char
	def __init__(self):
		self.s = ""
		self.dict = {}

	def FirstAppearingOnce(self):
		for ch in self.s:
			if self.dict[ch] == 1:
				return ch
		return '#'

	
	def Insert(self, char):
		if char in self.dict.keys():
			self.dict[char] += 1
		else:
			self.dict[char] = 1
		self.s += char

if __name__ == '__main__':
	li = "go"
	so = Solution()
	for i in range(len(li)):
		so.Insert(li[i])
	print(so.FirstAppearingOnce())