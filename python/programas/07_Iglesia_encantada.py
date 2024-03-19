#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Importar los módulos que necesitaremos
import time

# Varias listas con terminología usada en el juego
verbos = ['ir', 'coger', 'abrir', 'atacar', 'hablar', 'beber', 'comer', 'saltar', \
        'subir', 'bajar', 'inventario','examinar']
objetos = ['llave', 'crucifijo', 'copa', 'vaso', 'pan', 'hostia']
direcciones = ["norte", "sur", "este", "oeste"]

# Mapa de salidas de cada habitación, identificadas por 3 números, respectivamente,
# el piso, la fila y la columna
salidas = {}
salidas[(1,1,1)] = ["este"]
salidas[(1,1,2)] = ["oeste","sur"]
salidas[(1,1,3)] = ["sur"]
salidas[(1,2,1)] = ["este"]
salidas[(1,2,2)] = ["oeste","norte","este"]
salidas[(1,2,3)] = ["oeste","norte"]
salidas[(2,1,1)] = ["sur"]
salidas[(2,1,2)] = ["este"]
salidas[(2,1,3)] = ["oeste","norte","sur"]
salidas[(2,2,1)] = ["norte","este"]
salidas[(2,2,2)] = ["oeste","este"]
salidas[(2,2,3)] = ["oeste","norte"]

# Función que se encarga de describir cada sala, identificada como previamente
# se ha comentado por una tupla de tres números.
def describir(p,f,c):
    # p es el piso
    # f la fila
    # c la columna
    sala = (p,f,c)
    print ("-----------------------------------------------------------------------")
    if sala == (1,1,1):
       print ("Ves una tumba en un altar en el centro de la habitación.")
       print ("Te da la sensación que hay algo dentro de la tumba ")
    elif sala == (1,1,2):
        print ('Estás en la entrada de a iglesia. Todo está oscuro y húmedo')
        if monjeVivo:
           print ('Escuchas ruídos extraños y tu miedo aumenta.')
    elif sala == (1,1,3):
       print ("Una antorcha encendida ilumina un baúl. Te preguntas quien encendió eso")
    elif sala == (1,2,1):
       print ("Ves una gran larga mesa. Sobre ella, algunos trozos de pan y restos líquidos en copas rotas.")
    elif sala == (1,2,2):
        print ("Una escalera  de caracol demadera podrida conduce hacia arriba.")
        if monjeVivo:
           print ("En algún lugar se ecucha a alguien moverse de lado a lado.")
    elif sala == (1,2,3):
       print ("En el suelo hay una copa. Las paredes parcen que se van a venir abajo.")
    elif sala == (2,1,1):
        print ("En una esquina hay vaso con líquido en su interior.")
        if monjeVivo:
           print ("Hay unos murmullos de fondo que parece de otro idioma. No logras entender nada.")
    elif sala == (2,1,2):
        if monjeVivo:
           print ("Un monje horrendo se te queda mirando fijamente.")
           print ("Detrás de él puedes observar varias velas y un libro abierto.")
        else:
           print ('El cadaver de un monje descansa en el suelo junto a las velas y un libro.')
    elif sala == (2,1,3):
        print ('La habitación está desierta...')
        if monjeVivo:
           print ('...pero notas como si la atmósfera se hiciese cada vez más densa.')
    elif sala == (2,2,1):
       print ("Un agugero en el centro de la habitación llama tu atención. El suelo no parece muy estable ")
    elif sala == (2,2,2):
       print ("Estás en el piso superior. No hay casi luz y casi te dan ganas")
       print ("de volver a bajar corriendo y salir de ahí")
    elif sala == (2,2,3):
        print ("Hay unos trozos de hostia en una estantería. Un ruído metálico")
        print ("produce un sonido rítmico y espeluznante.")
    # Indicamos hacia qué direcciones puede moverse el jugador
        print ('Direcciones posibles:',)
        for s in salidas[sala]:
            print (s,)
            print ()
            print ("-----------------------------------------------------------------------")

# Función que muestra en pantalla la introducción del Juego, con pausas.     
def intro():
   print ("Ante ti está la Iglesia abandonada de Santalucía, ")
   print ("solo viendola un  escalofrío te recorre todo en cuerpo, pero has perdido una apuesta y tienes que entrar. ")
   print ("Según dicen, dentro se encuentra un monje custodiando el libro sagrado de San Benito")
   time.sleep(1)
   print ()
   print ("Cojes fuerzas, te arrepientes)
   por aceptar la apuesta y entras a la iglesia...")
   time.sleep(1)
   print ()
   input("Pulsa <intro> para empezar el juego.")

# Función que se encarga de los actos de comer y beber.   
def comerBeber(v,c):
    # v es el verbo; comer o beber
    # c es lo que se quiere comer o beber
    
    # Declarar los globales
    global inventario, juegoAcabado, haComido, haBebido
    
    #Comprobar que se lleva lo que se quiere comer
    if c not in inventario:
        print ('No tienes ' + c)
        return
    
    # Caso de comer...
    if v == 'comer':
        # ... pan
        if c == 'pan':
            print ('Comes el pan y te sientes con más fuerza y energía.')
            # Activar el indicador de alimentado
            haComido = True
            # Eliminar del inventario, pues se ha comido
            inventario.remove(c)
            return
        # ... hostia
        elif c == 'hostia':
            print ('¡Horror! un dolor insoportable te invade...')
            time.sleep(1)
            print ('y mueres retorciendote como una serpiente por la comida en mal estado')
            # Activar el indicador de fin de juego
            juegoAcabado = True
            return
        # ... cualquier otra cosa
        else:
            print ('No puedo comer ' + c)
            return
    # caso de beber
    else:
         # ... vaso
        if c == 'vaso':
            print ('Bebes del vaso... agua cristalina. ¡Qué bien!')
            # Activar el indicador de alimentado
            haBebido = True
            # Eliminar del inventario, pues se ha comido
            inventario.remove(c)
            return
        # ... copa
        elif c == 'copa':
            print ('¡Sientes un mareo momentáneo...')
            time.sleep(1)
            print ('... y mueres fulminantemente')
            # Activar el indicador de fin de juego
            juegoAcabado = True
            return
        # ... cualquier otra cosa
        else:
            print ('No puedo beber ' + c)
            return

# Función que procesa las acciones del jugador ('parser')   
def procesar(instrucciones):
    # Hay que declarar como globales las variables que pueden modificarse
    global piso, fila, columna, juegoAcabado, inventario, yaDescrito, sinLlave
    global agujeroAlSur, bAbierto, tienecrucifijo, monjeActivo, monjeVivo
    # Si no se ha escrito nada, no hacer nada
    if instrucciones == '':
        return
    # Mostrar ayuda si se solicita
    if instrucciones == 'ayuda':
        print ( 'Debes usar verbos en infinitivo y, si lo necesitas, un nombre.'   )
        print ( 'Acciones disponibles:')
        for i in verbos:
           print ( i,)
        print ()
        return
    # Separar la acción en palabras
    palabras = instrucciones.split()
    # El verbo ha de ser siempre el primero
    verbo = palabras[0]
    # Si el verbo es desconocido, no hacer nada y volver a preguntar
    if verbo not in verbos:
        print ( "Perdona, no te entiendo")
        return
    # Si el verbo es 'ir'...
    if verbo == 'ir':
        # Comprobar que va acompañado de una direección
        if len(palabras) != 2 or palabras[1] not in direcciones:
            print ( "No entiendo a dónde tengo que ir.")
            return
        # Almacenar la dirección en la variable donde
        donde = palabras[1]
        # Si la dirección elegida no está disponible, comunicarlo
        if donde not in salidas[(piso, fila, columna)]:
            print ( "No puedo ir hacia el " + donde)
            return
        # Desplazarse en la dirección solicitada
        elif donde == "norte":
            # Hay una dos excepciones: La primera es la puerta trampa del segundo
            # piso. Activar el indicador de fin de juego...
            if fila == 1:
                print ( "¡La puerta era una trampa!")
                time.sleep(1)
                print ( "Al otro lado hay un precipico y te despeñas por él...")
                juegoAcabado = True
                return
            elif (fila,columna) == (2,1) and not agujeroAlSur:
                # La segunda es cuando se ha atraviesa el agujero sin saltar
                print ( 'Avanzas sin cuidado y te adelantas sobre el agujero...')
                time.sleep(1)
                print ( '¡Caes a la profundidad y la oscuridad del submundo!')
                juegoAcabado = True
                return
            fila = fila - 1
        elif donde == "sur":
            fila = fila + 1
        elif donde == "este":
            # Hay una excepción: Atravesar el agujero sin saltar...
            if (fila,columna) == (2,1) and agujeroAlSur:
                print ( "¡Te has olvidado del agujero!")
                time.sleep(1)
                print ( "¡La sima del agujero se te traga sin clemencia...")
                juegoAcabado = True
                return
            columna = columna + 1
        else:
            columna = columna - 1
        # Una vez que el jugador se ha movido, confirmarlo y activar el
        # indicador de describir la nueva sala
        print ( "Vas hacia el " + donde)
        yaDescrito = False
        return
    # Si el verbo es 'saltar'...
    if verbo == 'saltar':
        # Comprobar que va acompañado de una direección
        if len(palabras) != 2:
            print ( "No entiendo qué tengo que saltar.")
            return
        # Almacenar lo que se salta
        elQue = palabras[1]
        # Si no es el agujero, comunicarlo
        if elQue != 'agujero' :
            print ( "Qué tontería...")
            return
        # saltar agujero
        else:
            if (piso,fila,columna) != (2,2,1):
               print ( 'No hay ningún agujero que saltar.')
            else:
                print ( 'Saltas el agujero con agilidad...')
                time.sleep(1)
                print ( '... y lo dejas a tus espaldas.')
                agujeroAlSur = not agujeroAlSur
        return
    # Comprobar que 'subir' ocurre sólo al pie de la escalera.
    if verbo == 'subir':
        if (piso,fila,columna) == (1,2,2):
            print ( 'Subes por la escalera.')
            piso = piso + 1
            yaDescrito = False
        else:
           print ( 'No puedo subir.')
        return
    # Comprobar que bajar ocurre sólo en lo alto de la escalera
    if verbo == 'bajar':
        if (piso,fila,columna) == (2,2,2):
            print ( 'Bajas por la escalera.')
            piso = piso - 1
            yaDescrito = False
        # ¡Ojo, una excepción! Si se quiere bajar por el agujero mágico
        # el jugador muere y hay que activar el indicador de fin de juego.
        elif (piso,fila,columna) == (2,2,1):
            print ( 'Desciendes por el agujero...')
            time.sleep(0.5)
            print ( 'Unos ojos brillantes te observan desde el fondo.')
            print ( '¡Algo te agarra y te devora!')
            juegoAcabado = True
        else:
           print ( 'No puedo bajar.')
        return
    # Gestionar el comer o el beber.
    if verbo == 'comer' or verbo == 'beber':
        # Asegurarse que se indica lo que se quiere comer
        if len(palabras) == 1:
            print ( 'Perdona... ¿el qué?')
            return
        else:
            # Enviar a la función que gestiona el alimento, tanto si
            # come o bebe como el qué
            comerBeber(verbo, palabras[1])
            return
    # Coger objetos
    if verbo == 'coger':
        # Asegurarse que se indica lo que se quiere coger
        if len(palabras) == 1:
            print ( 'Perdona... ¿coger qué?')
            return
        else:
            objeto = palabras[1]
            # Comprobar que el objeto está en la sala
            if objeto in mapa[(piso,fila,columna)]:
                # Añadirlo al inventario y quitarlo de la sala
                inventario.append(objeto)
                mapa[(piso,fila,columna)].remove(objeto)
                # Confirmar la acción
                print ( 'Llevas contigo: ' + objeto)
            elif (piso,fila,columna)== (1,2,1) and objeto == "llave" and sinLlave:
                # Añadir la llave al inventario
                inventario.append(objeto)
                sinLlave = False
                # Confirmar la acción
                print ( 'Llevas contigo: ' + objeto)
            elif (piso,fila,columna)== (1,1,3) and objeto == 'crucifijo' and bAbierto:
                if tienecrucifijo:
                   print ( 'Ya tienes la crucifijo.')
                else:
                    # Añadir la crucifijo al inventario
                    inventario.append(objeto)
                    tienecrucifijo = True
                    # Confirmar la acción
                    print ( 'Llevas contigo: ' + objeto)
            else:
               print ( 'No puedo hacer eso.')
            return
    # Abrir objetos
    if verbo == 'abrir':
        # Asegurarse que se indica lo que se quiere abrir
        if len(palabras) == 1:
            print ( 'Perdona... ¿abrir qué?')
            return
        else:
            objeto = palabras[1]
            # Comprobar que el objeto está es el correcto
            if (piso,fila,columna) == (1,1,3) and objeto == 'baúl':
                if bAbierto:
                   print ( 'El baúl ya está abierto.')
                else:
                    #abrir baúl
                    bAbierto = True
                    print ( 'Has abierto el baúl.')
            elif (piso,fila,columna) == (2,1,2) and objeto == 'cofre':
                if sinLlave:
                   print ( '¡No puedes abrir el cofre sin una llave!')
                else:
                    # El cofre se abre y el juego se ha ganado
                    print ( 'Abres el cofre, lentamente...')
                    time.sleep(1)
                    ganar()
                    juegoAcabado = True
            else:
               print ( 'No puedo hacer eso.')
            return
    # examinar objetos
    if verbo == 'examinar':
        if len(palabras) == 1:
            print ( 'Perdona... ¿examinar qué?')
            return
        else:
            objeto = palabras[1]
            # Comprobar que el objeto es correcto
            if objeto == 'mesa' and (piso,fila,columna) == (1,2,1):
                print ( 'La mesa parece sólida.')
                time.sleep(0.5)
                print ( 'Miras por debajo...')
                time.sleep(0.5)
                if sinLlave:
                   print ( '... y ves una llave!')
                else:
                   print ( 'No hay nada.')
            elif objeto == 'baúl' and (piso,fila,columna) == (1,1,3):
                if bAbierto:
                    print ( 'Miras dentro del baúl...')
                    time.sleep(0.5)
                    if tienecrucifijo:
                       print ( 'Está vacío.')
                    else:
                       print ( '¡Hay un crucifijo!')
                else:
                    print ( 'El baúl parece cerrado...')
                    time.sleep(0.5)
                    print ( '...pero no tiene cerradura.')
            elif objeto == 'cofre' and (piso,fila,columna) == (2,1,2):
                print ( 'Es un cofre de madera regia.')
                time.sleep(1)
                print ( 'Y con una cerradura muy resistente.')
            else:
               print ( 'Para lo que te va a servir...')
            return
    # Mostrar el inventario
    if verbo == 'inventario':
        # Verificar que llevas algo
        if inventario == []:
            print ( 'No llevas nada')
            return
        # Listar tus objetos
        print ( 'Llevas contigo ',)
        for i in inventario:
           print ( i)
        print ()
        return
    # Atacar al monje
    if verbo == 'atacar':
        # Asegurarse que se ataca al monje
        if len(palabras) == 1 or palabras[1] == 'monje':
            # El monje tiene que estar vivo para atacarle
            if not monjeVivo:
                print ( 'Pero... ¡si ya está muerto!')
                return
            if (piso,fila,columna) == (2,1,2):
                # Atacar al monje y ponerlo activo
                monjeActivo = True
                # Mirar si llevamos la crucifijo
                if tienecrucifijo:
                    print ( 'Alzas el crucifijo. El monje se te queda mirando')
                    time.sleep(1)
                    if haComido:
                        # Ejecutar al monje
                        print ( 'Y ves como se desmaya y desaparece delante de ti')
                        monjeVivo = False
                    else:
                        # Morir por no estar fuerte
                        print ( ' te falta fuerza para combatirlo...')
                        time.sleep(0.5)
                        print ( 'y te desplomas mientras el monje te lleva al agujero, donde una criatura te devora.')
                        juegoAcabado = True
                        monjeActivo = False
                else:
                   print ( 'Insensato... ¡Deberías haber huído mientras podías!')
            else:
               print ( 'Creo que no estás en el lugar correcto para hacer eso.')
        else:
           print ( 'Supongo que estás de broma, ¿no?')
        return
        
# Función que gestiona las felicitaciones al ganar el juego
def ganar():
   print ( 'Cojes el libro y ves que está escrito en otro iddioma y no entiendes nada, pero...')
   print ( 'lo levantas y puedes ver dentro del arario un cofre... ')
   time.sleep(1)
   print ()
   print ( '***************************************************************************')
   print ( ' ****************** ENHORABUENA, TE ACABAS DE HACER RICO ******************')
   print ( '***************************************************************************')

# Bucle general, necesario por si se quiere volver a jugar
while True:
    # Primero inicializamos las variables del juego
    
    # Posición
    piso = 1
    fila = 1
    columna = 2
    
    # Indicadores del estado del jugador
    bAbierto = False
    sinLlave = True
    tienecrucifijo = False
    haComido = False
    haBebido = False
    tienecrucifijo = False
    crucifijoEnMano = False
    agujeroAlSur = False
    inventario = []
    
    # Mapa de situación de diferentes objetos
    mapa ={}
    mapa[(1,1,1)] = []
    mapa[(1,1,2)] = []
    mapa[(1,1,3)] = []
    mapa[(1,2,1)] = ["pan"]
    mapa[(1,2,2)] = []
    mapa[(1,2,3)] = ["copa"]
    mapa[(2,1,1)] = ["vaso"]
    mapa[(2,1,2)] = []
    mapa[(2,1,3)] = []
    mapa[(2,2,1)] = []
    mapa[(2,2,2)] = []
    mapa[(2,2,3)] = ["hostia"]
    
    # Indicador de partida terminada
    juegoAcabado = False
    
    # Indicador para no repetir varias veces la descripción
    yaDescrito = False
    
    # Contador del tiempo que pasa
    tiempo = 0
    
    # Tiempo de espera del monje
    monjeVivo = True
    esperamonje = 0
    
    # Indicador de que el monje te ataca
    monjeActivo = False
    
    # Mostrar la introducción
    intro()
    
    # Bucle de juego. Se repite una y otra vez mientras dura el juego
    while True:
        if not yaDescrito:
            describir(piso, fila, columna)
            yaDescrito = True
        # Pedir al jugador que realice una acción
        orden = input('¿Qué quieres hacer? ').lower()
        # Aumentar el tiempo
        tiempo = tiempo + 1
        # Si estás con el monje, aumentar el tiempo de espera
        if (piso,fila,columna) == (2,1,2):
            esperamonje = esperamonje + 1
        # Procesar la acción y ejecutarla
        procesar(orden)
        # Si no se ha bebido pasado un tiempo, se pierde si ya no se ha hecho
        if tiempo>25 and not haBebido and not juegoAcabado:
            print ( 'Estás sediento, no puedes más, deberías haber bebido...')
            time.sleep(1)
            print ( 'Te desmayas...')
            time.sleep(1)
            if monjeVivo:
               print ( '... Y el monje lo aprovecha para arrogarte a un agujero.')
               print ( 'El juego ha acabado.')
            else:
               print ( '... Y te consumes poco a poco en el suelo, deshidratado.')
            juegoAcabado = True
        # Si has pasado demasiado tiempo en presencia del monje
        # o si está activo, te ataca.
        # Pero siempre que no lo haya hecho ya y estés muerto
        if (esperamonje > 2  or monjeActivo) and monjeVivo:
            print ( 'El monje te ataca...')
            time.sleep(1)
            # Si el jugador está armado, dar una oportunidad
            if tienecrucifijo:
                monjeActivo = True
                if not crucifijoEnMano:
                    print ( '... y sacas el crucifijo y ¡intentas auyentarlo!')
                    crucifijoEnMano = True
            else:
                print ( 'Desarmado, no tienes ninguna oportunidad.')
                time.sleep(0.5)
                print ( 'Te despedaza y te lanza al agujero.')
                juegoAcabado = True
        # Si el monje ha atacado varias veces y no has comido, mueres
        if esperamonje > 3 and monjeVivo:
            if not haComido:
                print ( 'Débil por falta de comida, no ofreces resistencia al monje.')
                print ( '¡La comida eres tú!')
                juegoAcabado = True
        # Y si ha pasado demasiado tiempo, también pierdes
        if esperamonje > 5 and monjeVivo:
            print ( 'Finalmente el monje te hunde el pecho y mueres brutalmente...')
            juegoAcabado = True
        # Si el juego ha terminado, salir del bucle
        if juegoAcabado:
            break
    print ()
    print ( '---------------------------------------------------')
    continuar = input('¿Quieres jugar otra vez? ').lower().startswith('s')
    if not continuar:
        break
    print ( '---------------------------------------------------')
    print ()
