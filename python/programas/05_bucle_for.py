texto = input("introduzca un texto, por favor")
def contador_vocales(texto):
    x = texto.lower()  # Convertir el texto a minúsculas para simplificar el conteo
    contador_vocales = 0 # Definir un contador para las vocales
    # Lista de vocales en español
    vocales = ['a', 'e', 'i', 'o', 'u', 'á', 'é','í', 'ó', 'ú','ü'] # Lista de vocales en español
    
    for caracter in x :  # Iterar sobre cada carácter en el texto
        if caracter in vocales:   # Si el carácter es una vocal, incrementar el contador
            contador_vocales = contador_vocales + 1
    
    return contador_vocales   # Devolver el resultado
    
print("El número de vocales en este texto es ",contador_vocales(texto)) # Imprir el contador de las vocales