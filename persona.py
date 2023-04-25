class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def sumarAsistencia(self):
        self.asistencia += 1
    
    def nuevoNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre