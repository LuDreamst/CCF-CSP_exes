n,d = input().split(" ")
n = int(n)
d = int(d)

Q = []
K = []
V = []
Kt =[]

def matrix_function(matrix,n,d):
    for i in range(n):
            row = input().split(" ")
            for j in range(d):
                  row[j] = int(row[j])
            matrix.insert(i,row)

def transposed_matrix(matrix_in,matrix_out,n,d):
    for i in range(d):
        row = []
        for j in range(n):
            row.append(matrix_in[j][i])
        matrix_out.append(row)
    return matrix_out

matrix_function(Q,n,d)
matrix_function(K,n,d)
transposed_matrix(K,Kt,n,d)
matrix_function(V,n,d)

W = []
def w_function(n):
    r = input().split(" ")
    for i in range(n):
        row = []
        row.append(int(r[i]))
        W.insert(i,row)
w_function(n)

def dot_puduct(matrix1,matrix2):
     matrix_result = []
     for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            row.append(matrix1[i][0]*matrix2[i][j])
        matrix_result.append(row)
     return matrix_result

def cross_puduct(matrix1,matrix2):
    matrix_result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            r = 0
            for g in range(len(matrix2)):
                r += matrix1[i][g]*matrix2[g][j]
            row.append(r)
        matrix_result.append(row)
    return matrix_result

QxKt = cross_puduct(Q,Kt)
WQxKt = dot_puduct(W,QxKt)
WQxKtxV = cross_puduct(WQxKt,V)
for i in range(len(WQxKtxV)):
    for j in range(len(WQxKtxV[0])):
        print(WQxKtxV[i][j], end=" ")
    print()
