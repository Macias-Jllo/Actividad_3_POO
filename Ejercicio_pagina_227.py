from enum import Enum

class Mascota:
    def __init__(self, nombre: str, edad: int, color: str):
        self.nombre = nombre
        self.edad = edad
        self.color = color

class Perro(Mascota):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde

    @staticmethod
    def sonido():
        print("Los perros ladran")

class PerroPequeno(Perro):
    class Raza(Enum):
        CANICHE = "Caniche"
        YORKSHIRE_TERRIER = "Yorkshire Terrier"
        SCHNAUZER = "Schnauzer"
        CHIHUAHUA = "Chihuahua"

    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool, raza: Raza):
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza

class PerroMediano(Perro):
    class Raza(Enum):
        COLLIE = "Collie"
        DALMATA = "Dálmata"
        BULLDOG = "Bulldog"
        GALGO = "Galgo"
        SABUESO = "Sabueso"

    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool, raza: Raza):
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza

class PerroGrande(Perro):
    class Raza(Enum):
        PASTOR_ALEMAN = "Pastor Alemán"
        DOBERMAN = "Doberman"
        ROTWEILLER = "Rotweiller"

    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool, raza: Raza):
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza

class Gato(Mascota):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto

    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean")

class GatoSinPelo(Gato):
    class Raza(Enum):
        ESFINGE = "Esfinge"
        ELFO = "Elfo"
        DONSKOY = "Donskoy"

    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float, raza: Raza):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza


class GatoPeloLargo(Gato):
    class Raza(Enum):
        ANGORA = "Angora"
        HIMALAYO = "Himalayo"
        BALINES = "Balinés"
        SOMALI = "Somalí"

    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float, raza: Raza):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza

class GatoPeloCorto(Gato):
    class Raza(Enum):
        AZUL_RUSO = "Azul Ruso"
        BRITANICO = "Británico"
        MANX = "Manx"
        DEVON_REX = "Devon Rex"

    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float, raza: Raza):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza

if __name__ == "__main__":
    toby = PerroPequeno(
        nombre="Toby",
        edad=2,
        color="Blanco",
        peso=4.5,
        muerde=False,
        raza=PerroPequeno.Raza.CANICHE
    )
    print(f"{toby.nombre} es un {toby.raza.value}")
    Perro.sonido() 

    luna = GatoSinPelo(
        nombre="Luna",
        edad=3,
        color="Rosa",
        altura_salto=1.8,
        longitud_salto=2.5,
        raza=GatoSinPelo.Raza.ESFINGE
    )
    print(f"{luna.nombre} salta {luna.altura_salto} metros de altura")
    Gato.sonido()
