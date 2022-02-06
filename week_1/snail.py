height = int(input())
up = int(input())
down = int(input())

day_dist = up - down

if up >= height:
    print(1)

else:
    result = (height - down) / day_dist
    result2 = (height - down) // day_dist

    if result2 % result == 0:
        print(result2)
    elif not result2 % result == 0:
        print(result2 + 1)
