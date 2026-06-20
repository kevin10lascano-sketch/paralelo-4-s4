from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca

libro1 = Libro(
    "Python para Principiantes",
    "Juan Pérez",
    "ISBN001"
)

libro2 = Libro(
    "Programación Orientada a Objetos",
    "María Gómez",
    "ISBN002"
)


usuario1 = Usuario(
    "Carlos López",
    "carlos@correo.com"
)

biblioteca = Biblioteca()

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.agregar_usuario(usuario1)

print("=== LIBROS REGISTRADOS ===")
biblioteca.mostrar_libros()

print("\n=== USUARIOS REGISTRADOS ===")
biblioteca.mostrar_usuarios()

