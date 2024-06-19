from obxetos import *

class localizacion:
	def __init__(self, nombre, descripcion, coordenadas):
		self.nombre = nombre
		self.descripcion = descripcion
		self.salida = []
		self.coordenadas = coordenadas
		self.objetos = []
		self.objetos_ocultos = self.objetos.copy()

	def añadir(self, objeto):
		self.objetos.append(objeto)
		self.objetos_ocultos.append(objeto)
  
	def arramplar(self, objeto):
		self.objetos.remove(objeto)
		return objeto

	def mostrar_info(self):
		print(f"Te encuentras en: {self.nombre}")
		print(self.descripcion)

	def buscar(self):
		if self.objetos_ocultos:
			print("Has encontrado los siguientes objetos:")
		for objeto in self.objetos_ocultos:
			print(f"- {objeto.nombre}")
			self.objetos_ocultos.clear()
		else:
			print("No hay nada más que encontrar aquí")

	def buscar(self):
		if self.objetos_ocultos:
			print("Has encontrado los siguientes objetos:")
			for objeto in self.objetos_ocultos:
				print(f"- {objeto.nombre}")
			self.objetos_ocultos.clear()
		else:
			print("No hay nada más que encontrar aquí")

class Mapamundi:
	def __init__(self):
		self.mapa = {}
		self.cartografiar()

	def cartografiar(self):
		comedor = localizacion("Comedor", "Es un comedor asqueroso" , [0,1,1])
		comedor.salida.extend(["sur", "oeste", "arriba"])
       
		porche = localizacion("Porche", "Es un porche sucio, con un banco lleno de telarañas" , [0,0,0])
		porche.salida.extend(["norte", "este"])
        
		salon = localizacion("Salón", "Es un salón grande y oscuro" , [0,0,1])
		salon.salida.extend(["norte", "oeste"])
        
		cocina = localizacion("Cocina", "Es una cocina pequeña y llena de mugre" , [0,1,0])
		cocina.salida.extend(["sur" , "este"])

		terraza = localizacion("Terraza", "Es una terraza fria y descuidada" ,[2,1,1])
		terraza.salida.extend(["sur", "oeste", "arriba", "arriba"])
        
		habitacion  = localizacion("Habitación", "Es una habitación oscura y huele muy mal" , [1,1,1])
		habitacion.salida.extend(["abajo"])
        
		self.mapa[tuple(comedor.coordenadas)] = comedor
		self.mapa[tuple(porche.coordenadas)] = porche
		self.mapa[tuple(salon.coordenadas)] = salon
		self.mapa[tuple(cocina.coordenadas)] = cocina
		self.mapa[tuple(habitacion.coordenadas)] = habitacion

		pera = objeto("Pera", "Es una pera verde y jugosa")
		bolsa = objeto("Bolsa", "Es una bolsa pequeña llena de polvos")
		portatil = objeto("Portatil", "Es un portatil linus viejo")
		llaves = objeto("Llaves", "Has visto unas llaves antiguas")
		arma = objeto("Arma", "Ves un arma de caza")
		rastrillo = objeto("Rastrillo", "Hay un rastrillo oxidado apoyado en la esquina")
		
		comedor.añadir(pera)
		cocina.añadir(bolsa)
		habitacion.añadir(portatil)
		porche.añadir(llaves)
		salon.añadir(arma)
		terraza.añadir(rastrillo)        