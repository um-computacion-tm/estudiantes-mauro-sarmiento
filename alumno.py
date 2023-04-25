from persona import Persona
from materia import Materia


class Alumno(Persona):
    def __init__(self, legajo, nombre, email):
        self.legajo = legajo
        self.asistencia = 0
        self.materias_alumno = []
        self.claseMateria = Materia()
        super().__init__(nombre, email)


    def inscribirseEnMateria(self, codigoMateria):
        materia = Materia().obtenerMaterias(codigoMateria)
        if materia is not None:
            self.materias_alumno.append(materia)


    def __repr__(self):
        return f'### {self.legajo}, {self.nombre}, {self.email}, {self.asistencia}, {self.materias_alumno} ###'
