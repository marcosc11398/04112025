class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

class AnimalSalvaje(Animal):
    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)
        self.nombre = nombre
        self.sonido = sonido    

class Leon (AnimalSalvaje):
    def __init__(self, nombre, sonido, caracteristica="Rey de la selva"):
        super().__init__(nombre, "sonido")
        self.caracteristica = caracteristica
        

class mono (AnimalSalvaje):
    def __init__(self, nombre, sonido , caracteristica="Muy jugueton"):
        super().__init__(nombre, sonido)
        sonido = "uau uau"
    

class lobo (AnimalSalvaje):
    def __init__(self, nombre, sonido , caracteristica="Cazador en manada"):
        super().__init__(nombre, sonido) 
        sonido = "Auuuu"   

class elefante (AnimalSalvaje):
    def __init__(self, nombre, sonido , caracteristica="El animal terrestre mas grande"):
        super().__init__(nombre, sonido)
        

class hiena (AnimalSalvaje):
    def __init__(self, nombre, sonido , caracteristica="Risa siniestra"):
        super().__init__(nombre, sonido)
        