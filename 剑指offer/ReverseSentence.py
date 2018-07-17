# coding=utf-8

__author__ = 'LY'
__time__ = '2018/6/17'

# 牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
# 同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。
# 后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。

# 思路：字符串翻转

class Solution:
	def ReverseSentence(self, s):
		if not s:
			return ''

		# 字符串循环右移n-1位
		res = s.split(' ')
		res = list(reversed(res))
		return ' '.join(res)

if __name__ == '__main__':
	s = Solution()
	ss = 'student. a am I'
	print(s.ReverseSentence(ss))