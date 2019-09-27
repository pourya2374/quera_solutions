# کدتخفیف
# https://quera.ir/problemset/contest/10327/سؤال-کدتخفیف
# pourya.2374@gmail.com


def converter(in_str: str) -> list:
    tmp = []
    for i in in_str:
        if i not in tmp:
            tmp.append(i)
    return sorted(tmp)


n, base = input().split(' ')
base = converter(base)
for _ in range(int(n)):
    tmp = converter(input())
    if base == tmp:
        print('Yes')
    else:
        print('No')
