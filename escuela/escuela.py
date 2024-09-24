from typing import List
from Estudiantes.estudiante import Estudiante
from Grupos.Grupo import Grupo
from Maestros.maestro import maestro
from Materias.materia import Materia
from random import randint
from datetime import datetime

class Escuela:
    lista_estudiantes: List [Estudiante] = []
    lista_grupos: List[Grupo] = [] 
    lista_maestros: List [maestro] = []
    lista_materias: List [Materia] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
          
    def registrar_maestro(self, maestro: maestro):
        self.lista_maestros.append(maestro)

    def generar_numero_control(self):
        #L - 2024 - longitud lista estudiantes +1 + random(0, 10000)
        numero_control = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0, 10000)}"

        return numero_control

    def generar_numero_control_maestro (self, maestro: maestro):
        ano_nacimiento = maestro.ano_nacimiento
        dia = datetime.now().day
        aleatorio = randint(500, 5000)
        dos_letras_nombre = maestro.nombre[:2].upper()
        dos_letras_rfc = maestro.rfc[-2:].upper()
        longitud_maestros = len(self.lista_maestros) + 1
        
        numero_control = f"M{ano_nacimiento}{dia}{aleatorio}{dos_letras_nombre}{dos_letras_rfc}{longitud_maestros}"
        return numero_control
    
    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)
        
    def generar_id_materia(self, nombre, semestre, creditos):
        #MT{ultimos 2 digitos del nombre}{semestre}{cantidad creditos}{randint(1,1000)}"
        nombre = nombre.upper()
        digitos_nombre = nombre[-2:]
        semestre = semestre
        cantidad_creditos = creditos
        
        id = f"MT{digitos_nombre}{semestre}{cantidad_creditos}{randint(1,1000)}"
        return id


        