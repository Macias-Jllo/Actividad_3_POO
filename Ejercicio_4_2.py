from enum import Enum

class Inmueble:
    def __init__(self, id_inmobiliario, area, direccion):
        self.id_inmobiliario = id_inmobiliario
        self.area = area
        self.direccion = direccion
        self.precio_venta = 0

    def calcular_precio_venta(self, valor_area):
        self.precio_venta = self.area * valor_area
        return self.precio_venta

    def imprimir(self):
        print(f"Identificador inmobiliario: {self.id_inmobiliario}")
        print(f"Área: {self.area}")
        print(f"Dirección: {self.direccion}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")

class InmuebleVivienda(Inmueble):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos):
        super().__init__(id_inmobiliario, area, direccion)
        self.num_habitaciones = num_habitaciones
        self.num_banos = num_banos

    def imprimir(self):
        super().imprimir()
        print(f"Habitaciones: {self.num_habitaciones}")
        print(f"Baños: {self.num_banos}")

class Casa(InmuebleVivienda):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos)
        self.num_pisos = num_pisos

    def imprimir(self):
        super().imprimir()
        print(f"Pisos: {self.num_pisos}")

class CasaRural(Casa):
    valor_area = 1500000

    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos, distancia_cabecera, altitud):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos)
        self.distancia_cabecera = distancia_cabecera
        self.altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a cabecera municipal: {self.distancia_cabecera} km")
        print(f"Altitud: {self.altitud} msnm\n")

class CasaUrbana(Casa):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos)

    def imprimir(self):
        super().imprimir()

class CasaConjuntoCerrado(CasaUrbana):
    valor_area = 2500000

    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos, valor_admon, piscina, deportes):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos)
        self.valor_admon = valor_admon
        self.piscina = piscina
        self.deportes = deportes

    def imprimir(self):
        super().imprimir()
        print(f"Valor administración: ${self.valor_admon}")
        print(f"Tiene piscina: {self.piscina}")
        print(f"Tiene campos deportivos: {self.deportes}\n")

class CasaIndependiente(CasaUrbana):
    valor_area = 3000000

    def imprimir(self):
        super().imprimir()
        print()

class Apartamento(InmuebleVivienda):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos)

    def imprimir(self):
        super().imprimir()

class ApartamentoFamiliar(Apartamento):
    valor_area = 2000000

    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, valor_admon):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos)
        self.valor_admon = valor_admon

    def imprimir(self):
        super().imprimir()
        print(f"Valor administración: ${self.valor_admon}\n")

class Apartaestudio(Apartamento):
    valor_area = 1500000

    def __init__(self, id_inmobiliario, area, direccion):
        super().__init__(id_inmobiliario, area, direccion, 1, 1)

    def imprimir(self):
        super().imprimir()
        print()

class TipoLocal(Enum):
    INTERNO = "Interno"
    CALLE = "Calle"

class Local(Inmueble):
    def __init__(self, id_inmobiliario, area, direccion, tipo_local):
        super().__init__(id_inmobiliario, area, direccion)
        self.tipo_local = tipo_local

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local: {self.tipo_local.value}")

class LocalComercial(Local):
    valor_area = 3000000

    def __init__(self, id_inmobiliario, area, direccion, tipo_local, centro_comercial):
        super().__init__(id_inmobiliario, area, direccion, tipo_local)
        self.centro_comercial = centro_comercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial: {self.centro_comercial}\n")

class Oficina(Local):
    valor_area = 3500000

    def __init__(self, id_inmobiliario, area, direccion, tipo_local, es_gobierno):
        super().__init__(id_inmobiliario, area, direccion, tipo_local)
        self.es_gobierno = es_gobierno

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental: {self.es_gobierno}\n")

    def main():
        print("Datos apartamento")
        apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
        apto1.calcular_precio_venta(ApartamentoFamiliar.valor_area)
        apto1.imprimir()

        print("Datos apartaestudio")
        aptestudio1 = Apartaestudio(12354, 50, "Avenida Caracas 30-15")
        aptestudio1.calcular_precio_venta(Apartaestudio.valor_area)
        aptestudio1.imprimir()

    if __name__ == "__main__":
        main()
