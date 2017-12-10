from decimal import Decimal
I = [[1.123456,2.123456,3.123456,5.123456],
     [2.123456,3.123456,3.123456,5.123456],
     [1.123456,2.123456,5.123456,1.123456],
     [3.123456,1.123456,2.123456,5.123456]]
print len(I)
print len(I[0])

n=3

def matxRound(M, decPts=4):
    for i in xrange(len(M)):
        #print i, M[i]
        for j in xrange(len(M[i])):
            #print j, M[i][j]
            n = Decimal(M[i][j])
            n = round(n, decPts)
            M[i][j] = n


matxRound(I, 4)
print I