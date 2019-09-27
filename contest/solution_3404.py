# تو چقدر اضافه وزن داری؟
# https://quera.ir/problemset/contest/3404/سؤال-تو-چقدر-اضافه-وزن-داری
# pourya.2374@gmail.com

n = int(input())
m = float(input())

bmi = n / m**2
print('{0:.2f}'.format(bmi))

if bmi < 18.5:
    print('Underweight')
elif bmi < 25:
    print('Normal')
elif bmi < 30:
    print('Overweight')
else:
    print('Obese')
