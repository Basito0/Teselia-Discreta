def DefinirRuta(vec, ar, rec):
    vecActual = "A2"
    recorridas = []
    peleas = 0

    #PRIMERA BUSQUEDA
    vecObj = "G"
    vecPos = "G"
    while vecPos != vecActual:
        

def sort(ar):
    #PARA ORDENAR DE MENOR A MAYOR SEGÚN NÚMERO DE ENTRENADORES
    n = len(ar)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (ar[j][2]) > (ar[j + 1][2]):
                ar[j][2], ar[j + 1][2] = ar[j + 1][2], ar[j][2]
    for x in range(len(ar)):
        print(ar[x])


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

sort(rutas)
DefinirRuta(ciudades, rutas, aRecorrer)