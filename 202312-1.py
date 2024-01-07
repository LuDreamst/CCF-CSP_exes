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
        # for g in range(m):
        #     if ifprint == True:
        #         break
        #     elif ifprint == False and j == n-1 and g == m-1:
        #         print(0)
        #         ifprint = True
        #     else:
        #         if matrix[i][g] < matrix[j][g]:
        #             num += 1
        #             if num == m:
        #                 print(j+1)
        #                 ifprint = True

