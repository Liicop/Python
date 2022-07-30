def division_entre_cero():

    try:
        divisor = int(input("Ingrese un divisor: "))
        if divisor < 0:
            raise ValueError("Ingrese solo números positivos")
        print(f' 1/{divisor} es {round(1/divisor,3)}')
    except ZeroDivisionError as e:
        print(e)
    except ValueError as error:
        print(error)
    else:
        print("Divisor != 0, ok")
    finally:
        print("Program executed")

def run():
    division_entre_cero()

if __name__ == "__main__":
    run()