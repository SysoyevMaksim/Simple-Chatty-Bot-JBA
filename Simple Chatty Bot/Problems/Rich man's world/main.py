a = int(input())
count = 0
while a < 700000.0:
    a += a * 7.1 / 100
    count += 1
print(count)
