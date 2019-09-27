# ام‌سین
# https://quera.ir/problemset/contest/28947/سؤال-پیاده-سازی-امسین
# pourya.2374@gmail.com

import random
import string

for _ in range(int(input())):
    tmp = 's{}'.format(
        ''.join(random.sample(string.ascii_lowercase, random.randint(1, 16)))
    )
    print(tmp)
