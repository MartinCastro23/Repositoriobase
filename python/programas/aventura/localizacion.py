class localizacion:
	def __init__(self, nombre, descripcion, coordenadas):
		self.descripcion = descripcion
		self.salida = []
		self.coordenadas = coordenadas
		self.objetos = []
		self.id = nombre

	def engadir(self, cousa):
		self.objetos.append(cousa)
	
	def arramplar(self, cousa):
		self.objetos.remove(cousa)
		return cousa

comedor = localizacion("comedor", "Es un comedor asqueroso", [0,1,1])
porche = localizacion("porche", "En el porche hay un banco podrido", [0,0,0])
salon = localizacion("salon", "El salon esta helado", [0,0,1])
cocina = localizacion("cocina", "Es una concina mugrienta", [0,1,0])
habitacion = localizacion("habitacion", "La habitacion esta destrozada", [1,1,1])


comedor.salida.extend(["oeste,sur,arriba"])
porche.salida.extend(["norte,este"])
salon.salida.extend(["norte"])
cocina.salida.extend(["sur,este"])
habitacion.salida.extend([""])


print (comedor.descripcion)
print ("Las salidas posibles son:",comedor.salida) 

print (porche.descripcion)
print ("Las salidas posibles son:",porche.salida) 

print (salon.descripcion)
print ("Las salidas posibles son:",salon.salida) 

print (cocina.descripcion)
print ("Las salidas posibles son:",cocina.salida) 

print (habitacion.descripcion)
print ("Las salidas posibles son:",habitacion.salida) 
		
		

#Crear una clase de personaje que tenga como propiedad nombre,
 puntos de vida y un metodo ir