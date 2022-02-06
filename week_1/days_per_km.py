km = int(input())
destination = int(input())

if km == destination:
    print(1)
else:
    result = destination // km + 1
    print(result)
