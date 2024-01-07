n, m = input().split(" ")
n = int(n)
m = int(m)

matrix = []
for i in range(n):
    matrix.append([])
    for j in input().split(" "):
        matrix[i].append(int(j))

for i in range(n):
    ifprint = False
    for j in range(n):
        if ifprint == False:
            if all(matrix[i][g] < matrix[j][g] for g in range(m)):
                print(j+1)
                ifprint = True
            else:
                if j == n-1:
                    print(0)
                    ifprint = True
