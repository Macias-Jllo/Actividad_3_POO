class Persona:
    def __init__(self, nombre: str, direccion: str):
        self._nombre = nombre
        self._direccion = direccion

    def get_nombre(self) -> str:
        return self._nombre

    def get_direccion(self) -> str:
        return self._direccion

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def set_direccion(self, direccion: str):
        self._direccion = direccion


class Estudiante(Persona):
    def __init__(self, nombre: str, direccion: str, carrera: str, semestre: int):
        super().__init__(nombre, direccion)
        self._carrera = carrera
        self._semestre = semestre

    def get_carrera(self) -> str:
        return self._carrera

    def get_semestre(self) -> int:
        return self._semestre

    def set_carrera(self, carrera: str):
        self._carrera = carrera

    def set_semestre(self, semestre: int):
        self._semestre = semestre


class Profesor(Persona):
    def __init__(self, nombre: str, direccion: str, departamento: str, categoria: str):
        super().__init__(nombre, direccion)
        self._departamento = departamento
        self._categoria = categoria

    def get_departamento(self) -> str:
        return self._departamento

    def get_categoria(self) -> str:
        return self._categoria

    def set_departamento(self, departamento: str):
        self._departamento = departamento

    def set_categoria(self, categoria: str):
        self._categoria = categoria

def main():
    estudiante = Estudiante("Ana Gómez", "Calle 123", "Ingeniería", 5)
    print("== ESTUDIANTE ==")
    print("Nombre:", estudiante.get_nombre())
    print("Dirección:", estudiante.get_direccion())
    print("Carrera:", estudiante.get_carrera())
    print("Semestre:", estudiante.get_semestre())

    estudiante.set_carrera("Matemáticas")
    estudiante.set_semestre(6)
    print("\nDespués de actualizar:")
    print("Carrera:", estudiante.get_carrera())
    print("Semestre:", estudiante.get_semestre())

    profesor = Profesor("Carlos Ruiz", "Av. Siempre Viva 742", "Matemáticas", "Titular")
    print("\n== PROFESOR ==")
    print("Nombre:", profesor.get_nombre())
    print("Dirección:", profesor.get_direccion())
    print("Departamento:", profesor.get_departamento())
    print("Categoría:", profesor.get_categoria())

    profesor.set_departamento("Física")
    profesor.set_categoria("Asociado")
    print("\nDespués de actualizar:")
    print("Departamento:", profesor.get_departamento())
    print("Categoría:", profesor.get_categoria())

if __name__ == "__main__":
    main()
