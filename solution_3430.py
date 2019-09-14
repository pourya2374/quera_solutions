# بلندگو
# https://quera.ir/problemset/contest/3430/سؤال-بلندگو
# pourya.2374@gmail.com

name = input().strip()
tmp = [i for i in name]

print(name)
for i in range(len(name) - 1):
    tmp[0:i+1] = (i+1)*tmp[i+1]
    print(''.join(tmp))
