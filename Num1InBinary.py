# coding = utf-8

__author__ = 'LY'
__time__ = '2018/5/18'

# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

class Solution:
    def NumberOf1(self, n):
    	'''计算整数二进制中的1个数，不包括符号位，共有32位用来表示'''
    	if n >= 0:
    		biList = self.toBinary(n)
    	if n < 0:
    		n = abs(n)
    		biList = self.toBinary(n)
    		biList = self.NegativeBi(biList)
    	return biList.count(1)

        
    def toBinary(self, n):
    	'''将正整数转换成二进制数'''
    	bi = [0]*32
    	i = 0
    	while n//2 != 0:
    		re = n%2
    		bi[i] = re
    		i += 1
    		n = n//2
    	bi[i] = n
    	bi = list(reversed(bi))
    	return bi

    def NegativeBi(self, biList):
    	'''将负数的二进制原码转换成补码'''
    	for i in range(0,len(biList)):
    		biList[i] = 1 - biList[i]
    	# 进位
    	c = 1
    	biList = biList[::-1]
    	for i in range(len(biList)): 
    		biList[i] = biList[i] + c
    		if biList[i] == 2:
    			biList[i] = 0
    			c = 1 
    		else:
    			c = 0
    	if c == 1:
    		biList.append(c)
    	biNeg = biList[::-1]
    	return biNeg

    def NumberOf1_2(self, n):
        INT_BITS = 32
        MAX_INT = (1 << (INT_BITS - 1)) - 1
        if n == 0:
            return 0
        count = 0
        while n != 0:
            if n < -MAX_INT - 1 or n > MAX_INT:
                break
            count += 1
            n = n & (n-1)
        return count

    def NumberOf1_3(self, n):
        INT_BITS = 32
        MAX_INT = (1 << (INT_BITS - 1)) - 1
        if n == 0:
            return 0
        count, bit = 0, 1
        while n != 0 and bit <= MAX_INT + 1:
            if bit & n:
                count += 1
                n -= bit
            bit = bit << 1
        return count



if __name__ == '__main__':
	n = 7
	s = Solution()
	#orgin = s.toBinary(n)
	#print(orgin)
	print(s.NumberOf1_3(n))

