q = int(input())
list_input = []
for i in range(q):
    x,y = input().split(" ")
    x = int(x)
    y = int(y)
    list_input.append([x,y])
# print('list_input:',list_input)

def ifprime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def prime_factor(n):
    list_prime = []
    j = 2
    while True:
        if ifprime(n):
            list_prime.append(n)
            break
        if ifprime(j) and n % j == 0:
            n = n // j
            list_prime.append(j)
            if ifprime(n):
                list_prime.append(n)
                break
        else:
            j += 1
    return list_prime

for i in range(q):
    num = 1
    list_prime_factor = prime_factor(list_input[i][0])
    # print('list_prime_factor:',list_prime_factor)
    for j in list_prime_factor:
        # print('j:',j)
        # print('list_prime_factor.count(j):',list_prime_factor.count(j))
        if list_prime_factor.count(j) >= list_input[i][1]:
            num = num * j
    print(num)