from datetime import datetime
from functools import reduce

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Tiempo de ejecución: {round(time_elapsed.total_seconds(),4)} segundos')
    return wrapper

@execution_time
def random_func():
    factorial = reduce(lambda x,y:x*y,[i for i in range(2,70)])
    print(f'El factorial de 70 es: {factorial}')

def run():
    random_func()

if __name__ == '__main__':
    run()