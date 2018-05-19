
##请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        replace = '%20'
        resault = ''
        lens = len(s)
        i = 0
        while i < lens:
        	if s[i] == ' ':
        		resault += replace
        		i += 1
        	else:
        		resault += s[i]
        		i += 1
        return resault       

if __name__ == '__main__':
	s = Solution()
	a = 'We Are Happy'
	print(s.replaceSpace(a))