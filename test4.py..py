# test4.py - Sistema básico de evaluación tributaria para el SRI de Costa Rica

def solicitar_datos():
    """Solicita al usuario su nombre, edad e ingreso mensual."""
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    ingreso = float(input("Ingrese su ingreso mensual en USD: "))
    return nombre, edad, ingreso

def evaluar_tributacion(nombre, edad, ingreso):
    """Evalúa y muestra el mensaje correspondiente según los criterios del SRI."""
    if edad >= 18:
        if ingreso > 2000:
            print(f"Estimado usuario: {nombre}, ud. debe tributar.")
        elif ingreso < 500:
            print(f"Estimado usuario: {nombre}, ud. NO debe pagar impuestos.")
        else:
            print(f"Nombre: {nombre} | Edad: {edad}")
            print("Estimado usuario, ud. no es apto para tributar.")
    else:
        print(f"Nombre: {nombre} | Edad: {edad}")
        print("Estimado usuario, ud. no es apto para tributar.")

def main():
    """Función principal del programa."""
    nombre, edad, ingreso = solicitar_datos()
    evaluar_tributacion(nombre, edad, ingreso)

if __name__ == "__main__":
    main()
