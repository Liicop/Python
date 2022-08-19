class Paladins_champ:
    def __init__(self,name):
        self.name = name
        
    def moverse(self):
        print('{} se está moviendo'.format(self.name))
    
    def capturar(self):
        print('{} está capturando el punto'.format(self.name))
    
    def damage(self):
        print('{} hace daño'.format(self.name))

class Flank(Paladins_champ):
    def __init__(self, name, harm):
        super().__init__(name)
        self.harm = harm

    def moverse(self):
        print('{} de rol flanco, está volando'.format(self.name))
    
    def damage(self):
        print('{} hace {} de daño'.format(self.name, self.harm))

class Healer(Paladins_champ):
    def __init__(self, name, heal):
        super().__init__(name)
        self.heal = heal

    def healing(self):
        print('{} cura {} a sus aliados'.format(self.name, self.heal))


def run():
    Cassie = Paladins_champ('Cassie')
    Cassie.moverse()
    Cassie.damage()

    Maeve = Flank('Maeve', 800)
    Maeve.damage()
    Maeve.moverse()
    Maeve.capturar()

    MalDamba = Healer('MalDamba', 700)
    MalDamba.healing()
    MalDamba.capturar()
    MalDamba.moverse()


if __name__ == '__main__':
    run()