num = int(input())

seconds = str(num % 60).zfill(2)
minutes = str(num // 60 % 60).zfill(2)
hours = str(num // 60 // 60 % 24)

print(hours, minutes, seconds, sep=':')
