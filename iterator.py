import time

class FiboIter:

    def __init__(self, top=0):
        self. top = top

    def __iter__(self):  #aquí van los elementos necesarios para la sucesión
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self): #aquí van las restricciones, operaciones, etc., para que se cumpla la sucesión
        
        if self.top or self.counter >= self.top:
            print('Finished')
            raise StopIteration() 
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux

class iterator:
    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.valor = 0
        return self
    
    def __next__(self):
        if not self.max or self.valor < self.max:
            value = self.valor
            self.valor += 1
            return value   


Fibonacci = FiboIter()
print(Fibonacci.__iter__())
for i in Fibonacci:
    print(i)
    time.sleep(0.5)



'''
my_iter = iterator(10)
print(my_iter.__iter__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())

print('*'*50)

iter1 = [i for i in range(9)]
iter2 = iter(iter1)

def iteration(iter2):
    while True:
        try:
            print(next(iter2))
        except StopIteration:
            break

iteration(iter2)'''