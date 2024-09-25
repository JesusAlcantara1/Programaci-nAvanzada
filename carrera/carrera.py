from typing import List
from Materias.materia import Materias
from Estudiantes.estudiante import Estudiante
from semestre.semestre import Semestre

class Carrera:
    matricula: str
    nombre: str
    materias: List[Materias]
    numero_semestre= int
    semestres= List[Estudiante]
    semestres: List[Semestre]