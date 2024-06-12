from Localización import *
from obxetos import *
from personaxes import *

class Juego:
    def __init__(self):
        self.mundo = Mapamundi()
        self.jugador = Personaje("André", self.mundo.mapa[(0, 0 , 0)])
    def jugar(self):
        print("¡Bienvenido a tu mayor pesadilla!")
        self.jugador.lugar_actual.mostrar_info()
        while True:
            comando = input("\n¿Qué vas a hacer ahora? ").lower().split()
            if len(comando) == 0:
                continue

            if comando[0] in ["ir", "mover"]:
                if len(comando) > 1:
                    self.jugador.mover(comando[1], self)
                else:
                    print("¿En qué dirección quieres ir?")

            elif comando[0] == "recoger":
                if len(comando) > 1:
                    self.jugador.recoger(" ".join(comando[1:]))
                else:
                    print("¿Qué quieres recoger?")

            elif comando[0] == "inventario":
                self.jugador.mostrar_inventario()

            elif comando[0] in ["salir", "exit"]:
                print("¡Gracias por jugar y de nada por crear el juego!")
                break

            else:
                print("No te entiendo explícate mejor.")

# Iniciar el juego
if __name__ == "__main__":
    juego = Juego()
    juego.jugar()