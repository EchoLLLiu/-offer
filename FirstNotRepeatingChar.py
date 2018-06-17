# coding=utf-8

__author__ = 'LY'
__time__ = '2018/6/13'

# 在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置

class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
        	return -1
        for char in s:
        	if s.count(char) == 1:
        		return s.index(char)
        return -1

    def FirstNotRepeatingChar2(self, s):
    	return s.index(list(filter(lambda c:s.count(c)==1, s))[0]) if s else None

if __name__ == '__main__':
	ss = 'aaaaabccc'
	s = Solution()
	print(s.FirstNotRepeatingChar(ss))
	print(s.FirstNotRepeatingChar2(ss))

	ss2 = ''
	print(s.FirstNotRepeatingChar(ss2))
	print(s.FirstNotRepeatingChar2(ss2))

	# ss3 = 'aabbcc'
	# print(s.FirstNotRepeatingChar(ss3))
	# print(s.FirstNotRepeatingChar2(ss3))	