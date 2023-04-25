
class Materia:
    instancia = None

    def __new__(self):
        if self.instancia is None:
            self.instancia = super().__new__(self)
            self.instancia.materias = {}
        return self.instancia

    def listaMaterias(self, codigo, materia):
        self.materias[codigo] = materia

    def obtenerMaterias(self, codMat):
        return self.materias.get(codMat)
    

    def __repr__(self):
        return f'{self.materias}'