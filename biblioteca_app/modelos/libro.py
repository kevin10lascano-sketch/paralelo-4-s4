class Libro:
    
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
    
    def mostrar_informacion(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nISBN: {self.isbn}"
    
    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"