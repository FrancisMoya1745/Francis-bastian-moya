import os
destinos_disponibles = ["Torres del Paine", "Carretera Austral", "Chiloé"]
# Lista para almacenar las reservas

reservas = []
def registrar_reserva():
    print("\n*** Registro de Reserva ***")
    nombre = input("Nombre del cliente: ")
    apellido = input("apellido del cliente:")
    ciudad_origen = input("Ciudad de origen: ")

    # mostrar los destinos disponibles
    
    print("Destinos disponibles:")
    for i, destino in enumerate(destinos_disponibles, start=1):
        print(f"{i}. {destino}")

    opcion_destino = int(input("Seleccione el número de destino: "))
    destino_elegido = destinos_disponibles[opcion_destino - 1]

    cantidad_personas = int(input("Cantidad de personas: "))
    reserva = {
        "Nombre": nombre,
        "apellido":apellido,
        "Ciudad de Origen": ciudad_origen,
        "Tour": destino_elegido,
        "Cantidad de Personas": cantidad_personas
    }

    reservas.append(reserva)
    print("Reserva registrada correctamente.\n")

def listar_todas_reservas():
    print("\n*** Listado de Todas las Reservas ***")
    if not reservas:
        print("No hay reservas registradas.")
    else:
        for reserva in reservas:
            print(f"Cliente: {reserva['Nombre']} ,apellido: {reserva['apellido']} ,Ciudad de Origen: {reserva['Ciudad de Origen']}, Tour: {reserva['Tour']}, Cantidad de Personas: {reserva['Cantidad de Personas']}")
    print()

def imprimir_detalle_por_destino():
    print("\n*** Impresión de Detalle de Reservas por Destino ***")
    print("Destinos disponibles:")
    for i, destino in enumerate(destinos_disponibles, start=1):
        print(f"{i}. {destino}")

    opcion_destino = int(input("Seleccione el número de destino para generar el archivo .txt: "))
    destino_elegido = destinos_disponibles[opcion_destino - 1]

    nombre_archivo = f"reservas_{destino_elegido.lower().replace(' ', '_')}.txt"

    with open(nombre_archivo, "w") as archivo:
        archivo.write(f"Detalle de reservas para {destino_elegido}:\n\n")
        for reserva in reservas:
            if reserva['Tour'] == destino_elegido:
                archivo.write(f"Cliente: {reserva['Nombre']},apellido: {reserva['apellido']}, Ciudad de Origen: {reserva['Ciudad de Origen']}, Cantidad de Personas: {reserva['Cantidad de Personas']}\n")

    print(f"Archivo {nombre_archivo} generado correctamente en el directorio actual.\n")

def main():
    while True:
        print("Bienvenido a SurExplora - Sistema de Reservas")
        print("1. Registrar Reserva")
        print("2. Listar Todas las Reservas")
        print("3. Imprimir Detalle de Reservas por Destino")
        print("4. Salir del Programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_reserva()
        elif opcion == "2":
            listar_todas_reservas()
        elif opcion == "3":
            imprimir_detalle_por_destino()
        elif opcion == "4":
            print("Gracias por utilizar SurExplora. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n")

if __name__ == "__main__":
    main()




