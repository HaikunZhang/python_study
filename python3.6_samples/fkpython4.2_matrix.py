#!/usr/bin/env python
# -*- coding:utf-8 -*-

##################################################################
# 练习7. 定义计算矩阵转置的函数
# 1  2  3  4 	转置为  1  5  9
# 5  6  7  8            2  6 10
# 9 10 11 12            3  7 11
#                       4  8 12
# 要求：
# 1. 使用循环进行转置
# 2. 使用zip()函数进行转置
# 3. 使用numpy模块进行转置
##################################################################
import numpy

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


#  打印矩阵：
def print_matrix(mat):
    for x in mat:
        for y in x:
            print("%2d" % y, end=" ")
        print('\t')


print("原始矩阵：")
print_matrix(matrix)

# 1.使用循环进行转置
print('使用循环进行转置:')


def matrix_transpose_loop(ma_t):
    new_matrix = [[] for i in ma_t[0]]  # 创建空二维数组new_matrix（new_matrix 的行数等于原始数组的列数）

    for row in ma_t:  # 遍历原始矩阵的每一行
        for i in range(len(row)):    # 遍历原始矩阵每一行中的每一个元素
            new_matrix[i].append(row[i])    # 新矩阵的列添加原始矩阵对应的行的元素
    return new_matrix


print_matrix(matrix_transpose_loop(matrix))


# 2.使用zip()函数进行转置
print('使用zip()函数进行转置:')


def matrix_transpose_zip(ma_t):
    return list(zip(*ma_t))


print_matrix(matrix_transpose_zip(matrix))


# 2.使用numpy模块进行转置
print('使用numpy模块进行转置:')


def matrix_transpose_numpy(ma_t):
    return numpy.transpose(ma_t).tolist()


print_matrix(matrix_transpose_numpy(matrix))
