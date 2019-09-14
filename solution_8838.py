# کمک به کاپی
# https://quera.ir/problemset/contest/8838/سؤال-کمک-به-کاپی
# pourya.2374@gmail.com

n, name = input().split(' ')

result = []
for i in range(int(n)):
    result.append('copy of')
result.append(name)

print(*result, sep=' ')
