
class Persona():
    def __init__(self,name):
        self.nombre = name

    def saludar(self, friends_name):
        print(f'Hola {friends_name}, ¿Cómo estás?')

    def respuesta(self, friends_name):
        print(f'Hola {friends_name}, ¡estoy genial!\n')

Pepe = Persona('Pepe')
Carla = Persona('Carla')
Pepe.saludar(Carla.nombre)
Carla.respuesta(Pepe.nombre)

Carla.saludar(Pepe.nombre)
Pepe.respuesta(Carla.nombre)