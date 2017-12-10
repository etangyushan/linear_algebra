#-*- coding:utf8 -*-
import unittest
import numpy as np

from decimal import *

#-*- coding:utf8 -*-
from copy import deepcopy
from decimal import Decimal, getcontext
seed = 333

def transpose(M):
    # return zip(*M)
    try:
        ret = [[0 for col in range(len(M))] for row in range(len(M[0]))]
        for i in range(len(M)):
            for j in range(len(M[i])):
                ret[j][i] = M[i][j]
        return ret
    except Exception as e:
        ret = []
        ret.append(list(M))
        return ret


# TODO 计算矩阵乘法 AB，如果无法相乘则raise ValueError
def matxMultiply(A, B):

    # return [[sum(a*b for a, b in zip(a,b)) for b in transpose(B)] for a in A]
    try:
        res = [[0]*len(B[0]) for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in xrange(len(A[0])):
                    res[i][j] += A[i][k]*B[k][j]
    except Exception as e:
        raise ValueError

    return res

#print transpose(m)
# A=[[3,2]]
# B=[[1,2,3],[1,2,3]]
# print "start"
# print matxMultiply(A, B)

# TODO 构造增广矩阵，假设A，b行数相同
def augmentMatrix(A, b):
    ret=deepcopy(A)
    for i in range(len(ret)):
        # print "a:",ret[i]
        ret[i].append(b[i][0])
    return ret

# A=[[1,2],[4,5]]
# b=[[3],[6]]
# print augmentMatrix(A, b)

# A=[[-4, -3, -5, 4, 3, -7, -3, 5, 5, 4, -2, -10, 4, -5, 7, -7, -4, 9, -6],
#  [6, -5, 0, 4, 2, -4, 6, -5, 7, 3, -8, 8, 0, -10, -6, -8, -7, -7, 1],
#  [0, -3, 6, -7, -7, 4, -6, 9, -5, -9, 7, 5, -7, -1, 6, 0, -2, 1, 5],
#  [6, -7, -6, 9, 3, 8, -10, -6, -5, 5, 0, -1, 6, 0, 4, -10, 7, 2, -9],
#  [-6, 8, -1, 5, -1, 1, 5, -5, 1, -6, -1, 9, 1, 9, 0, 6, -2, -3, -1],
#  [7, -4, 6, 1, 4, -5, 2, -8, -9, -9, 8, 4, -6, -7, 7, -5, 5, 0, 1],
#  [-4, -1, 8, -9, 3, -1, -1, 5, -8, 5, -1, 7, -7, 8, 8, 7, 9, 4, -9],
#  [1, 6, 6, 1, -4, -9, 1, -6, 8, -10, -6, -5, -7, -3, -7, 0, -2, -7, -8]]
# b=[[9], [-4], [5], [0], [1], [-3], [-9], [0]]
# print augmentMatrix(A, b)

# A=[[-1, 8, -6], [-6, 2, 2], [-6, 6, -3]]
# b=[[-7], [8], [0]]
# print augmentMatrix(A, b)
# print A

# TODO r1 <---> r2
# 直接修改参数矩阵，无返回值
def swapRows(M, r1, r2):
    for i in range(len(M[r1])):
        tmp = M[r1][i]
        M[r1][i] = M[r2][i]
        M[r2][i] = tmp

# TODO r1 <--- r1 * scale
# scale为0是非法输入，要求 raise ValueError
# 直接修改参数矩阵，无返回值
def scaleRow(M, r, scale):
    try:
        if (scale == 0):
            raise ValueError
        for i in range(len(M[r])):
            # print "M[r][i]:",M[r][i]
            # print "scale:", scale
            M[r][i] = round(M[r][i]*scale, 4)
    except Exception as e:
        raise e

# TODO r1 <--- r1 + r2*scale
# 直接修改参数矩阵，无返回值
def addScaledRow(M, r1, r2, scale):
    for i in range(len(M[r1])):
        M[r1][i] = round(M[r1][i] + M[r2][i]*scale, 4)

# M=[[1,2,3], [4,5,6]]

# print "M:",M
# addScaledRow(M, 0, 1, 2)
# print "M:",M
# print "M:",M
# swapRows(M, 0, 1)
# print "M:",M

# print "M:",M
# scaleRow(M, 0, 3)
# print "M:",M
# scaleRow(M, 0, 0)


# TODO 实现 Gaussain Jordan 方法求解 Ax = b
""" Gaussian Jordan 方法求解 Ax = b.
    参数
        A: 方阵
        b: 列向量
        decPts: 四舍五入位数，默认为4
        epsilon: 判读是否为0的阈值，默认 1.0e-16

    返回列向量 x 使得 Ax = b
    返回None，如果 A，b 高度不同
    返回None，如果 A 为奇异矩阵
"""
def gj_Solve1(A, b, decPts=4, epsilon = 1.0e-16):
    try:
        #步骤1 检查A，b是否行数相同
        if (len(A) != len(b)):
            raise ValueError
    except Exception as e:
        raise e
    #步骤2 构造增广矩阵Ab
    Ab = augmentMatrix(A, b)
    print "Ab:",Ab
    #步骤3 逐列转换Ab为化简行阶梯形矩阵
    ## 获取绝对值最大的值
    maxnum = 0
    c_row = 0
    c_col = 0
    for i in range(len(Ab)):
        for j in range(len(Ab[0])):
            if (j <= i):
                if (maxnum < abs(Ab[i][j])):
                    maxnum = abs(Ab[i][j])
                    c_row = i
                    c_col = j
    print "maxnum:",maxnum

    if (maxnum == 0):
        ##奇异矩阵
        print "奇异矩阵"
        return None
    else:
        # print "Ab:", Ab
        # print "c_row:", c_row
        # print "c_col:", c_col
        ##将绝对值最大值所在行交换到对角线元素所在行（行c）
        print "swapRows Ab 1:", Ab
        swapRows(Ab, c_row, c_col)
        print "swapRows Ab 2:", Ab

        ##行变换:将列c的对角线元素缩放为1
        for i in range(len(Ab)):
            print "Ab_ij:", Ab[i][i]
            scaleRow(Ab, i, round(1.0/Ab[i][i], decPts))
        print "scaleRow Ab:", Ab

        ##行变换:多次使用第三个行变换，将列c的其他元素消为0
        c_row = 0
        for i in range(len(Ab)):

            print "----Ab is:", Ab
            for j in range(len(Ab[0])-1):
                print "--i:",i
                print "--j:",j
                if (i == j):
                    print "skip  Ab[i][i]"
                else:
                    if (Ab[i][j] < 0):
                        addScaledRow(Ab, i, j, Ab[i][j])
                    else:
                        addScaledRow(Ab, i, j, -Ab[i][j])
                    print "---Ab:", Ab
            c_row += 1
            print "c_row is:", c_row
            ##行变换:将列c的对角线元素缩放为1
            scaleRow(Ab, i, round(1.0/Ab[i][i], decPts))
    print "Ab:", Ab
    ##整理格式
    ret = []
    for i in range(len(Ab)):
        for j in range(len(Ab[0])):
            if (Ab[i][j] <= epsilon):
                Ab[i][j] = 0
            Ab[i][j] = round(Ab[i][j], decPts)

        ret.append(Ab[i][(len(Ab[0])-1)])
        print "ret:",ret

    return ret

# TODO 实现 Gaussain Jordan 方法求解 Ax = b

""" Gaussian Jordan 方法求解 Ax = b.
    参数
        A: 方阵
        b: 列向量
        decPts: 四舍五入位数，默认为4
        epsilon: 判读是否为0的阈值，默认 1.0e-16

    返回列向量 x 使得 Ax = b
    返回None，如果 A，b 高度不同
    返回None，如果 A 为奇异矩阵
"""

def gj_Solve (A, b, decPts=4, epsilon = 1.0e-16):
    # print "decPts:",decPts
    # print "epsilon:",epsilon
    try:
        #步骤1 检查A，b是否行数相同
        if (len(A) != len(b)):
            raise ValueError
    except Exception as e:
        raise e
    #步骤2 构造增广矩阵Ab
    Ab = augmentMatrix(A, b)
    # print "Ab:",Ab
    #步骤3 逐列转换Ab为化简行阶梯形矩阵
    ## 获取绝对值最大的值
    maxnum = 0
    c_row = 0
    c_col = 0
    for i in range(len(Ab)):
        for j in range(len(Ab[0])):
            if (j <= i):
                if (maxnum < abs(Ab[i][j])):
                    maxnum = abs(Ab[i][j])
                    c_row = i
                    c_col = j
    # print "maxnum:",maxnum

    if (maxnum == 0):
        ##奇异矩阵
        print "奇异矩阵"
        return None
    else:
        # print "Ab:", Ab
        # print "c_row:", c_row
        # print "c_col:", c_col
        ##将绝对值最大值所在行交换到对角线元素所在行（行c）
        # print "swapRows Ab 1:", Ab
        swapRows(Ab, c_row, c_col)
        # print "swapRows Ab 2:", Ab
        try:
            ##行变换
            c_row = 0
            for j in range(len(Ab[0])):
                for i in range(len(Ab)):
                    # print "i:",i
                    # print "j:",j
                    if (i == j):
                        # print "Ab-ij:", Ab[i][i]
                        ##将列c的对角线元素缩放为1
                        scaleRow(Ab, i, round(1.0/Ab[i][i], decPts))
                        # print "scaleRow Ab:", Ab
                    elif (j < len(Ab[0])-1):
                        ##多次使用第三个行变换，将列c的其他元素消为0
                        addScaledRow(Ab, i, j, -Ab[i][j])
                        # print "---Ab:", Ab
                        scaleRow(Ab, i, round(1.0/Ab[i][i], decPts))
                c_row += 1
                # print "c_row is:", c_row
        except Exception as e:
            raise e


    ##整理格式
    ret = []
    for i in range(len(Ab)):
        for j in range(len(Ab[0])):
            if (Ab[i][j] <= epsilon):
                Ab[i][j] = 0
            Ab[i][j] = round(1.0*Ab[i][j], decPts)

        ret.append([Ab[i][(len(Ab[0])-1)]])
    #     print "ret:",ret
    # print "Ab:", Ab
    # print "ret:", ret
    return ret

A=[[3,2,1],[1,-2,5],[2,1,-3]]
b=[[5],[-2],[1]]
print gj_Solve(A, b)

# TODO 实现以下函数并输出所选直线的MSE

def calculateMSE(X,Y,m,b):
    sumvalue = 0
    try:
        for i in range(len(X)):
            squarevalue = (Y[i] - m*X[i] -b)**2
            sumvalue += squarevalue
        mse = sumvalue/1.0*len(X)
        return mse
    except Exception as e:
        raise e

    return sumvalue/len(X)

# print(calculateMSE(X,Y,m,b))

# TODO 实现线性回归
'''
参数：X, Y
返回：m，b
'''
def linearRegression(X,Y):
    X = [[x] for x in X]
    Y = [[y] for y in Y]
    # print "X:",X
    # print "Y:",Y
    XT = transpose(X)
    # print "XT",XT

    A = matxMultiply(XT, X)
    b = matxMultiply(XT, Y)

    print gj_Solve(A, b)
    return None,None

m,b = linearRegression(X,Y)
print(m,b)