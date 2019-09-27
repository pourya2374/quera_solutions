# شطرنج حرفه‌ای
# https://quera.ir/problemset/contest/2636/سؤال-شطرنج-حرفهای
# pourya.2374@gmail.com

inputs = list(map(int, input().split()))
should_be = [1, 1, 2, 2, 2, 8]

result = []
for i in range(6):
    result.append(should_be[i] - inputs[i])
print(*result, sep=' ')
