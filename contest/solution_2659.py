# تست بینایی
# https://quera.ir/problemset/contest/2659/سؤال-تست-بینایی
# pourya.2374@gmail.com

n = int(input())
a1 = input()
a2 = input()

result = 0
for i in range(n):
    if a1[i] != a2[i]:
        result += 1
print(result)
