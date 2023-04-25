from profesor import Profesor
from materia import Materia
from alumno import Alumno

class Universidad:
    pass

if __name__ == '__main__':
    materias = Materia()
    materias.listaMaterias(15, 'Computación')
    materias.listaMaterias(13, 'Álgebra')
    materias.listaMaterias(54, 'Programación')
    print(materias)
    pepeSand = Alumno(601, 'Pepe Sand', 'pepesand@alumno.com')
    pepeSand.inscribirseEnMateria(15)
    pepeSand.inscribirseEnMateria(13)
    pepeSand.inscribirseEnMateria(54)
    profesorHiguain = Profesor('Gonzalo Higuain', 'ghiguain@gmail.com')
    profesorHiguain.sumarAsistencia()
    pepeSand.sumarAsistencia()
    pepeSand.sumarAsistencia()
    pepeSand.sumarAsistencia()
    pepeSand.sumarAsistencia()
    print(profesorHiguain)
    print(pepeSand)