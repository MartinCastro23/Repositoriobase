class localizacion:
    def __init__(self, nombre, descripcion, coordenadas):
        self.nombre = nombre
        self.descripcion = descripcion
        self.salida = []
        self.coordenadas = coordenadas
        self.objetos = []

    def engadir(self, objetos):
        self.objetos.append(objeto)
        
    def arramplar(self, objetos):
        self.objetos.remove(objeto)
        return cousa

    def mostrar_info(self):
        print(f"Te encuentras en {sel.nombre}")
        print(self.descripcion)
        if self.objetos:
            print("Puedes ver los siguientes objetos:")
            for cousa in self.objetos:
                print(f"-{objeto.nombre}")

class mapamundi:
    def __init__(self):
        self.mapa = {}
        self.cartografiar()

    def cartografiar():
       comedor = localizacion("comedor", "Es un comedor asqueroso" , [0,1,1])
       comedor.salida.extend(["sur", "oeste", "arriba"])
       
       porche = localizacion("porche", "Es un porche sucio, con un banco lleno de telarañas" , [0,0,0])
       porche.salida.extend(["norte", "este"])
        
       salon = localizacion("salon", "Es un salon grande y oscuro" , [0,0,1])
       salon.salida.extend(["norte", "oeste"])
        
       cocina = localizacion("cocina", "Es una cocina pequeña y llena de mugre" , [0,1,0])
       cocina.salida.extend(["sur" , "este"])
        
       habitacion  = localizacion("habitacion", "Es una habitacion oscura y huele muy mal" , [1,1,1])
       habitacion.salida.extend(["abajo"])

        self.mapa[localizacion.comedor.coordenadas] = comedor
