# رشته فیبوناچی
# https://quera.ir/problemset/contest/17675/سؤال-رشته-فیبوناچی
# pourya.2374@gmail.com

n = int(input())
fib_list = [1, 2]

while fib_list[-1] < 100:
    fib_list.append(fib_list[-1] + fib_list[-2])

result = []
for i in range(1, n+1):
    result.append('+') if i in fib_list else result.append('-')
print(*result, sep='')
