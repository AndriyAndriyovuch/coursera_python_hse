cow_num = int(input())

if cow_num % 10 == 1 and cow_num not in range(10, 21):
    print(cow_num, 'korova')
elif cow_num % 10 in range(2, 5) and cow_num not in range(10, 21):
    print(cow_num, 'korovy')
elif cow_num % 10 in range(5, 10) or \
        cow_num in range(10, 21) or \
        cow_num % 10 == 0:
    print(cow_num, 'korov')
