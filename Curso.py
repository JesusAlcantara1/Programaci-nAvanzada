class Curso:
    nombre_curso = ""
    codigo_curso = 0
    profe = ""
    
    def __init__(self, nombre_curso, codigo_curso, profe):
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso
        self.profe = profe
        
    def mostrar_info_curso(self):
        print("\nInfo del curso")
        print("Curso: ",self.nombre_curso)
        print("Codigo: ",self.codigo_curso)
        print("Profesor: ",self.profe)