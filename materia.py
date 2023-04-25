
class Materia:
    def __init__(self):
        self.materias = {}

    def listaMaterias(self, codigo, materia):
        self.materias[codigo] = materia

    def obtenerMaterias(self, codMat):
        return self.materias.get(codMat)

    def __repr__(self):
        return f'{self.materias}'