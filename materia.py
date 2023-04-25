
class Materia:
    #? Se inicializa una instancia en None (Instancia inexistente)
    instancia = None

    #? Método que devuelve None, en caso de no haber instancia o devuelve instancia en caso de haber
    #? sido creadas, esto sirve para que se puedan llamar desde otras clases, habiendo instanciado
    #? objetos dentro de esta clase. 
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