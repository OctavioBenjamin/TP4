
from registro import *
from datetime import datetime
import os
import os.path
import pickle

def menu():
    print("""
╔════════════════════════════════════════╗
║        TP4-G206 SOFTWARE COMPANY       ║
╠════════════════════════════════════════╣
║1- Cargar Proyectos                     ║
║2- Filtrar por tag                      ║
║3- Proyectos por lenguajes              ║
║4- Popularidad                          ║
║5- Buscar proyecto a actualizar         ║
║6- Guardar Populares                    ║
║7- Reconstruir Matriz                   ║
║0- Salir                                ║
╚════════════════════════════════════════╝""")
    op = validar_rango(0, 7, mensaje="Ingrese la opcion que desee: ")
    print(" ")
    return op

def add_in_order(vec, elemento):
    izq, der = 0, len(vec)-1
    pos = der+1
    while izq <= der:
        i = (izq + der)//2
        if elemento.repo == vec[i].repo:
            pos = i
            break
        elif elemento.repo < vec[i].repo:
            der = i-1
        else:
            izq = i + 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [elemento]


def cargar_proyectos():
    repositorios = list()
    proyectos = list()
    lenguajes = list()
    contador = [0]*2 #0: Cargados 1:Omitidos
    tamaño = os.path.getsize("files/proyectos.csv")
    if os.path.exists("files/proyectos.csv"):
        archivo = open("files/proyectos.csv", "rt", encoding="utf8")
        linea = archivo.readline()
        while archivo.tell() < tamaño:
            linea = archivo.readline()
            linea = linea[:-1]
            proyecto, lenguajes_array= to_proyecto(linea, lenguajes)

            # Omitir proyectos mientras se cargan
            # Contador -> 0: Cargados    1:Omitidos
            if proyecto.repo not in repositorios and len(proyecto.leng) != 0:
                if proyecto.repo != "repositorio":
                    add_in_order(proyectos, proyecto)
                    repositorios.append(proyecto.repo)
                    contador[0]+=1
            else:
                contador[1]+=1

        archivo.close()
    else:
        print("No existe el archivo\n")
    
    return proyectos, lenguajes_array, contador



def busqueda_binaria(vec, val, inicio, final):
    if inicio == final:
        if vec[inicio] > val:
            return inicio
        else:
            return inicio+1
    if inicio > final:
        return inicio
  
    mid = (inicio+final)//2
    if vec[mid] < val:
        return busqueda_binaria(vec, val, mid+1, final)
    elif vec[mid] > val:
        return busqueda_binaria(vec, val, inicio, mid-1)
    else:
        return mid


def ignorar_proyectos(proyectos):
    repositorios = list()
    lista_proyecto_limpia = list()
    for proyecto in proyectos:

        if len(proyecto.leng) == 0:
            if proyecto.repo not in repositorios:
                repositorios.append(proyecto.repo)
                lista_proyecto_limpia.append(proyecto)

    return lista_proyecto_limpia
def ordenar_asc(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]

def limpiar_lista(lista):
    nueva_lista = list()
    for i in range(len(lista)):
        if lista[i] not in nueva_lista:
            nueva_lista.append(lista[i])
    nueva_lista.remove('')
    return nueva_lista

def validar_opcion(valor=0, mensaje="Ingrese un valor:"):
    num = int(input(mensaje))
    while num <= valor:
        print('Error, debe ingresar un valor mayor que', valor)
        num = int(input(mensaje))
    return num

def validar_cadena_vacia(mensaje="Ingrese el filtro a buscar: "):
    palabra = str(input(mensaje))
    while len(palabra) <= 0:
        print("Error! Ingrese un valor valido")
        palabra = str(input(mensaje))
    return palabra

def validar_rango(desde, hasta, mensaje="Ingrese un valor: "):
    val = int(input(mensaje))
    while val < desde or val > hasta:
        print("Error, el valor debe estar entre", desde, "y", hasta, "!")
        val = int(input(mensaje))
    return val

def buscar_por_tag(proyectos, filtro):
    proyectos_filtrados = list()
    for proyecto in proyectos:
        tags = list()
        tags.extend(proyecto.tags.split(","))
        for tag in tags:
            if tag == filtro:
                proyectos_filtrados.append(proyecto)
    return proyectos_filtrados

"""
    1: de 0 a 10 k
    2: de 10.1 a 20 k
    3: de 20.1 a 30 k
    4: de 30.1 a 40 k
    5: mayor a 40 k

"""
def definir_estrellas(proyecto):
    estrella = 0
    if float(proyecto.likes) <= 10:
        estrella =  1
    elif 20 >= float(proyecto.likes) >= 10.1:
        estrella = 2
    elif 30 >= float(proyecto.likes) >= 20.1:
        estrella = 3
    elif 40 >= float(proyecto.likes) >= 30.1:
        estrella = 4
    elif float(proyecto.likes) > 40:
        estrella = 5
    return estrella

def mostrar_tag_encontrados(proyectos, tag):
    print(f"\n Proyectos encontrados con el Tag {tag}")
    for proyecto in proyectos:
        estrella = definir_estrellas(proyecto)
        print(f"{proyecto.repo} | {proyecto.fecha} | {estrella} Estrella")

def guardar_datos(encontrados):
    print("")
    print("¿Desea guardar los registros encontrados?")
    # op = int(input("1. Guardar\n2. No Guardar\n"))
    op = validar_rango(1, 2, mensaje="Ingrese la opcion que desea:\n1. Guardar\n2. No Guardar\n")
    if op == 1:
        m = open("files/filtros_encontrados.txt", mode="w", encoding="utf8")
        m.write("USUARIO | REPOSITORIO | DESCRIPCION | FECHA DE ACTUALIZACION | LENGUAJE | LIKES | TAGS | URL\n")
        for encontrado in encontrados:
            m.write(f"{to_string(encontrado)}")
        m.close()
    elif op == 2:
        print("Se decidio no guardar los datos... \n")


def busqueda_binaria_asc(v, x):
    izq = 0
    der = len(v) - 1
    c = (izq + der) // 2
    while izq <= der and x != v[c]:
        if x > v[c]:
            izq = c + 1
        else:
            der = c - 1
        c = (izq + der) // 2
    if izq > der:
        res = -1
    else:
        res = c
    return res

def busqueda_binaria_asc_repo(proyectos, x):
    izq = 0
    der = len(proyectos) - 1
    c = (izq + der) // 2
    while izq <= der and x != proyectos[c].repo:
        if x > proyectos[c].repo:
            izq = c + 1
        else:
            der = c - 1
        c = (izq + der) // 2
    if izq > der:
        res = -1
    else:
        res = c
    return res

def contar_proy_por_lenguaje(proyectos, lenguajes):
    
    contador = [0]*len(lenguajes)
    for i in range(len(proyectos)):
        lenguajes_usados = proyectos[i].leng.split(",")
        for lenguaje in lenguajes_usados:
            j = busqueda_binaria_asc(lenguajes, lenguaje)
            contador[j] += 1
    return contador

def ordenar_mayor_menor_dos_vectores(v1, v2):
    n = len(v1)
    for i in range(n-1):
        for j in range(i+1, n):
            if v1[i] < v1[j]:
                v1[i], v1[j] = v1[j], v1[i]
                v2[i], v2[j] = v2[j], v2[i]

def mostrar_conteo_lenguajes(contador, lenguajes):
    ordenar_mayor_menor_dos_vectores(contador, lenguajes)
    print("")
    for i in range(len(lenguajes)):
        print(f"{lenguajes[i]} tiene: {contador[i]} proyectos.")

def matriz_xmes():
    matriz = list()
    for i in range(12):
        matriz.append([0]*5)
    return matriz

def mostrar_matriz(matriz):
    for i in matriz:
        print(i)

def definir_mes(proyecto):
    fecha = proyecto.fecha
    # yyyy-mm-dd
    mes = str(fecha[5]+fecha[6])
    #print(mes)
    if mes[0] == "0":
        return int(fecha[6])
    else:
        return int(mes)



def definir_tabla(proyectos, matriz):
    for i in range(len(proyectos)):
        mes = definir_mes(proyectos[i])
        estrella = definir_estrellas(proyectos[i])
        #print(proyectos[i].repo, type(mes), mes, proyectos[i].likes, type(estrella), estrella)
        #matriz[estrella-1][mes-1] += 1
        matriz[mes-1][estrella-1] += 1
    return matriz

def sumar_actualizaciones(matriz, filtro):
    filtro -= 1
    suma = 0
    
    for i in range(5):
        suma += matriz[filtro][i]

    return suma

def fecha_actual():
    return datetime.today().strftime('%Y-%m-%d')

def actualizar_url(proyecto):
    nuevo_url = validar_cadena_vacia(mensaje='Ingrese nuevo url para actualizar: ')
    proyecto.url = nuevo_url
    proyecto.fecha = fecha_actual()
    return proyecto


def definir_registros_de_matriz(matriz):
    proyectos_por_mes = list()
    for i in range(12):
        for j in range(5):
            if matriz[i][j] != 0:
                mes = i+1
                tipo = j+1 #Tipo de estrellas (de 1 a 5 estrellas)
                proyectos = matriz[i][j]
                elemento = ElementoDeMatriz(mes, tipo, proyectos)
                proyectos_por_mes.append(elemento)
    return proyectos_por_mes
            
def guardar_registros_en_archivo_dat(registro, archivo):
    archivo_dat = open(archivo, "ab")
    for elemento in registro:
        pickle.dump(elemento, archivo_dat)
    archivo_dat.close()

def leer_archivo_binario(archivo): 
    m = open(archivo, "rb")
    t = os.path.getsize(archivo)
    print('Informacion recuperada desde el archivo', archivo, ':')
    matriz = matriz_xmes()
    while m.tell() < t:
        elemento = pickle.load(m)
        reconstruir_matriz(elemento, matriz)
    m.close()

def reconstruir_matriz(elemento, matriz):
    for i in range(12):
        for j in range(5):
            matriz[elemento.mes - 1][elemento.tipo - 1] = elemento.proyectos

