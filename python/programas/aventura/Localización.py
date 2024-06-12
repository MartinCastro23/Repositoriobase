from obxetos import *

class Localizacion:
    def __init__(self, nombre, descripcion, coordenadas):
        self.nombre = nombre
        self.descripcion = descripcion
        self.coordenadas = coordenadas
        self.objetos = []
        self.salida = []

    def engadír(self, objeto):
        self.objetos.append(objeto)

    def arramplar(self, objeto):
        self.objetos.remove(objeto)
        return objeto
        
    def mostrar_info(self):
        print(f"Te encuentras en {self.nombre}")
        print(self.descripcion)
        if self.objetos:
            print("Puedes ver los siguientes objetos:")
            for objeto in self.objetos:
                print(f"- {objeto.nombre}")

class Mapamundi:
    def __init__(self):
        self.mapa = {}
        self.cartografiar()
    
    def cartografiar(self):
        
        ganzua = objeto("Ganzua", "una ganzua vieja y rota")
        pera = objeto("Pera", "una pera rica y jugosa")
        tenedor = objeto("Tenedor", "un tenedor sucio y oxidado")
        peluche = objeto("Peluche", "un peluche de un zorro apoyado en el banco")
        croquetas = objeto("Croquetas", "un par de croquetas envasadas")
        
        porche = Localizacion("Porche", "ves un porche con un banco sucio y una puerta hacia la casa.", (0, 0, 0))
        self.mapa[tuple(porche.coordenadas)] = porche
        porche.engadír(peluche)
        
        cocina = Localizacion("Cocina", "una cocina muy sucia con una mesa en mal estado.", (0, 1, 0))
        self.mapa[tuple(cocina.coordenadas)] = cocina
        cocina.engadír(pera)
        
        salon = Localizacion("Salón", "un salón con un sofá lleno de polvo y una televisión rota.", (0, 0, 1))
        self.mapa[tuple(salon.coordenadas)] = salon
        salon.engadír(tenedor)
        
        comedor = Localizacion("Comedor", "un comedor con una mesa, 4 sillas y un cuadro aterrador.", (0, 1, 1))
        self.mapa[tuple(comedor.coordenadas)] = comedor
        comedor.engadír(croquetas)
        
        habitacion = Localizacion("Habitación", "hay una habitación con una cama rota y un armario cerrador.", (1, 1, 1))
        self.mapa[tuple(habitacion.coordenadas)] = habitacion
        habitacion.engadír(ganzua)
        
        