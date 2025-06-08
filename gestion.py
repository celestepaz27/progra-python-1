#SISTEMA ACADEMICO
# Guardamos la info en listas
cursos = []
profesores = []
estudiantes = []
 
#CURSOS
 
def buscar_curso_por_codigo(codigo):
    # Busca un curso por su código
    for curso in cursos:
        if curso['codigo'] == codigo:
            return curso
    return None
 
def agregar_curso():
    print("\n-- Agregar Curso --")
    codigo = input("Código del curso (ej. INF101): ").upper()
 
    if buscar_curso_por_codigo(codigo):
        print(f"❌ Ya existe un curso con el código '{codigo}'")
        return
 
    nombre = input("Nombre del curso: ")
    cursos.append({'codigo': codigo, 'nombre': nombre})
    print(f"✅ Curso '{nombre}' agregado correctamente")
 
def listar_cursos():
    print("\n-- Lista de Cursos --")
    if not cursos:
        print("No hay cursos registrados.")
    else:
        for c in cursos:
            print(f"  - [{c['codigo']}] {c['nombre']}")
 
def gestionar_cursos():
    while True:
        print("\n--- Menú Cursos ---")
        print("1. Agregar Curso")
        print("2. Listar Cursos")
        print("3. Volver")
        op = input("Opción: ")
 
        if op == '1':
            agregar_curso()
        elif op == '2':
            listar_cursos()
        elif op == '3':
            break
        else:
            print("❌ Opción no válida")
 
# MENU DE PROFESORES
 
def agregar_profesor():
    print("\n-- Agregar Profesor --")
    if not cursos:
        print("❌ Primero debés agregar al menos un curso.")
        return
 
    cedula = input("Cédula del profe: ")
    nombre = input("Nombre completo: ")
    listar_cursos()
    codigo_curso = input("Código del curso que imparte: ").upper()
 
    if not buscar_curso_por_codigo(codigo_curso):
        print(f"❌ No existe el curso con código '{codigo_curso}'")
        return
 
    profesores.append({'cedula': cedula, 'nombre': nombre, 'curso_codigo': codigo_curso})
    print(f"✅ Profe '{nombre}' agregado al curso {codigo_curso}")
 
def listar_profesores():
    print("\n-- Profes Registrados --")
    if not profesores:
        print("No hay profes registrados.")
        return
 
    for p in profesores:
        curso = buscar_curso_por_codigo(p['curso_codigo'])
        nombre_curso = curso['nombre'] if curso else "Curso desconocido"
        print(f"  - {p['nombre']} ({p['cedula']}) -> {nombre_curso}")
 
def gestionar_profesores():
    while True:
        print("\n--- Menú Profesores ---")
        print("1. Agregar Profesor")
        print("2. Listar Profesores")
        print("3. Volver")
        op = input("Opción: ")
 
        if op == '1':
            agregar_profesor()
        elif op == '2':
            listar_profesores()
        elif op == '3':
            break
        else:
            print("❌ Opción no válida")
 
# LISTA DE ESTUDIANTES
 
def agregar_estudiante():
    print("\n-- Nuevo Estudiante --")
    if not cursos:
        print("❌ Agregá primero al menos un curso.")
        return
 
    cedula = input("Cédula: ")
    nombre = input("Nombre completo: ")
    listar_cursos()
    curso_codigo = input("Código del curso al que se inscribe: ").upper()
 
    if not buscar_curso_por_codigo(curso_codigo):
        print("❌ Ese curso no existe.")
        return
 
    while True:
        try:
            nota = float(input("Nota final (0-100): "))
            if 0 <= nota <= 100:
                break
            else:
                print("⚠️ Nota fuera de rango")
        except ValueError:
            print("⚠️ Eso no es un número")
 
    estudiantes.append({'cedula': cedula, 'nombre': nombre, 'curso_codigo': curso_codigo, 'nota': nota})
    print(f"✅ Estudiante '{nombre}' agregado")
 
def listar_estudiantes():
    print("\n-- Lista de Estudiantes --")
    if not estudiantes:
        print("No hay estudiantes.")
        return
 
    for est in estudiantes:
        curso = buscar_curso_por_codigo(est['curso_codigo'])
        nombre_curso = curso['nombre'] if curso else "Curso no encontrado"
        print(f"  - {est['nombre']} ({est['cedula']}) -> {nombre_curso}, Nota: {est['nota']}")
 
def gestionar_estudiantes():
    while True:
        print("\n--- Menú Estudiantes ---")
        print("1. Agregar Estudiante")
        print("2. Listar Estudiantes")
        print("3. Volver")
        op = input("Opción: ")
 
        if op == '1':
            agregar_estudiante()
        elif op == '2':
            listar_estudiantes()
        elif op == '3':
            break
        else:
            print("❌ Opción no válida")
 
#REPORTE
