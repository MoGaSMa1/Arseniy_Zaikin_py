def decorator(func):    
    def wraper_decorator():
        if login == 'admin':
            func()
        else:
            print('Fail')
    return wraper_decorator

@decorator
def money():
    print('Сумма счета - 5$')

login = input('Login - ')
money()