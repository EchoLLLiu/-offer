# coding = utf-8

__author__ = 'LY'
__time__ = '2018/5/31'

# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
# 二叉搜索树的定义：左子树小于根，右子树大于根，左右子树都是二叉搜索树

class Solution:
    def VerifySquenceOfBST(self, sequence):
        '''判断是否是二叉搜索树的后序遍历'''
        if sequence == []:
        	return False
        # 根节点为序列最后一个数
        root = sequence[-1]
        idx = 0
        # 找到第一个比根节点大的数，该数往后为右子树节点
        for node in sequence[:-1]:
        	if node > root:
        		break
        	idx += 1
        # 判断右子树中的值是否都大于根节点
        for rnode in sequence[idx:-1]:
        	if rnode < root:
        		return False
        # 判断是否左右子树都是二叉搜索树
        left = True
        if idx >= 1:
        	left = self.VerifySquenceOfBST(sequence[:idx])
        right = True
        if idx <= len(sequence)-2:
        	right = self.VerifySquenceOfBST(sequence[idx:-1])
        return left and right

if __name__ == '__main__':
	List = [2,8,9,16,11,5,29,38,35,17]
	s = Solution()
	print(s.VerifySquenceOfBST(List))