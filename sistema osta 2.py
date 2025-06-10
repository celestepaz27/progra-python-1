import random
import sys
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

# Variables globales
tabla_1 = []
tabla_2 = []
senales_enviadas = []
coincidencias = []

# Función para crear artefactos
def crear_tablas():
    global tabla_1, tabla_2, senales_enviadas, coincidencias
    codigos = random.sample(range(1, 21), 10)
    tabla_1 = codigos[:5]
    tabla_2 = codigos[5:]
    senales_enviadas.clear()
    coincidencias.clear()
    console.print("\n[bold green]Nuevos artefactos creados correctamente.[/bold green]")
    mostrar_tablas()

# Función para mostrar tablas
def mostrar_tablas():
    table = Table(title="TABLAS DE PREDICCIÓN NUMÉRICA", box=box.ROUNDED, style="cyan")
    table.add_column("Tabla 1", justify="center")
    table.add_column("Tabla 2", justify="center")
    for i in range(5):
        table.add_row(str(tabla_1[i]), str(tabla_2[i]))
    console.print(table)

# Función para enviar una nueva señal
def enviar_senal():
    global senales_enviadas, coincidencias
    disponibles = [n for n in range(1, 21) if n not in senales_enviadas]
    if not disponibles:
        console.print("[bold red]Todas las señales han sido interceptadas.[/bold red]")
        return
    nueva_senal = random.choice(disponibles)
    senales_enviadas.append(nueva_senal)
    console.print(f"\n📡 [bold yellow]Señal interceptada:[/bold yellow] {nueva_senal}")
    if nueva_senal in tabla_1 or nueva_senal in tabla_2:
        coincidencias.append(nueva_senal)
        console.print(f"[bold green]¡Coincidencia detectada con los artefactos![/bold green]")

# Función para ver coincidencias
def ver_coincidencias():
    table = Table(title="ESTADO DE COINCIDENCIAS", box=box.SQUARE, style="magenta")
    table.add_column("Código Interceptado", justify="center")
    table.add_column("Coincide con", justify="center")

    for senal in senales_enviadas:
        match = []
        if senal in tabla_1:
            match.append("Tabla 1")
        if senal in tabla_2:
            match.append("Tabla 2")
        table.add_row(str(senal), ", ".join(match) if match else "-")
    
    if not senales_enviadas:
        console.print("[bold]No se han enviado señales aún.[/bold]")
    else:
        console.print(table)

# Menú principal
def menu():
    while True:
        console.print("\n[bold blue]=== MENÚ TÁCTICO OSTA ===[/bold blue]")
        console.print("1. Crear artefactos (nuevas tablas)")
        console.print("2. Enviar señal")
        console.print("3. Ver coincidencias")
        console.print("4. Reiniciar misión")
        console.print("5. Finalizar operación\n")
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            crear_tablas()
        elif opcion == "2":
            if not tabla_1 or not tabla_2:
                console.print("[bold red]Debe crear los artefactos primero.[/bold red]")
            else:
                enviar_senal()
        elif opcion == "3":
            ver_coincidencias()
        elif opcion == "4":
            crear_tablas()
        elif opcion == "5":
            console.print("\n[bold red]Operación finalizada. Cerrando sistema OSTA...[/bold red]")
            sys.exit()
        else:
            console.print("[bold red]Opción no válida. Intente de nuevo.[/bold red]")

# Iniciar el sistema
if __name__ == "__main__":
    console.print("[bold cyan]Bienvenido al Sistema Autónomo de la OSTA[/bold cyan]")
    menu()
