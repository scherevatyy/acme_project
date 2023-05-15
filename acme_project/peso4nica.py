import time


def sleep_one_sec():
    time.sleep(1)
    return 'Результат первой функции.'
        

def sleep_two_sec():
    time.sleep(2)
    return 'Результат второй функции.'

# Функция time_of_function()
# принимает на вход тестируемую функцию
# и возвращает результат измерений:
def time_of_function(func):
    # Объявляем внутреннюю функцию — её-то и вернём, когда опишем.
    def wrapper():
        start_time = time.time()
        print('Время пошло')

        # Вызываем полученную функцию и 
        # cохраняем результат её выполнения в переменную.
        result = func()

        execution_time = round(time.time() - start_time, 1)
        # Можем использовать результат выполнения полученной функции:
        print(f'Через {execution_time} сек функция вернула «{result}»')
        # Возвращаем результат выполнения полученной функции.
        return result
    # Возвращаем функцию wrapper, но не вызываем её:
    return wrapper 