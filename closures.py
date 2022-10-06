def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo se permiten cadenas'
        return string*n
    return repeater

def make_division_by(n): #divisor
    def dividend(x): #dividendo
        return x/n
    return dividend


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('José'))

    print('-'*50)

    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))
    division_by_18 = make_division_by(18)
    print(division_by_18(54))

if __name__ == '__main__':
    run()