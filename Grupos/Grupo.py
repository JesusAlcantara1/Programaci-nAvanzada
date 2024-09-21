from typing import List
from Estudiantes.estudiante import Estudiante 
from Maestros.maestro import maestro
from Materias.materia import materia


class Grupo:
    id:int 
    estudiantes: List [Estudiante] = []
    maestros: List [maestro] = []
    materias: List [materia] = []
    tipo: chr
    