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

    
    
    
    def generar_numero_control(self):
        #L - 2024 - longitud lista estudiantes +1 + random(0, 10000)
        numero_control = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0, 10000)}"
        return numero_control

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
          


    def registrar_maestro(self, maestro: maestro):
        self.lista_maestros.append(maestro)

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
    

    def listar_estudiantes(self):
        print("** Estudiante **")    
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante(self))

    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control.strip(): 
                self.lista_estudiantes.remove(estudiante)
                print(f"Estudiante {estudiante.nombre} {estudiante.apellido}, eliminado exitosamente.\n")
                return 
            
        print(f"NO se encontro unn estudiante con el numero de control: {numero_control}")
    

    def listar_maestros(self):
        print("** Maestros **")    
        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestros())


    def eliminar_maestro(self, numero_controlp: str):
        for maestro in self.lista_maestros:
            if maestro.numero_controlp == numero_controlp.strip(): 
                self.lista_maestros.remove(maestro)
                print(f"Maestro {maestro.nombre} {maestro.apellido}, eliminado exitosamente.\n")
                return 
            

    def listar_materias(self):
        print("** Materias **")    
        for materias in self.lista_materias:
            print(materias.mostrar_info_materia())


    def eliminar_materia(self, id_materia: str):
        for materia in self.lista_materias:
            if materia.id == id_materia.strip(): 
                self.lista_materias.remove(materia)
                print(f"Materia {materia.nombre}, eliminado exitosamente.\n")
                return 
    






        