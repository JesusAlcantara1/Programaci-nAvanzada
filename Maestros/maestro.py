class maestro:
    NumeroControl: str
    Nombre: str
    Apellido: str
    rfc: str
    sueldo: float 

    def __init__(self, Nombre:str, Apellido: str, NumeroControl: str, rfc: str, sueldo: float):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.rfc = rfc
        self.sueldo =  sueldo 
