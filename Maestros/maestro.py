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

    def mostrar_info_maestros(self):
        nombre_completo = f"{self.nombre}{self.apellido}"
        info = f"Numero de control: {self.numero_controlp}, nombre completo: {nombre_completo}, sueldo: {self.sueldo},rfc: {self.rfc}, fecha de nacimiento: {self.fecha_nacimiento}"
        return info
