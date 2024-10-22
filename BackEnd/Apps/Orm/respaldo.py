from django.db.models import F
from django.db.models import Q
from django.db.models import Sum, Avg, Max, Min, Count
from BackEnd.Apps.Orm.models import *


# Insertar un registro directamente en la base de datos
tipo1 = TipoSangre.objects.create(tipo="A+", descripcion="Tipo A positivo")

# Crear el registro en memoria (sin guardarlo aún en la base de datos)
tipo2 = TipoSangre(tipo="B-", descripcion="Tipo B negativo")
# Guardar el registro en la base de datos
tipo2.save()

# Crear una lista de instancias de TipoSangre con varios tipos de sangre
tipos_sangre = [
  TipoSangre(tipo="B+", descripcion="Tipo B positivo"),
  TipoSangre(tipo="B-", descripcion="Tipo B negativo"),
]

# Insertar múltiples registros en la base de datos de una sola vez
TipoSangre.objects.bulk_create(tipos_sangre)

# Consultar todos los registros de TipoSangre y mostrar sus campos
tipos_sangre = TipoSangre.objects.all()
for tipo in tipos_sangre:
  print(f"Tipo: {tipo.tipo}, Descripción: {tipo.descripcion}")

# Obtener un registro por tipo de sangre específico
tipo_O_pos = TipoSangre.objects.get(tipo="O+")
tipo_A = TipoSangre.objects.get(tipo="A")
tipo_ab_pos = TipoSangre.objects.get(tipo="AB+")

# Crear una lista de instancias de Paciente
pacientes = [
  Paciente(
    nombres="Juan",
    apellidos="Pérez",
    cedula="1234567890",
    fecha_nacimiento="1980-01-15",
    telefono="0998765432",
    email="juan.perez@example.com",
    sexo="M",
    estado_civil="C",
    direccion="Calle Falsa 123",
    latitud=-0.123456,
    longitud=-78.123456,
    tipo_sangre=tipo_O_pos,
    alergias="Ninguna",
    enfermedades_cronicas="Hipertensión",
    medicacion_actual="Losartán",
    cirugias_previas="Apendicectomía",
    antecedentes_personales="Diabetes en tratamiento",
    antecedentes_familiares="Corazón en la familia"
  ),
  Paciente(
    nombres="María",
    apellidos="Gómez",
    cedula="0987654321",
    fecha_nacimiento="1990-05-20",
    telefono="0991234567",
    email="maria.gomez@example.com",
    sexo="F",
    estado_civil="S",
    direccion="Av. Libertad 456",
    latitud=-0.654321,
    longitud=-78.654321,
    tipo_sangre=tipo_A,
    alergias="Penicilina",
    enfermedades_cronicas="Asma",
    medicacion_actual="Salbutamol",
    cirugias_previas="Ninguna",
    antecedentes_personales="No fuma",
    antecedentes_familiares="Madre con cáncer"
  ),
  Paciente(
    nombres="Carlos",
    apellidos="Ramírez",
    cedula="1357924680",
    fecha_nacimiento="1975-09-30",
    telefono="0987654321",
    email="carlos.ramirez@example.com",
    sexo="M",
    estado_civil="C",
    direccion="Calle 10 de Agosto 789",
    latitud=-0.321654,
    longitud=-78.321654,
    tipo_sangre=tipo_ab_pos,
    alergias="Ninguna",
    enfermedades_cronicas="Ninguna",
    medicacion_actual="Ninguna",
    cirugias_previas="Ninguna",
    antecedentes_personales="No antecedentes relevantes",
    antecedentes_familiares="Padre con hipertensión"
  ),
]

# Insertar múltiples registros de Paciente en la base de datos
Paciente.objects.bulk_create(pacientes)

# Consultar y mostrar todos los pacientes
pacientes = Paciente.objects.all()
for paciente in pacientes:
  print(f"--- Paciente ---")
  print(f"Nombres: {paciente.nombres}")
  print(f"Apellidos: {paciente.apellidos}")
  print(f"Cédula: {paciente.cedula}")
  print(f"Fecha de Nacimiento: {paciente.fecha_nacimiento}")
  print(f"Teléfono: {paciente.telefono}")
  print(f"Email: {paciente.email}")
  print(f"Sexo: {paciente.sexo}")
  print(f"Estado Civil: {paciente.estado_civil}")
  print(f"Dirección: {paciente.direccion}")
  print(f"Latitud: {paciente.latitud}")
  print(f"Longitud: {paciente.longitud}")
  print(f"Tipo de Sangre: {paciente.tipo_sangre.tipo if paciente.tipo_sangre else 'No especificado'}")
  print(f"Alergias: {paciente.alergias if paciente.alergias else 'Ninguna'}")
  print(f"Enfermedades Crónicas: {paciente.enfermedades_cronicas if paciente.enfermedades_cronicas else 'Ninguna'}")
  print(f"Medicación Actual: {paciente.medicacion_actual if paciente.medicacion_actual else 'Ninguna'}")
  print(f"Cirugías Previas: {paciente.cirugias_previas if paciente.cirugias_previas else 'Ninguna'}")
  print(
    f"Antecedentes Personales: {paciente.antecedentes_personales if paciente.antecedentes_personales else 'Ninguno'}")
  print(
    f"Antecedentes Familiares: {paciente.antecedentes_familiares if paciente.antecedentes_familiares else 'Ninguno'}")
  print("-----------------------------")

# Consultar pacientes con tipo de sangre O+
pacientes_o_plus = Paciente.objects.filter(tipo_sangre__tipo="O+")

# Consulta utilizando filtros de texto (icontains busca sin distinguir mayúsculas)
pacientes_con_o = Paciente.objects.filter(tipo_sangre__tipo__icontains="O")

# Buscar pacientes cuyos nombres comiencen con "y" o "w" (sin importar mayúsculas)
empleados_con_yw = Paciente.objects.filter(nombres__iregex=r'^[yw]')

# Consultar pacientes nacidos en 2024 y mostrar apellidos y fecha de nacimiento
pacientes_2024 = Paciente.objects.filter(fecha_nacimiento__year=2024).values('apellidos', 'fecha_nacimiento')

# Consultar pacientes que nacieron antes de 2024
pacientes_menor_2024 = Paciente.objects.filter(fecha_nacimiento__year__lt=2024).values('apellidos', 'fecha_nacimiento')
pacientes_menor_2024 = list(pacientes_menor_2024)  # Convertir a lista

# Obtener nombres y descripción del tipo de sangre de pacientes con "AB+"
pacientes_ab = Paciente.objects.filter(tipo_sangre__tipo="AB+").values('nombres', 'apellidos',
                                                                       'tipo_sangre__descripcion')

# Consulta inversa: obtener todos los pacientes con tipo de sangre "AB+"
tipo_sangre_ab = TipoSangre.objects.get(tipo="AB+")
pacientes_con_ab = tipo_sangre_ab.tipos_sangre.all()

# Consulta con AND: pacientes nacidos en 1980 y tipo de sangre "O+"
pacientes = Paciente.objects.filter(fecha_nacimiento__year=1980, tipo_sangre__tipo="O+")

# Consulta con OR: pacientes nacidos en 1980 o con tipo de sangre "O+"
pacientes = Paciente.objects.filter(Q(fecha_nacimiento__year=1980) | Q(tipo_sangre__tipo="O+"))

# Filtrar pacientes nacidos en 1980 o con tipo de sangre "O+" y sin alergias
pacientes = Paciente.objects.filter(Q(fecha_nacimiento__year=1980) | Q(tipo_sangre__tipo="O+"), alergias__isnull=True)

# Excluir pacientes con tipo de sangre "AB+" y mostrar apellidos y descripción
pacientes = Paciente.objects.exclude(tipo_sangre__tipo="AB+").values('apellidos', 'tipo_sangre__descripcion')

# Obtener pacientes nacidos después de 1980 excluyendo tipo de sangre "O+"
pacientes = Paciente.objects.filter(fecha_nacimiento__year__gt=1980).exclude(tipo_sangre__tipo="O+").values('apellidos',
                                                                                                            'tipo_sangre__descripcion')

# Obtener cargo con id 1 (ej. Enfermera)
cargo_1 = Cargo.objects.get(id=1)

# Crear y guardar empleados en la base de datos
empleado1 = Empleado(
  nombres="Juan",
  apellidos="Pérez",
  cedula="1234567890",
  fecha_nacimiento="1990-01-01",
  cargo=cargo_1,
  sueldo=1500.00,
  direccion="Calle 1, Ciudad",
  latitud=-0.123456,
  longitud=-78.123456,
)
empleado1.save()

empleado2 = Empleado(
  nombres="María",
  apellidos="Gómez",
  cedula="0987654321",
  fecha_nacimiento="1985-05-15",
  cargo=cargo_1,
  sueldo=1800.00,
  direccion="Calle 2, Ciudad",
  latitud=-0.654321,
  longitud=-78.654321,
)
empleado2.save()

# Consultar todos los empleados y mostrar sus nombres, apellidos y cargos
empleados = Empleado.objects.all()
for empleado in empleados:
  print(f"{empleado.nombres} {empleado.apellidos} - Cargo: {empleado.cargo.descripcion}")

# Calcular el número de pacientes por tipo de sangre
pacientes_por_tipo_sangre = Paciente.objects.values('tipo_sangre__tipo').annotate(total=Count('tipo_sangre'))
for registro in pacientes_por_tipo_sangre:
  print(f"Tipo de Sangre: {registro['tipo_sangre__tipo']}, Total: {registro['total']}")

# Mostrar el nombre y el sueldo de todos los empleados
emps = Empleado.objects.values('nombres', 'sueldo')

# Consulta de agregados para empleados con cargo "Enfermera"
resultados = Empleado.objects.filter(cargo__descripcion__icontains="Enfermera").aggregate(
  total_sueldo=Sum('sueldo'),
  promedio_sueldo=Avg('sueldo'),
  max_sueldo=Max('sueldo'),
  min_sueldo=Min('sueldo'),
  cantidad_enfermeras=Count('id')
)

# Consulta de agregados agrupados por cargo
resultados = Empleado.objects.values('cargo__nombre').annotate(
  total_sueldo=Sum('sueldo'),
  promedio_sueldo=Avg('sueldo'),
  max_sueldo=Max('sueldo'),
  min_sueldo=Min('sueldo'),
  cantidad_empleados=Count('id')
)

# Consulta de agregados agrupados por cargo y sueldo
resultados = Empleado.objects.values('cargo__nombre', 'sueldo').annotate(
  cantidad_empleados=Count('id')
).order_by('cargo__nombre', 'sueldo')

# Consulta de empleados con el nombre del cargo como alias
resultados = Empleado.objects.annotate(
  cargo_descripcion=F('cargo__nombre')
)

# Actualizar los sueldos en un 10% para empleados cuyo cargo sea "Enfermera"
Empleado.objects.filter(cargo__nombre="Enfermera").update(sueldo=F('sueldo') * 1.10, direccion='Guayaquil')

# Actualizar la descripción del cargo con id 3
cargo = Cargo.objects.get(id=3)
cargo.descripcion = "Financiero"
cargo.save()

# Eliminar los tipos de sangre cuya descripción contenga "positivo"
tipos_eliminados = TipoSangre.objects.filter(descripcion__iendswith="positivo").delete()

# Eliminar el cargo con id 3
cargo = Cargo.objects.get(id=3)
cargo.delete()
