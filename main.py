from Curso import Curso
from estudiante import Estudiante


curso_uno = Curso("Dinamica",1,"Jose Nicolas Ponciano Guzman")
curso_dos = Curso("Termodinámica",2,"Daniel Molinero Hernandez")
curso_tres = Curso("Ecuaciones Diferenciales",3,"Doctora Betty")

estudiante_1 = Estudiante("Edson Jared Martinez Gomez", 19,22121048)
estudiante_2 = Estudiante("Manuel Alberto Tena García",20,22121034)


estudiante_1.agregar_curso(curso_uno)
estudiante_1.agregar_curso(curso_tres)

estudiante_2.agregar_curso(curso_uno)
estudiante_2.agregar_curso(curso_dos)


curso_uno.mostrar_info_curso()
curso_dos.mostrar_info_curso()
curso_tres.mostrar_info_curso()

estudiante_1.mostrar_informacion()
estudiante_2.mostrar_informacion()