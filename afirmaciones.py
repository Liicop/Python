def square_root(raices):
    result = []
    for i in raices:
        assert type(i) == int, f'{i} no es un entero'
        assert i>=0, "Número imaginario"
        result.append(round(i**0.5,2))

    return result
    
raices = [8,'a',87,25]

print(square_root(raices), "---", type(square_root(raices)))