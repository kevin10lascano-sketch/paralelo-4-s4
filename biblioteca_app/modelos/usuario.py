class Usuario:

    def __init__(self, nombre, correo):

        self.nombre = nombre
        self.correo = correo

    def mostrar_informacion(self):
        return f"{self.nombre} ({self.correo})"

    def __str__(self):
        return self.nombre