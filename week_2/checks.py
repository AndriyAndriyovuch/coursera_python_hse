num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())

if (num_1 + num_2) % 2 == 0 and (num_3 + num_4) % 2 == 0 and num_4 > num_2:
    if (num_1 - (num_4 - num_2)) <= num_3 <= (num_1 + (num_4 - num_2)):
        print('YES')
    else:
        print('NO')
elif (num_1 + num_2) % 2 == 1 and (num_3 + num_4) % 2 == 1 and num_4 > num_2:
    if (num_1 - (num_4 - num_2)) <= num_3 <= (num_1 + (num_4 - num_2)):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
