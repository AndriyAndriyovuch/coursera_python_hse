num_1 = int(input())
num_2 = int(input())

if num_2 % (num_2 - (num_1 - 1)) == 0:
    print('YES')
else:
    print('NO')
