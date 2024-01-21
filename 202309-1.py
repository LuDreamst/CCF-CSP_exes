n, m = map(int, input().split())

listT = []  
for i in range(n):
    x, y = map(int, input().split())
    listT.append([x, y])

listM = []
for i in range(m):
    x, y = map(int, input().split())
    listM.append([x, y])

# print(listT)
# print(listM)

for i in range(m):
    for j in range(n):
        listM[i][0] = listM[i][0] + listT[j][0]
        listM[i][1] = listM[i][1] + listT[j][1]

for i in range(m):
    print(listM[i][0], listM[i][1])