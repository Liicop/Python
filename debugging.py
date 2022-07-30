def divisores(dividendo):
    divisors = []
    #divisors = [i for i in range(1,dividendo+1) if dividendo%i==0]
    for divisor in range(1,dividendo+1):
        if(dividendo%divisor==0):
            divisors.append(divisor) 
    
    return divisors

def run():
    n = int(input("Ingrese un numero para hallar sus divisores: "))
    print(f'Los divisores de {n} son {divisores(n)}')

if __name__ == "__main__":
    run()