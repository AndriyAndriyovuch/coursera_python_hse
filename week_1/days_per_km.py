km = int(input())
destination = int(input())

if km >= destination:
    print(1)
else:
    result = destination / km
    result2 = destination // km

    if result2 % result == 0:
        print(result2)
    elif not result2 % result == 0:
        print(result2 + 1)
