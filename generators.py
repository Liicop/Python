import time

def FiboIter(top):
    num1 = 0
    num2 = 1
    counter = 0

    while True:
        if counter >= top:
            print('\nSucesión finalizada')
            break
        
        counter += 1
        yield num1
        num1, num2 = num2, num1 + num2

for i in FiboIter(16):
    print(i, end=' ')