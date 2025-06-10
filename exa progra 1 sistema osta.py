import random
import time

# ========================
# 1. Generador de Artefactos
# ========================
def generar_artefactos(cantidad, longitud=5):
    artefactos = []
    for _ in range(cantidad):
        artefacto = sorted(random.sample(range(1, 21), longitud))
        artefactos.append(artefacto)
    return artefactos

# ========================
# 2. Detector de Coincidencias
# ========================
def detectar_coincidencias(artefactos, señal):
    coincidencias = []
    for idx, artefacto in enumerate(artefactos):
        interseccion = set(artefacto) & set(señal)
        if interseccion:
            coincidencias.append((idx, artefacto, list(interseccion)))
    return coincidencias

# ========================
# 3. Visualizador simple
# ========================
def visualizar_eventos(coincidencias):
    print("\n📡 Eventos de Coincidencia:")
    print("-" * 50)
    if coincidencias:
        print(f"{'ID Artefacto':<15} {'Números':<20} {'Coincidencias'}")
        print("-" * 50)
        for idx, artefacto, interseccion in coincidencias:
            print(f"{idx:<15} {str(artefacto):<20} {interseccion}")
    else:
        print("⚠️  Sin coincidencias detectadas en esta señal")

# ========================
# 4. Simulación en Tiempo Real
# ========================
def simulador_tiempo_real():
    artefactos = generar_artefactos(10)  # Genera 10 artefactos
    print("🛠 Artefactos generados:")
    for idx, artefacto in enumerate(artefactos):
        print(f"#{idx}: {artefacto}")

    print("\n🚦 Iniciando detección de señales... (Presiona Ctrl+C para detener)")

    try:
        while True:
            señal = random.sample(range(1, 21), random.randint(3, 6))
            print(f"\n📥 Señal entrante: {señal}")
            coincidencias = detectar_coincidencias(artefactos, señal)
            visualizar_eventos(coincidencias)
            time.sleep(3)  # Espera 3 segundos antes de la próxima señal

    except KeyboardInterrupt:
        print("\n🛑 Sistema finalizado por el operador")

# ========================
# 5. Entrada Principal
# ========================
if __name__ == "__main__":
    simulador_tiempo_real()
