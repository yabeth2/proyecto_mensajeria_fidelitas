# Inicialización para almacenar datos 
usuarios = []
paquetes = []
facturas = []

# Mensaje de bienvenida y registro de usuario
print("===================================================")
print("         BIENVENIDO A MENSAJERÍA FIDÉLITAS       ")
print("===================================================\n")

print("Por favor regístrese en la aplicación:\n")
correo_comercio = input("Correo Electrónico: ")
nombre_comercio = input("Nombre del Comercio: ")
telefono_comercio = input("Teléfono del Comercio: ")
nombre_dueno = input("Nombre del Dueño: ")
ubicacion_comercio = input("Ubicación del Local: ")

# Mostrar pantalla de opciones
while True:
    print("\n================= Menú Principal =================\n")
    print("1. Registrar Factura Electrónica")
    print("2. Crear Paquete")
    print("3. Salir")
    opcion = input("\nSeleccione una opción (1/2/3): ")

    if opcion == "1":
        # Registro de la factura electrónica
        print("\n--------------- Registro de Factura ---------------\n")
        tipo_cedula = input("Tipo de Cédula: ")
        numero_cedula = input("Número de Cédula: ")
        nombre_registrado = input("Nombre Registrado: ")
        telefono = input("Teléfono: ")
        correo_factura = input("Correo Electrónico: ")
        provincia = input("Provincia: ")
        canton = input("Cantón: ")
        distrito = input("Distrito: ")
        
        print("\n¡Factura registrada exitosamente!")

    elif opcion == "2":
        # Creación del paquete
        print("\n----------------- Crear Paquete ------------------\n")
        nombre_destinatario = input("Nombre Destinatario: ")
        telefono_destinatario = input("Teléfono Destinatario: ")
        peso_paquete = float(input("Peso del Paquete (Kilogramos): "))
        cobro_contra_entrega = input("Monto contra Entrega (colones, opcional): ")
        cobro_contra_entrega = cobro_contra_entrega if cobro_contra_entrega else None  # Asigna None si no se ingresó ningún valor
       
        print("\n¡Paquete Creado Exitosamente!")

    elif opcion == "3":
        print("\nSaliendo de la aplicación...")
        break #termina todo

    else:
        print("\nOpción no válida, por favor seleccione 1, 2 o 3.")

# Mensaje de despedida al salir del programa
print("\n===================================================")
print("         Gracias por usar Fidelitas. ¡Hasta pronto!      ")
print("===================================================\n")
