# Base de datos de usuarios como lista
usuarios = []

# Mensaje de bienvenida y registro de usuario
print("===================================================")
print("         BIENVENIDO A MENSAJERÍA FIDÉLITAS         ")
print("===================================================\n")

while True:
    print("\n================= Menú Principal =================\n")
    print("1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Salir")
    opcion_principal = input("\nSeleccione una opción (1/2/3): ")

    if opcion_principal == '1':
        # Iniciar sesión
        correo_usuario = input("Ingrese su correo electrónico: ")
        
        usuario_encontrado = ''
        for usuario in usuarios:
            if usuario['correo_usuario'] == correo_usuario:
                usuario_encontrado = usuario
                break
        
        if usuario_encontrado != '':
            print("\n===================================================")
            print("                   ESTAS DENTRO                    ")
            print("===================================================")
            
            usuario_actual = usuario_encontrado

            # Submenú de Usuario
            while True:
                print("\n================= Submenú Usuario =================\n")
                print("1. Registrar factura electrónica")
                print("2. Crear paquete")
                print("3. Volver al menú principal")
                opcion_submenu = input("Seleccione una opción (1/2/3): ")

                if opcion_submenu == '1':
                    # Registrar factura electrónica
                    numero_cedula_factura = input("Número de cédula: ")
                    nombre_registrado = input("Nombre registrado: ")
                    numero_telefono_factura = input("Número de Teléfono: ")
                    correo_factura = input("Correo Electrónico: ")
                    provincia_factura = input("Provincia: ")
                    canton_factura = input("Cantón: ")
                    distrito_factura = input("Distrito: ")
                    factura = {
                        'numero_cedula_factura': numero_cedula_factura,
                        'nombre_registrado': nombre_registrado,
                        'numero_telefono_factura': numero_telefono_factura,
                        'correo_usuario': correo_factura,
                        'provincia_factura': provincia_factura,
                        'canton_factura': canton_factura,
                        'distrito_factura': distrito_factura
                    }
                    usuario_actual['facturas'] = usuario_actual['facturas'] + [factura]  # Agregar factura a la lista
                    print("Factura registrada con éxito.")
                    
                #falta el crear paquetes
                 
                elif opcion_submenu == '3':
                    # Salir del submenú de usuario y volver al menú principal
                    break
                
                else:
                    print("Opción no válida. Inténtelo de nuevo.")
        else:
            print("\nEl usuario con correo electrónico "+ correo_usuario + " no está registrado.")

    elif opcion_principal == '2':
        # Registrar usuario
        correo_usuario = input("Correo Electrónico: ")
        nombre_comercio_usuario = input("Nombre del comercio: ")
        locacion_usuario = input("Ubicación del local: ")
        nuevo_usuario = {
            'correo_usuario': correo_usuario,
            'nombre_comercio_usuario': nombre_comercio_usuario,
            'locacion_usuario': locacion_usuario,
            'facturas': [],
            'paquetes': []
        }
        usuarios = usuarios + [nuevo_usuario]  # Agregar nuevo usuario a la lista
        print("Usuario registrado con éxito.")

    elif opcion_principal == '3':
       # Mensaje de despedida al salir del programa
        print('Saliendo de la aplicación...')
        print("\n===================================================")
        print("         Gracias por usar Fidélitas. ¡Hasta pronto!      ")
        print("===================================================\n")
        break


