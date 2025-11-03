import os
from db.connection import conectar
from db.queries import Queries
from prettytable import PrettyTable


def mostrar_menu_principal():
    print("SISTEMA DE GESTION DE PARQUEADERO")
    print("[1] Gestion de Tipo de Vehiculos")
    print("[2] Registro de Entrada de Vehiculo")
    print("[3] Listar Vehiculos Activos")
    print("[0] Salir")

def menu_tipos_vehiculos():
    print("GESTION DE TIPO DE VEHICULOS")
    print("[1] Crear un Nuevo Tipo Vehiculo")
    print("[2] Listar Tipos Vehiculos")
    print("[0] Salir")

    opcion = input("Seleccione un opcion: ")

    match opcion:
        case "1":
            crear_tipo_vehiculo()
        case "2":
            listar_tipo_vehicuos()
        case "0":
            print("Saliendo del menu de tipos de vehiculos...")
            return


def crear_tipo_vehiculo():
    print("Crear nuevo tipo de vehiculo")

    nombre = input("Nombre del tipo de Vehiculo: ")
    tarifa = float(input("Tarifa por hora: $"))
    limite = int(input("Limiete de vehiculo: "))

    Queries.crear_tipo_vehiculo(nombre,tarifa,limite)

def listar_tipo_vehicuos():
    print("TIPOS DE VEHICULOS REGISTRADOS")

    tipos = Queries.listar_tipos_vehiculos()

    table = PrettyTable()

    table.field_names = ["ID", "Nombre", "Tarifa($)", "Limite", "Creado en"]
    table.title = "Tipos de Vehiculos"
    for tipo in tipos:
        table.add_row([tipo.id, tipo.nombre, f"$ {tipo.tarifa}", tipo.limite, tipo.createdAt])
    print(table)

def registrar_entrada_vehiculo():
    
    try:
        print("REGISTRO DE ENTRADA DE VEHICULO")
        listar_tipo_vehicuos()
        idTipoVehiculo = int(input("Seleccione el ID del tipo de vehiculo: "))
        placa = input("Placa del vehiculo: ")
        documento = input("Documento del propietario: ")
        nombre = input("Nombre del propietario: ")
        Queries.registrar_entrada(idTipoVehiculo,placa,documento,nombre)
    except ValueError as ve:
        print(f"[ERROR] Entrada invalida: {ve}")

def listar_vehiculos_activos():
    print("VEHICULOS ACTIVOS")

    vehiculos = Queries.listar_vehiculos_activos()

    table = PrettyTable()

    table.field_names = ["ID", "Placa", "Nombre", "Documento", "Hora de Llegada", "Tipo Vehiculo"]
    table.title = "Vehiculos Activos"
    for vehiculo in vehiculos:
        table.add_row(vehiculo[0],vehiculo[1],vehiculo[2],vehiculo[3],vehiculo[4],vehiculo[5])
    print(table)

def registrar_salida_vehiculo():
    print("REGISTRO DE SALIDA DE VEHICULO")

    idVehiculo = int(input("Ingrese el ID del vehiculo a registrar salida: "))

    Queries.registrar_salida(idVehiculo)

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opcion: ")

        match opcion:
            case "1":
                menu_tipos_vehiculos()
            case "2":
                registrar_entrada_vehiculo()
            case "3":
                listar_vehiculos_activos()
            case "4":
                registrar_salida_vehiculo()
            case "0":
                print("Saliendo del sistema...")
                break


main()