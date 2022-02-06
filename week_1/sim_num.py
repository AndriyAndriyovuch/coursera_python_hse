num = int(input())

a1 = num // 1000 % 10
a2 = num // 100 % 10
a3 = num // 10 % 10
a4 = num % 10

if a1 == a4 and a2 == a3:
    print(1)
else:
    print(666)
