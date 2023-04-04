height = int(input('Введите ваш рост - '))
weight = int(input('Введите ваш вес - '))
BMI = round((weight/(height*height))*10000, 2)
print('Ваш индекс массы тела - ', BMI)
BMI= round(BMI)
skale = '20' + '='*28 + '50'
print(skale[:BMI-20], '|', skale[BMI-20:], sep='=')