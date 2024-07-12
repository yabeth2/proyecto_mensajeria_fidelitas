# Base de datos de usuarios como lista
usuarios = []
paquetes= []
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
                    print("\n================= Seleccione el tipo de cédula =================\n")
                    print("1. Nacional")
                    print("2. Extrajera")
                    print("3. Jurídica")
                    tipo_cedula = input("Ingrese el número de cédula")
                    if tipo_cedula == '1':
                        tipo_cedula_esc = "Nacional"
                    elif tipo_cedula == '2':
                        tipo_cedula_esc = "Extranjera"
                    elif tipo_cedula == '3':
                        tipo_cedula_esc = "Jurídica"
                    else:
                        print("Opcion no válida, se procede a solicitar una cédula nacional")
                        tipo_cedula_esc = "Nacional"
                    numero_cedula_factura = input("Número de cédula: ")
                    nombre_registrado = input("Nombre registrado: ")
                    numero_telefono_factura = input("Número de Teléfono: ")
                    correo_factura = input("Correo Electrónico: ")
                    provincia_factura = input("Provincia: ")
                    canton_factura = input("Cantón: ")
                    distrito_factura = input("Distrito: ")
                    factura = {
                        'tipo_cedula': tipo_cedula_esc,
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
                    
                #Crear paquetes
                elif opcion_submenu == '2':
                    nombre_destinatario = input("Ingrese nombre del destinatario: ")
                    telefono_destinatario = input("Ingrese teléfono del destinatario: ")
                    numeroCedula_destinatario = input("Ingrese el número de cédula del destinatario: ")
                    peso_paquete = input("Ingrese el peso del paquete en kilogramos: ")
                    cobro_contra_entrega = input("Ingrese el monto a contra entrega en colones: ")
                
                    paquetes = {
                        'nombre_destinatario': nombre_destinatario,
                        'telefono_destinatario': telefono_destinatario,
                        'numeroCedula_destinatario': numeroCedula_destinatario,
                        'peso_paquete': peso_paquete,
                        'cobro_contra_entrega': cobro_contra_entrega
                   }
                if 'paquetes' not in usuario_actual: 
                    usuario_actual['paquetes'] = []

                usuario_actual['paquetes'] = usuario_actual['paquetes'] + [paquetes]
                        
                print("El paquete fue registrado con exito")
                

                    
                 
                if opcion_submenu == '3':
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
        numero_tel_comercio = input ("Número telefónico del comercio: ")
        nombre_propietario = input("Nombre del propietario del local: ")
        locacion_usuario = input("Ubicación del local: ")
        nuevo_usuario = {
            'correo_usuario': correo_usuario,
            'nombre_comercio_usuario': nombre_comercio_usuario,
            'numero_tel_comercio' : numero_tel_comercio,
            'nombre_propietario': nombre_propietario,
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
    else:
        print("\nOpción no válida, por favor ingrese una ópcion disponible")


