from persona import Persona

class Profesor(Persona):

    def __init__(self, nombre, email):
        self.asistencia = 0
        super().__init__(nombre, email)


    def __repr__(self):
        return f'### {self.nombre}, {self.email}, {self.asistencia} ###'