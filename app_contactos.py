import argparse 
import sys
from contactos.gestor_contactos import Gestor_contactos as gc
from contactos.validaciones import Validar as val


def main(create, show, search, delete):
    
    if create:
        print("CREAR NUEVO CONTACTO:")
        def create():
            nombre = input("Introduzca su nombre: ")
            telefono = input("Introduzca su teléfono: ")
            email = input("Introduzca su email: ")
                
            nombre = val.validar_nombre(nombre)
            telefono = val.validar_telefono(telefono)    
            email = val.validar_email(email)
            
            if nombre and telefono and email:
                gc.crear_contacto(nombre, telefono, email)
        create()

    if show:
        print("LISTA DE CONTACTOS:")
        def mostrar():
            gc.mostrar_contactos()
        mostrar()
        
    if search:       
        print("BUSCAR CONTACTO:")
        def buscar():
            nombre = input("Introduzca el nombre del contacto a buscar: ")
            nombre = val.validar_nombre(nombre)
            if nombre:
                gc.buscar_contacto(nombre)              
        buscar()

    if delete:
        print("ELIMINAR CONTACTO:")
        def eliminar():
            nombre = input("Introduzca el nombre del contacto a eliminar: ")
            nombre = val.validar_nombre(nombre)
            if nombre:
                gc.eliminar_contacto(nombre)
        eliminar()



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="APP Contactos. Guarda y gestiona tus contactos.")
    
    parser.add_argument("-c","--create", action="store_true", help="Crear un nuevo contacto")
    parser.add_argument("-sh","--show", action="store_true", help="Muestra lista de contactos creados.")
    parser.add_argument("-s","--search", action="store_true", help="Busca contacto resgistrado por el nombre.")
    parser.add_argument("-d","--delete", action="store_true", help="Borra contactos registrados por el nombre")
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    
    args = parser.parse_args()
    
    main(create=args.create, show=args.show, search=args.search, delete=args.delete)
    
    
    # INTERFAZ ALTERNATIVA
    # while True:
    #     print("\nMenú de gestión de contactos")
    #     print("1. Crear contacto")
    #     print("2. Mostrar contactos")
    #     print("3. Buscar contacto")
    #     print("4. Eliminar contacto")
    #     print("5. Salir")
    #     opcion = input("Introduzca su opción: ")
    #     if opcion == "1":
    #         create()
    #         continue
    #     elif opcion == "2":
    #         mostrar()
    #         continue
    #     elif opcion == "3":
    #         buscar()
    #         continue
    #     elif opcion == "4":
    #         eliminar()
    #         continue
    #     elif opcion == "5":
    #         print("Saliendo de la aplicación...")
    #         print("Hasta la próxima!!")
    #         break