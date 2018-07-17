# coding=utf-8

__author__ = 'LY'
__time__ = '2018/7/16'

# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
# 路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
# 如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
# 但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
# 思路：使用递归，设置一个assist数组用来保存路径情况


# class Solution:
#     def hasPath(self, matrix, rows, cols, path):
#         if not matrix:
#             return False
#         for i in range(rows):
#             for j in range(cols):
#                 if matrix[cols * i + j] == path[0]:     # 找到第一个字符所在位置
#                     if self.findPath(list(matrix), rows, cols, path[1:], i, j):
#                         return True
#         return False

#     def findPath(self, matrix, rows, cols, path, x, y):
#         if not path:
#             return True
#         # 将已找到的字符改为“*”
#         matrix[cols * x + y] = '*'

#         # 向右找
#         if y + 1 < cols and matrix[cols * x + y + 1] == path[0]:
#             self.printMatrix(matrix, rows, cols, "向右走")
#             return self.findPath(matrix, rows, cols, path[1:], x, y+1)
#         # 向左找
#         elif y - 1 >= 0 and matrix[cols * x + y - 1] == path[0]:
#             self.printMatrix(matrix, rows, cols, "向左走")
#             return self.findPath(matrix, rows, cols, path[1:], x, y-1)
#         # 向下找
#         elif x + 1 < rows and matrix[cols * (x+1) + y] == path[0]:
#             self.printMatrix(matrix, rows, cols, "向下走")
#             return self.findPath(matrix, rows, cols, path[1:], x+1, y)
#         # 向上找
#         elif x - 1 >= 0 and matrix[cols * (x-1) + y] == path[0]:
#             self.printMatrix(matrix, rows, cols, "向上走")
#             return self.findPath(matrix, rows, cols, path[1:], x-1, y)
#         else:   
#             return False

#     def printMatrix(self, matrix, rows, cols, directions):
#         if directions:
#             print('---'+directions)
#         for i in range(rows):
#             for j in range(cols):
#                 print(matrix[cols*i+j], end=' ')
#             print()

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        assistMatrix = [True]*rows*cols
        for i in range(rows):
            for j in range(cols):
                if(self.hasPathAtAStartPoint(matrix,rows,cols, i, j, path, assistMatrix)):
                    return True
        return False

    def hasPathAtAStartPoint(self, matrix, rows, cols, i, j, path, assistMatrix):
        if not path:
            return True
        index = i*cols+j
        if i<0 or i>=rows or j<0 or j>=cols or matrix[index]!=path[0] or assistMatrix[index]==False:
            return False
        assistMatrix[index] = False
        if(self.hasPathAtAStartPoint(matrix,rows,cols,i+1,j,path[1:],assistMatrix) or
               self.hasPathAtAStartPoint(matrix,rows,cols,i-1,j,path[1:],assistMatrix) or
               self.hasPathAtAStartPoint(matrix,rows,cols,i,j-1,path[1:],assistMatrix) or
               self.hasPathAtAStartPoint(matrix,rows,cols,i,j+1,path[1:],assistMatrix)):
            return True
        assistMatrix[index] = True
        return False

if __name__ == '__main__':
    # 调用测试
    _matrix = 'abcesfcsadee'
    _path = 'see'
#    _path = 'bcced'
    path = Solution()
    print(path.hasPath(list(_matrix), 3, 4, _path))



