from registro import *
from funciones import *

def main():
    opcion = -1
    proyectos_cargados = False
    matriz_creada = False
    elementos_guardados = False
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            proyectos, lenguajes, total_cargado = cargar_proyectos()
            proyectos.pop(0)
            #ordenar_asc_repo(proyectos) # generar funcion add_in_order
            print("Proyectos Cargados con Exito!")
            print(f"Se han cargado: {len(proyectos)}")
            print(f"Se han omitido: {total_cargado - len(proyectos)}")
            proyectos_cargados = True
            
        elif proyectos_cargados:    
            if opcion == 2:
                filtro = validar_cadena_vacia()
                encontrados = buscar_por_tag(proyectos, filtro)
                
                if encontrados:
                    mostrar_tag_encontrados(encontrados, filtro)
                    guardar_datos(encontrados)
                else:
                    print(f"No se han encontrado proyectos con el tag: {filtro}")

            elif opcion == 3:
                lenguajes = limpiar_lista(lenguajes)
                
                ordenar_asc(lenguajes)
                contador = contar_proy_por_lenguaje(proyectos, lenguajes)
                mostrar_conteo_lenguajes(contador, lenguajes)

            elif opcion == 4:
                matriz_creada = True
                matriz = matriz_xmes()
                matriz = definir_tabla(proyectos, matriz)
                
                mostrar_matriz(matriz)
                print("""\n1-Enero 2-Febrero 3-Marzo 4-Abril\n5-Mayo 6-Junio 7-Julio 8-Agosto\n9-Septiembre 10-Octubre 11-Noviembre 12-Diciembre\n""")
                filtro = validar_rango(1, 12, mensaje="Ingrese el mes a buscar: ")
                meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
                resultado = sumar_actualizaciones(matriz, filtro)
                print(f"En el mes {meses[filtro-1]} se encontraron: {resultado} proyectos actualizados.\n")
            
            elif opcion == 5:
                repo_filtro = validar_cadena_vacia(mensaje='Ingrese el repositorio a buscar: ')

                encontrado = busqueda_binaria_asc_repo(proyectos, repo_filtro)

                if encontrado > -1:
                    print(f"Se ha encontrado con el exito el repositorio {repo_filtro}")
                    proyectos[encontrado].url = actualizar_url(proyectos[encontrado])
                    print(f"Se ha actualizado el url del repositorio {repo_filtro} el dia {proyectos[encontrado].fecha}")
                else:
                    print("No se ha encontrado ningun repositorio.")

            elif opcion == 6:
                if matriz_creada:
                    
                    elementos_de_matriz = definir_registros_de_matriz(matriz)
                    archivo = "registros_proyectos_clasificados.dat"
                    guardar_registros_en_archivo_dat(elementos_de_matriz, archivo)
                    print("¡Se Han guardado los elementos de la matriz con exito!")
                    elementos_guardados = True
                else:
                    print("¡Error! no se ha generado la matriz para guardar los datos necesarios.")

            elif opcion == 7:
                if elementos_guardados:
                
                    leer_archivo_binario(archivo)
                    mostrar_matriz(matriz)
                else:
                    print("¡Error! No se han guardado los datos en el archivo binario")
            
        else:
            print("¡Error! Debe de cargar los proyectos en la opcion 1")
            
            
if __name__ == "__main__":
    main()