x = int(input())
y = int(input())
up = y > 0
over = x > 0
if up and over:
    print(1)
elif not over and up:
    print(2)
elif over and not up:
    print(3)
else:
    print(4)