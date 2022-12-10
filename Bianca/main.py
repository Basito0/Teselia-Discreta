import sys


def DefinirRuta(vec, ar, rec, rutas):
    vecActual = "A2"
    recorridas = []
    peleas = 0

    #ARCILLA-GRES
    print("Camino entre Arcilla y Gres")
    vecObj = "G"
    vecPos = "G"
    decision = []
    candidatos = []
    TodosCaminos(ar, vecActual, decision, vecObj, candidatos)
    #print(candidatos)
    peleas += ElMasBarato(candidatos, vecObj, rutas)

    #GRES-TEJA
    print("Camino mínimo entre Gres y Teja")
    vecObj = "T1"
    vecActual = "G"
    decision = []
    candidatos = []
    TodosCaminos(ar, vecActual, decision, vecObj, candidatos)
    peleas += ElMasBarato(candidatos, vecObj, rutas)

    # TEJA-HORMIGÓN
    print("Camino mínimo entre Teja y Hormigón")
    vecObj = "H"
    vecActual = "T1"
    decision = []
    candidatos = []
    TodosCaminos(ar, vecActual, decision, vecObj, candidatos)
    peleas += ElMasBarato(candidatos, vecObj, rutas)

    # HORMIGÓN-LOZA
    print("Camino mínimo entre Hormigón y Loza")
    vecObj = "L3"
    vecActual = "H"
    decision = []
    candidatos = []
    TodosCaminos(ar, vecActual, decision, vecObj, candidatos)
    peleas += ElMasBarato(candidatos, vecObj, rutas)

    # LOZA-PORCELANA
    print("Camino mínimo entre Loza y Porcelana")
    vecObj = "P"
    vecActual = "L3"
    decision = []
    candidatos = []
    TodosCaminos(ar, vecActual, decision, vecObj, candidatos)
    peleas += ElMasBarato(candidatos, vecObj, rutas)

    # PORCELANA-ENGOBE
    print("Camino mínimo entre Porcelana y Engobe")
    vecObj = "E2"
    vecActual = "P"
    decision = []
    candidatos = []
    TodosCaminos(ar, vecActual, decision, vecObj, candidatos)
    peleas += ElMasBarato(candidatos, vecObj, rutas)

    # ENGOBE-ESMALTE
    print("Camino mínimo entre Engobe y Esmalte")
    vecObj = "E1"
    vecActual = "E2"
    decision = []
    candidatos = []
    TodosCaminos(ar, vecActual, decision, vecObj, candidatos)
    peleas += ElMasBarato(candidatos, vecObj, rutas)

    # ESMALTE-CAOLÍN
    print("Camino mínimo entre Esmalte y Caolín")
    vecObj = "C1"
    vecActual = "E1"
    decision = []
    candidatos = []
    TodosCaminos(ar, vecActual, decision, vecObj, candidatos)
    peleas += ElMasBarato(candidatos, vecObj, rutas)

    # CAOLÍN-LIGA
    print("Camino mínimo entre Caolín y la Liga")
    vecObj = "L1"
    vecActual = "C1"
    decision = []
    candidatos = []
    TodosCaminos(ar, vecActual, decision, vecObj, candidatos)
    peleas += ElMasBarato(candidatos, vecObj, rutas)

    print("El número total de encuentros fue: " + str(peleas))

def TodosCaminos(vec, actual, rec2, obj, cand):
    rec2.append(actual)
    for v in vec[actual]:
        if v not in rec2:
            TodosCaminos(vec, v, rec2.copy(), obj, cand)
    cand.append(rec2)

def ElMasBarato(ar, obj, ls):
    precio_min_global = sys.maxsize
    candidato = []
    for c in ar:
        if c[len(c)-1] == obj:
            precio_min = 0
            for n in c:

                #ENCONTRAR EL PRECIO EN LS
                for d in ls:
                    #print(d)
                    if c.index(n)+1 != len(c):
                        if ((d[0] == n and d[1] == c[c.index(n)+1]) or (d[0] == c[c.index(n)+1] and d[1] == n)):
                            precio_min += d[2]
            if precio_min < precio_min_global:
                candidato = c
                precio_min_global = precio_min
    print("Ruta: ")
    print(candidato)
    print("Entrenadores encontrados: " + str(precio_min_global))
    return precio_min_global


def sort(ar):
    #PARA ORDENAR DE MENOR A MAYOR SEGÚN NÚMERO DE ENTRENADORES
    n = len(ar)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (ar[j][2]) > (ar[j + 1][2]):
                ar[j][2], ar[j + 1][2] = ar[j + 1][2], ar[j][2]



#DETECCIÓN Y DETERMINACIÓN DE CIUDADES
f = open('Bianca.txt')
nCiudades = int(f.readline())
print("Ciudades: " + str(nCiudades))

ciudades = []

for x in range(nCiudades):
    ciudades.append(f.readline())
    #print(ciudades[x])

#DETECCIÓN Y DETERMINACIÓN DE RUTAS
nRutas = int(f.readline())
print("Rutas: " + str(nRutas))
rutas = []
for x in range(nRutas):
    rutas.append(f.readline().split())
    #print(rutas[x])
for x in range(nRutas):
    rutas[x][2] = int(rutas[x][2])
    #print(rutas[x])

#DETECCIÓN Y DETERMINACIÓN DE CIUDADES A RECORRER
nRecorrer = int(f.readline())
print("A recorrer: " + str(nRecorrer))
aRecorrer = []
for x in range(nRecorrer):
    aRecorrer.append(f.readline())
    #print(aRecorrer[x])

grafo = { "A2" : ["T2"],
          "T2" : ["A2", "G"],
          "G" : ["T2", "E1"],
          "E1" : ["G", "P"],
          "P" : ["E1", "H", "M2"],
          "H" : ["P", "O"],
          "O" : ["H", "E2"],
          "E2" : ["O"],
          "M2" : ["P", "N", "F"],
          "F" : ["M2", "L3"],
          "L3" : ["F", "T1"],
          "T1" : ["L3", "C1"],
          "C1" : ["T1", "L2"],
          "L2" : ["C1", "A1"],
          "A1" : ["N", "M1", "C2", "L2"],
          "N" : ["A1", "M2"],
          "M1" : ["A1", "L1"],
          "L1" : ["M1"],
          "C2" : ["A1"]
        }

DefinirRuta(ciudades, grafo, aRecorrer, rutas)