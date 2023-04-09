print('Введите 3 случайных числа')
a, b, c = map(int, input().split())

z = ((a == 0 or b == 0 or c == 0 ))
(z is False and print('Нет нулевых значений'))

z = (((a > 0 and a) or (b > 0 and b) or (c > 0 and c)) or 'Введены все нули!')
print('Первое ненулевое значение - ', z)

if a > b + c:
    print('a - b - c = ', a - b - c)

if a < b + c:
    print('b + c - a = ', b + c - a)

if (a > 50) and (b or c) > a:
    print('Вася')

if (a > 5) or (b and c == 7):
    print('Петя')
