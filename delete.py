
# Base de datos de usuarios como lista
usuarios = []

salto_linea = "\n"
borde_superior = "=" * 51
borde_inferior = "=" * 51

def mensaje_bienvenida():
    print(borde_superior)
    print(" " * 10 + "BIENVENIDO A MENSAJERÍA FIDÉLITAS")
    print(borde_inferior)

def menu_principal():
    print("\n================= Menú Principal ==================\n")
    print("1. Iniciar sesión")
    print("2. Registrar usuario") 
    print("3. Salir")

def iniciar_sesion():
    print(salto_linea)
    correo_usuario = input("Ingrese su correo electrónico: ")
    
    usuario_encontrado = ''
    for usuario in usuarios:
        if usuario['correo_usuario'] == correo_usuario:
            usuario_encontrado = usuario
            break
    
    if usuario_encontrado != '':
        print(salto_linea)
        print(borde_superior)
        print(" " * 17 + "SESIÓN INICIADA")
        print(borde_inferior)
        
        usuario_actual = usuario_encontrado
        submenu_usuario(usuario_actual)
    else:
        print("\nEl usuario con correo electrónico " + '"' + correo_usuario + '"' + " no está registrado.")

def submenu_usuario(usuario_actual):
    while True:
        print("\n================= Menú de Usuario =================\n")
        print("1. Registrar factura electrónica")
        print("2. Crear paquete")
        print("3. Rastreo de paquetes")
        print("4. Volver al menú principal")
        opcion_submenu = input("\nSeleccione una opción (1/2/3/4): ")
        
        if opcion_submenu == '1':
            registrar_factura(usuario_actual)
        elif opcion_submenu == '2':
            crear_paquete(usuario_actual)
        elif opcion_submenu == '3':
            rastrear_paquete(usuario_actual)
        elif opcion_submenu == '4':
            break
        else:
            print("\nOpción no válida ❌. Inténtelo de nuevo.")

def registrar_factura(usuario_actual):
    print("\n============ Seleccione tipo de cédula ============\n")
    print("1. Nacional")
    print("2. Extrajera")
    print("3. Jurídica")
    tipo_cedula = input("Ingrese el tipo de cédula (1/2/3): ")
    if tipo_cedula == '1':
        tipo_cedula_esc = "Nacional"
    elif tipo_cedula == '2':
        tipo_cedula_esc = "Extranjera"
    elif tipo_cedula == '3':
        tipo_cedula_esc = "Jurídica"
    else:
        print("\nOpción no válida ❌, se procede a asignar la cédula nacional por defecto.\n")
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
    usuario_actual['facturas'] += [factura]
    
    print(salto_linea)
    print(borde_superior)
    print(" " * 11 + "Factura registrada con éxito.")
    print(borde_inferior)

def crear_paquete(usuario_actual):
    nombre_destinatario = input("Nombre del destinatario: ")
    telefono_destinatario = input("Teléfono del destinatario: ")
    numero_cedula_destinatario = input("Número de cédula del destinatario: ")
    peso_paquete = input("Peso del paquete (kg): ")
    cobro_contra_entrega = input("Monto a cobrar contra entrega (colones): ")
    numero_guia = telefono_destinatario + numero_cedula_destinatario

    paquete = {
        'nombre_destinatario': nombre_destinatario,
        'telefono_destinatario': telefono_destinatario,
        'numero_cedula_destinatario': numero_cedula_destinatario,
        'peso_paquete': peso_paquete,
        'cobro_contra_entrega': cobro_contra_entrega,
        'estado': 'creado',
        'numero_guia': numero_guia
    }
    usuario_actual['paquetes'] += [paquete]  # Agregar paquete a la lista
    
    print(borde_superior)                
    print(" " * 17 + "Paquete creado con éxito.")
    print(salto_linea)
    print("Número de guía: " + numero_guia)
    print("Información del Destinatario:")
    print("Nombre: " + nombre_destinatario)
    print("Número de teléfono: " + telefono_destinatario)
    if cobro_contra_entrega:
        print("Monto del Cobro: " + cobro_contra_entrega)
    else:
        print("Monto del Cobro: 0")
    print(borde_inferior)

def rastrear_paquete(usuario_actual):
    numero_guia_buscado = input("Ingrese el número de guía: ")
    paquete_encontrado = ''

    for paquete in usuario_actual['paquetes']:
        if paquete['numero_guia'] == numero_guia_buscado:
            paquete_encontrado = paquete
            break
    
def registrar_usuario():
    global usuarios
    correo_usuario = ''
    while correo_usuario == '':
        correo_usuario = input("Correo Electrónico: ")
        if correo_usuario == '':
            print("Correo electrónico inválido ❌. Inténtelo de nuevo.")
            print(salto_linea)
    
    nombre_comercio_usuario = input("Nombre del comercio: ")
    numero_tel_comercio = input("Número telefónico del comercio: ")
    nombre_propietario = input("Nombre del propietario del local: ")
    locacion_usuario = input("Ubicación del local: ")
    nuevo_usuario = {
        'correo_usuario': correo_usuario,
        'nombre_comercio_usuario': nombre_comercio_usuario,
        'numero_tel_comercio': numero_tel_comercio,
        'nombre_propietario': nombre_propietario,
        'locacion_usuario': locacion_usuario,
        'facturas': [],
        'paquetes': []
    }
    usuarios += [nuevo_usuario]  # Agregar nuevo usuario a la lista
    
    print(salto_linea)
    print(borde_superior)
    print(" " * 13 + "Usuario registrado con éxito.")
    print(borde_inferior)

def main():
    mensaje_bienvenida()

    while True:
        menu_principal()
        opcion_principal = input("\nSeleccione una opción (1/2/3): ")
        
        if opcion_principal == '1':
            iniciar_sesion()
        elif opcion_principal == '2':
            registrar_usuario()
        elif opcion_principal == '3':
            print('\nSaliendo de la aplicación...')
            print(borde_superior)
            print(" " * 5 + "Gracias por usar Fidélitas. ¡Hasta pronto!")
            print(borde_inferior)

            break
        else:
            print("\nError ❌: Por favor ingrese una opción disponible.")

main()
