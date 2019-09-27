# آسمان شکر آباد
# https://quera.ir/problemset/contest/6082/سؤال-آسمان-شکر-آباد
# pourya.2374@gmail.com

n, m = tuple(map(int, input().split(' ')))
result = 0
for _ in range(n):
    for item in input():
        if item == '*':
            result += 1
print(result)
