def posiciones(lista):
    suma=funcion_suma(lista[2],lista[0]+lista[1],0,[],
                      len(lista[0]+lista[1]))
    return suma

def funcion_suma(lista_2,lista,cont,resultado,largo_lista):
    if lista_2==[]:
        return resultado
    if cont==largo_lista:
        funcion_suma(lista_2[1:],lista,cont,resultado,largo_lista)
    if lista_2[0][0] in lista[0][0]:
        resultado+=[lista_2[0][0],lista_2[cont][1]]
    funcion_suma(lista_2,lista,cont+1,resultado,largo_lista)
"""
def ordenar(lista_2,lista_1,lista_0,resultado):
    try:
        if lista_2[0][0] in lista_1[0]:
            if lista_2[0][0] in lista_0[0]:
                resultado+=[lista_2[0][0],lista_2[0][1]+lista_1[1]+lista_0[1]]
            print
        return ordenar(lista_2[1:],lista_1,lista,resultado)
    except:
        return resultado
"""
##ejercicio 12
def es_fibonacci(num):
    """verifica si el numero ya es parte del fibonacci"""
    return es_fibonacci_aux(num,0,1)

def es_fibonacci_aux(num,valor_anterior,valor):
    print(valor)
    """crea la sucecion de fibonacci"""
    if valor>num:
        return False
    if valor==num:
        return True
    return es_fibonacci_aux(num,valor,valor+valor_anterior)
