# ساده تر
# https://quera.ir/problemset/contest/3403/سؤال-ساده-تر
# pourya.2374@gmail.com

a = []
for i in range(4):
    a.append(float(input()))

print('Sum : {0:.6f}'.format(sum(a)))
print('Average : {0:.6f}'.format(sum(a) / 4))
print('Product : {0:.6f}'.format(a[0] * a[1] * a[2] * a[3]))
print('MAX : {0:.6f}'.format(max(a)))
print('MIN : {0:.6f}'.format(min(a)))
