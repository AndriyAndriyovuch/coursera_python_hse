height = int(input())
up = int(input())
down = int(input())

day_dist = up - down

if up >= height:
    print(1)

else:
    result = (height - down) // day_dist
    print(result)
