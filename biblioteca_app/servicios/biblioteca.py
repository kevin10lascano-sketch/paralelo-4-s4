class Biblioteca:
    
    def __init__(self):

        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):

        self.libros.append(libro)
    
    def agregar_usuario(self, usuario):

        self.usuarios.append(usuario)
    
    def mostrar_libros(self):

        for libro in self.libros:
            print(libro)

    def mostrar_usuarios(self):

        for usuario in self.usuarios:
            print(usuario)