# اسم‌ها
# https://quera.ir/problemset/contest/2529/سؤال-اسمها
# pourya.2374@gmail.com

result = []
for _ in range(int(input())):
    tmp = []
    for item in input():
        if item not in tmp:
            tmp.append(item)
    result.append(len(tmp))
print(max(result))
