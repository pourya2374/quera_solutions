# مثلث خیام پاسکال
# https://quera.ir/problemset/contest/3410/سؤال-پیاده-سازی-ریاضیات-مثلث-خیام-پاسکال
# pourya.2374@gmail.com


def binomial_coef_seq2(n):
    k = int(n/2)
    b = [1] * (n + 1)
    for i in range(1, k+1):
        b[i] = int(b[i-1] * (n - i + 1) / i)

    b[k+1:] = b[-k-2::-1]
    return b


for i in range(int(input())):
    print(*binomial_coef_seq2(i), sep=' ')
