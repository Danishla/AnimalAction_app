class Mamifero:
    def caminar(self):
        print("Este mamífero camina")
    def nadar(self):
        print("Este mamífero nada")

class Perro(Mamifero):
    def caminar(self):
        print("El perro camina")
    def nadar(self):
        print("El perro nada")

class Ballena(Mamifero):
    def caminar(self):
        print("Las ballenas no pueden caminar")
    def nadar(self):
        print("La ballena nada")

def obtener_opcion_usuario(opciones, mensaje):
    while True:
        print(mensaje)
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        opcion = input("\nIngrese el número correspondiente: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(opciones):
            return int(opcion) - 1
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def main():
    print("""           
                                               Bienvenido a AnimalAction.
                          Aquí puedes elegir un animal (Mamífero) y una acción para ver cómo se comporta.
          """)
    opciones_animales = ["Perro", "Ballena"]
    opciones_acciones = ["Caminar", "Nadar"]

    while True:
        opcion_animal = obtener_opcion_usuario(opciones_animales, "Elija un animal:")
    
        animal = Perro() if opcion_animal == 0 else Ballena()
        opcion_accion = obtener_opcion_usuario(opciones_acciones, "\nElija una acción:")
        (animal.caminar if opcion_accion == 0 else animal.nadar)()
        if input("\n¿Desea realizar otra acción? (s/n): ").lower() != 's':
            print("\nAdios\nVuelva pronto:) ")
            break

if __name__ == "__main__":
    main()
