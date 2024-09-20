from typing import List
from Estudiantes.estudiante import Estudiante
from Grupos.Grupo import Grupo
from Maestros.maestro import maestro
from Materias.materia import materia
from random import randint
from datetime import datetime

class Escuela:
    lista_estudiantes: List [Estudiante] = []
    lista_grupos: List[Grupo] = [] 
    lista_maestros: List [maestro] = []
    lista_materias: List [materia] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def generar_numero_control(self):
        #L - 2024 - longitud lista estudiantes +1 + random(0, 10000)
        numero_control = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0, 10000)}"

        return numero_control


    