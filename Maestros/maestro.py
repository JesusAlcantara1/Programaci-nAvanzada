class maestro:
    numero_control: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float 
    ano_nacimiento: int

    def __init__(self, nombre:str, apellido: str, numero_control: str, rfc: str, sueldo: float, ano_nacimiento: int ):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_control = numero_control
        self.rfc = rfc
        self.sueldo =  sueldo
        self.ano_nacimiento = ano_nacimiento
