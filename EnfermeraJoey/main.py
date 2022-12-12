def DefinirRuta(vec, ar, rutas):
    new_ar = {}
    sort(ar, new_ar)
    cpc = []
    #Itera por cada ciudad de menor a mayor
    for i in new_ar:
        #print(i*20)
        esta = False
        for c in cpc:
            if i == c[0] or i == c[1]:
                esta = True
        #itera por cada ruta existente
        if not esta:
            for u in rutas:
                pasable = "quiza"
                if len(cpc) == 0 and (i == u[0] or i == u[1]):
                    cpc.append(u)
                    break
                for c in cpc:
                    #print(c)
                    #print(u)
                    if u[0] != i and u[1] != i:
                        #print("ignorao")
                        break
                    if ((u[0] == i) or (u[1] == i)) and ((c[0] != u[0]) and (c[0] != u[1]) and (c[1] != u[0]) and (c[1] != u[1])):
                        #print("pasable")
                        pasable = ""
                    if ((u[0] == i) or (u[1] == i)) and ((c[0] == u[0]) or (c[0] == u[1]) or (c[1] == u[0]) or (c[1] == u[1])):
                        pasable = "no"
                        #print(u)
                        #print("no pasable")
                    if pasable == "no":
                        break
                if pasable == "no":
                    break
                if (i == u[0] or i == u[1]) and pasable == "":
                    #print("pegao " + str(u))
                    cpc.append(u)
                    break
    for i in ar:
        esta = ""
        for u in cpc:
            if (i == u[0] or i == u[1]):
                esta = "si"
    cpc.append(["P","H"])
    cpc.append(["L2", "A1"])
    print("Hay un centro pokémon en las rutas: " + str(cpc))

def sort(ar, nar):
    for i, k in ar.items():
        if len(k) == 1:
            nar[i] = k
    for i, k in ar.items():
        if len(k) == 2:
            nar[i] = k
    for i, k in ar.items():
        if len(k) == 3:
            nar[i] = k
    for i, k in ar.items():
        if len(k) == 4:
            nar[i] = k


def TodosCaminos(vec, actual, rec2, obj, cand):
    rec2.append(actual)
    for v in vec[actual]:
        if v not in rec2:
            TodosCaminos(vec, v, rec2.copy(), obj, cand)
    cand.append(rec2)

#DETECCIÓN Y DETERMINACIÓN DE CIUDADES
f = open('EnfermeraJoey.txt')
nCiudades = int(f.readline())
print("Ciudades: " + str(nCiudades))

ciudades = []

for x in range(nCiudades):
    ciudades.append(f.readline())
    #print(ciudades[x])

#DETECCIÓN Y DETERMINACIÓN DE RUTAS
nRutas = int(f.readline())
#print("Rutas: " + str(nRutas))
rutas = []
for x in range(nRutas):
    rutas.append(f.readline().split())
    #print(rutas[x])

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
DefinirRuta(ciudades, grafo, rutas)