# سراب
# https://quera.ir/problemset/contest/4067/سؤال-سراب
# pourya.2374@gmail.com

points = []
for _ in range(int(input())):
    tmp = list(map(int, input().split(' ')))
    points.append((tmp[0], tmp[1]))

for point in points:
    x, y = point
    if y == x:
        print(2*x - (x % 2))
    elif y == x-2:
        print(2*(x - 1) - (x % 2))
    else:
        print(-1)
