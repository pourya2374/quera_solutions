# خُب باقر سرما خورده
# https://quera.ir/problemset/contest/10231/سؤال-خب-باقر-سرما-خورده
# pourya.2374@gmail.com

inputs = [input().strip() for _ in range(5)]
result = []

for i, item in enumerate(inputs):
    if 'MOLANA' in item or 'HAFEZ' in item:
        result.append(i+1)

if len(result) == 0:
    print('NOT FOUND!')
    exit()
print(*result, sep=' ')
