from registro import *
from funciones import *

def main():
    opcion = -1
    proyectos_cargados = False
    matriz_creada = False
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            proyectos, lenguajes = cargar_proyectos()
            proyectos.pop(0)
            ordenar_asc_repo(proyectos)
            print("Proyectos Cargados con Exito!")
            proyectos_cargados = True
            
        elif proyectos_cargados:    
            if opcion == 2:
                filtro = validar_cadena_vacia()
                encontrados = buscar_por_tag(proyectos, filtro)
                mostrar_tag_encontrados(encontrados, filtro)
                guardar_datos(encontrados)

            elif opcion == 3:
                lenguajes = limpiar_lista(lenguajes)
                lenguajes.remove("lenguaje"); lenguajes.remove("")
                
                ordenar_asc(lenguajes)
                contador = contar_proy_por_lenguaje(proyectos, lenguajes)
                mostrar_conteo_lenguajes(contador, lenguajes)

            elif opcion == 4:
                matriz_creada = True
                matriz = matriz_xmes()
                matriz = definir_tabla(proyectos, matriz)
                
                mostrar_matriz_meses(matriz)

                filtro = validar_rango(1, 12, mensaje="Ingrese el mes a buscar: ")
                meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
                resultado = sumar_actualizaciones(matriz, filtro)
                print(f"En el mes {meses[filtro-1]} se encontraron: {resultado} estrellas.\n")
            
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
                    
                    pass


                else:
                    print("¡Error! Debe de procesar la informacion de la opcion 4.")
        else:
            print("¡Error! Debe de cargar los proyectos en la opcion 1")
            
            
if __name__ == "__main__":
    main()