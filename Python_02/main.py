height = int(input("Введите ваш рост - "))
weight = int(input('Введите ваш вес - '))
BMI = round((weight/(height*height))*10000, 2)
print('Ваш индекс массы тела - ', BMI)
BMI= round(BMI)
skale = ['20 ', "= "*30, ' 50']
skale = ''.join(skale)
skale = skale.split(' ')
skale[BMI-20] = '|'
skale = ''.join(skale)
print(skale)