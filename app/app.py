import os

def menu():
    print("===Sistema===")
    print("1-Ver archivos")
    print("2-Ver uso de disco") 
    print("3-Ejecutar setup")
    print("4-Salir") 

    op=input("Opcion: ")

    if op == "1":
        os.system("ls")
    elif op == "2":
        os.system("df -h")
    elif op == "3":
        os.system("cd ../Scripts && ./setup.sh")
    elif op == "4":
        print("Saliendo...")
        exit()
    else:
        print("Opcion no valida")

while True:
    menu()