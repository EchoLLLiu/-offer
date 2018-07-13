# coding=utf-8

__author__ = 'LY'
__time__ = '2018/7/10'

# 请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
# 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

class Solution:
	# s, pattern都是字符串
	def match(self, s, pattern):
		if not pattern:
			return s == ''
		if len(pattern) == 1:
			return len(s) == 1 and (s[0] == pattern[0] or pattern[0] == '.')
		if pattern[1] != '*':
			if s == '':
				return False
			return (s[0] == pattern[0] or pattern[0] == '.') and self.match(s[1:], pattern[1:])
		while s and (s[0] == pattern[0] or pattern[0] == '.'):
			if self.match(s, pattern[2:]):
				return True
			s = s[1:]
		return self.match(s, pattern[2:])

	def Match(self, s, pattern):
		if not pattern:
			return s == ''
		if len(pattern) > 1 and pattern[1] == '*':
			return self.isMatch(s, pattern[2:]) or (s and (s[0] == pattern[0] or pattern[0] == '.') and self.isMatch(s[1:], pattern))
		else:
			return s and (s[0] == pattern[0] or pattern[0] == '.') and self.isMatch(s[1:], pattern[1:])

if __name__ == '__main__':
	s = Solution()
	print("方法一：")
	print(s.match("aa", "a"))  # false
	print(s.match("aa", "aa"))  # true
	print(s.match("aaa", "aa"))  # false
	print(s.match("aa", "a*"))  # true
	print(s.match("aa", ".*"))  # true
	print(s.match("ab", ".*"))  # true
	print(s.match("aab", "c*a*b"))  # true

	print("方法二：")
	print(s.isMatch("aa", "a"))  # false
	print(s.isMatch("aa", "aa"))  # true
	print(s.isMatch("aaa", "aa"))  # false
	print(s.isMatch("aa", "a*"))  # true
	print(s.isMatch("aa", ".*"))  # true
	print(s.isMatch("ab", ".*"))  # true
	print(s.isMatch("aab", "c*a*b"))  # true	


