#-*- coding:utf8 -*-
from math import sqrt, acos, pi
from decimal import Decimal, getcontext
# TODO 返回矩阵的行数和列数
def shape(M):
    return len(M),len(M[0])


# TODO 每个元素四舍五入到特定小数数位
# 直接修改参数矩阵，无返回值
def matxRound(M, decPts=4):
    for i in range(len(M)):
        #print i, M[i]
        for j in range(len(M[i])):
            #print j, M[i][j]
            n = Decimal(M[i][j])
            n = round(n, decPts)
            M[i][j] = n



# TODO 计算矩阵的转置
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

# TODO 构造增广矩阵，假设A，b行数相同
from copy import deepcopy
def augmentMatrix(A, b):
    ret=deepcopy(A)
    for i in range(len(ret)):
        # print "a:",ret[i]
        ret[i].append(b[i][0])
    return ret


# ## 2.2 初等行变换
# - 交换两行
# - 把某行乘以一个非零常数
# - 把某行加上另一行的若干倍：

# In[13]:


# TODO r1 <---> r2
# 直接修改参数矩阵，无返回值
def swapRows(M, r1, r2):
    # print "r1:", r1
    # print "r2:", r2
    for i in range(len(M[r1])):
        tmp = M[r1][i]
        # print "i:",i

        M[r1][i] = M[r2][i]
        M[r2][i] = tmp


# In[14]:


# In[15]:


# TODO r1 <--- r1 * scale
# scale为0是非法输入，要求 raise ValueError
# 直接修改参数矩阵，无返回值
def scaleRow(M, r, scale):
    try:
        if (scale == 0):
            raise ValueError
        for i in range(len(M[r])):
            M[r][i] = M[r][i]*scale
    except Exception as e:
        raise e


# In[16]:



# In[17]:


# TODO r1 <--- r1 + r2*scale
# 直接修改参数矩阵，无返回值
def addScaledRow(M, r1, r2, scale):
    for i in range(len(M[r1])):
        M[r1][i] = M[r1][i] + M[r2][i]*scale


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

def gj_Solve(A, b, decPts=4, epsilon = 1.0e-16):
    # print "decPts:",decPts
    # print "epsilon:",epsilon
    #步骤1 检查A，b是否行数相同
    if (len(A) != len(b)):
        print "row not equal"
        return None

    #步骤2 构造增广矩阵Ab
    Ab = augmentMatrix(A, b)

    # print "Ab:",Ab
    #步骤3 逐列转换Ab为化简行阶梯形矩阵
    ##遍历列
    max_row = 0
    max_col = 0
    max_num = 0
    for y in xrange(0, len(Ab[0])-1):
        # print "---------------y:",y
        ##遍历行,获取当前列绝对值最大的值
        for x in range(len(Ab)):
            if (max_num < abs(Ab[x][y])):
                max_num = abs(Ab[x][y])
                max_row = x
                max_col = y

        if (max_num < epsilon):
            ##奇异矩阵
            print "奇异矩阵"
            return None
        else:
            # print "Ab:", Ab
            # print "c_row:", c_row
            # print "c_col:", c_col
            ##将绝对值最大值所在行交换到对角线元素所在行（行c）
            # print "swapRows Ab 1:", Ab
            swapRows(Ab, max_row, max_col)

        # print "Ab-xy:", Ab[x][y]
        ##将列c的对角线元素缩放为1
        scaleRow(Ab, y, 1.0/Ab[y][y])
        # print "scaleRow Ab:", Ab


        for x in range(len(Ab)):
            ##多次使用第三个行变换，将列c的其他元素消为0
            if (x != y):
                addScaledRow(Ab, y, x, -(1.0/Ab[x][y]))


   # print "scaleRow Ab:", Ab

    ##整理格式
    matxRound (Ab, decPts)

    ret = []
    for i in range(len(Ab)):
        ret.append([Ab[i][(len(Ab[0])-1)]])

        # print "ret:",ret
    # print "Ab:", Ab
    # print "ret:", ret
    return ret

A=[[1,2,1],[3,-1,-3],[2,3,1]]
b=[[5],[-2],[1]]
print gj_Solve(A, b)