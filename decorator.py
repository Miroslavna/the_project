login = str(input("Введите логин: "))

def decorator(balance):
    def wrapper_decorator(*args, **kwargs):
        if login != 'admin':
            print('Доступ запрещен')
            return
        value = balance(*args, **kwargs)

        return value 
    return wrapper_decorator
@decorator 
def balance():
    print('236$')

balance()