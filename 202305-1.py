n = int(input())

matrix = []
for i in range(n):
    row = []
    for j in range(8):
        line = input()
        row.insert(j,line)
    matrix.insert(i,row)

for i in range(n):
    print(matrix[i])

num = []
for i in range(n):
    n_list = 0
    for j in range(i+1):
        if matrix[j] == matrix[i]:
            n_list += 1
    num.append(n_list)
for i in range(n):
    print(num[i])
