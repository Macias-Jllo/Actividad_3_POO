class Cuenta:
    def __init__(self, saldo, tasa_anual):
        self._saldo = saldo
        self._numero_consignaciones = 0
        self._numero_retiros = 0
        self._tasa_anual = tasa_anual
        self._comision_mensual = 0

    def consignar(self, cantidad):
        self._saldo += cantidad
        self._numero_consignaciones += 1

    def retirar(self, cantidad):
        nuevo_saldo = self._saldo - cantidad
        if nuevo_saldo >= 0:
            self._saldo -= cantidad
            self._numero_retiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcular_interes(self):
        tasa_mensual = self._tasa_anual / 12
        interes_mensual = self._saldo * tasa_mensual
        self._saldo += interes_mensual

    def extracto_mensual(self):
        self._saldo -= self._comision_mensual
        self.calcular_interes()

    def imprimir(self):
        print(f"Saldo = ${self._saldo:.2f}")
        print(f"Comisión mensual = ${self._comision_mensual:.2f}")
        print(f"Número de transacciones = {self._numero_consignaciones + self._numero_retiros}")


class CuentaAhorros(Cuenta):
    def __init__(self, saldo, tasa):
        super().__init__(saldo, tasa)
        self.__activa = saldo >= 10000

    def consignar(self, cantidad):
        if self.__activa:
            super().consignar(cantidad)

    def retirar(self, cantidad):
        if self.__activa:
            super().retirar(cantidad)

    def extracto_mensual(self):
        if self._numero_retiros > 4:
            self._comision_mensual += (self._numero_retiros - 4) * 1000
        super().extracto_mensual()
        self.__activa = self._saldo >= 10000

    def imprimir(self):
        print(f"Saldo = ${self._saldo:.2f}")
        print(f"Comisión mensual = ${self._comision_mensual:.2f}")
        print(f"Número de transacciones = {self._numero_consignaciones + self._numero_retiros}\n")


class CuentaCorriente(Cuenta):
    def __init__(self, saldo, tasa):
        super().__init__(saldo, tasa)
        self._sobregiro = 0

    def retirar(self, cantidad):
        resultado = self._saldo - cantidad
        if resultado < 0:
            self._sobregiro -= resultado
            self._saldo = 0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad):
        if self._sobregiro > 0:
            residuo = self._sobregiro - cantidad
            if residuo > 0:
                self._sobregiro = residuo
            else:
                self._sobregiro = 0
                self._saldo += -residuo
        else:
            super().consignar(cantidad)

    def extracto_mensual(self):
        super().extracto_mensual()

    def imprimir(self):
        print(f"Saldo = ${self._saldo:.2f}")
        print(f"Comisión mensual = ${self._comision_mensual:.2f}")
        print(f"Número de transacciones = {self._numero_consignaciones + self._numero_retiros}")
        print(f"Valor de sobregiro = ${self._sobregiro:.2f}\n")

def main():
    print("Cuenta de ahorros")
    saldo_inicial = float(input("Ingrese saldo inicial = $"))
    tasa = float(input("Ingrese tasa de interés = "))
    
    cuenta = CuentaAhorros(saldo_inicial, tasa)

    cantidad_consignar = float(input("Ingresar cantidad a consignar = $"))
    cuenta.consignar(cantidad_consignar)

    cantidad_retirar = float(input("Ingresar cantidad a retirar = $"))
    cuenta.retirar(cantidad_retirar)

    cuenta.extracto_mensual()
    cuenta.imprimir()


if __name__ == "__main__":
    main()
