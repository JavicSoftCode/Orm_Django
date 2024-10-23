from django.db.models import Sum, Avg, Max, Min, Count, F, Q
from django.db import transaction
from BackEnd.Apps.Orm.models import *


# from BackEnd.Apps.Orm.orm import Orm
# orm_instance = Orm()

# Comandos
# python manage.py shell_plus --print-sql      USAR ESTE DE AQUI


# Practica JavicSoftCode
class Orm:

  # <<<<< ORM MODELO TIPO SANGRE >>>>>
  def createTipoSangre(self):
    # Insertar un registro directamente en la base de datos
    TipoSangre.objects.create(tipo="O+", descripcion="Tipo 0 positivo")

    #  CONSOLA SHELL PLUS >>>>>

    # SENTENCIA SQL <<<<<
    # INSERT INTO "Orm_tiposangre" ("tipo", "descripcion")
    # VALUES ('O+', 'Tipo O positivo') RETURNING "Orm_tiposangre"."id"

# ==============================================================================================

  def saveTipoSangre(self):
    # Crear el registro en memoria (sin guardarlo aún en la base de datos)
    tipo2 = TipoSangre(tipo="A-", descripcion="Tipo A negativo")
    # Guardar el registro en la base de datos
    tipo2.save()

    #  CONSOLA SHELL PLUS >>>>>

    # SENTENCIA SQL <<<<<
    # INSERT INTO "Orm_tiposangre" ("tipo", "descripcion")
    # VALUES ('A-', 'Tipo A negativo') RETURNING "Orm_tiposangre"."id"

# ==============================================================================================

  def bulk_createTiposSangre(self):
    # Crear una lista de instancias de TipoSangre con varios tipos de sangre
    tipos_sangre = [
      TipoSangre(tipo="Z+", descripcion="Tipo Z positivo"),
      TipoSangre(tipo="X-", descripcion="Tipo X negativo"),
    ]

    # Insertar múltiples registros en la base de datos de una sola vez
    TipoSangre.objects.bulk_create(tipos_sangre)

    #  CONSOLA SHELL PLUS >>>>>

    # SENTENCIA SQL <<<<<
    # INSERT INTO "Orm_tiposangre" ("tipo", "descripcion")
    # VALUES ('Z+', 'Tipo Z positivo'), ('X-', 'Tipo X negativo') RETURNING "Orm_tiposangre"."id"

# ==============================================================================================

  def allTiposSangre(self):
    # Consultar todos los registros de TipoSangre y mostrar sus campos
    tipos_sangre = TipoSangre.objects.all()
    for tipo in tipos_sangre:
      print(f"Tipo: {tipo.tipo}, Descripción: {tipo.descripcion}")

      #  CONSOLA SHELL PLUS >>>>>
      # In [2]: orm_instance.allTiposSangre()
      # Tipo: A+, Descripción: Tipo A positivo
      # Tipo: B-, Descripción: Tipo B negativo
      # Tipo: O+, Descripción: Tipo O positivo
      # Tipo: A-, Descripción: Tipo A negativo
      # Tipo: Z+, Descripción: Tipo Z positivo
      # Tipo: X-, Descripción: Tipo X negativo

      # SENTENCIA SQL <<<<<
      # SELECT "Orm_tiposangre"."id",
      #        "Orm_tiposangre"."tipo",
      #        "Orm_tiposangre"."descripcion"
      #   FROM "Orm_tiposangre"

# ==============================================================================================

  def findTiposSangre(self):
    # Obtener un registro por tipo de sangre específico
    tipo_O_pos = TipoSangre.objects.get(tipo="O+")  # 1
    tipo_A = TipoSangre.objects.get(tipo="A-")  # 2
    tipo_ab_pos = TipoSangre.objects.get(tipo="X-")  # 3

    #  CONSOLA SHELL PLUS >>>>>

    # SENTENCIA SQL <<<<<

    # 1 )
    # SELECT "Orm_tiposangre"."id",
    #        "Orm_tiposangre"."tipo",
    #        "Orm_tiposangre"."descripcion"
    #   FROM "Orm_tiposangre"
    #  WHERE "Orm_tiposangre"."tipo" = 'O+'
    #  LIMIT 21

    # 2 )
    # SELECT "Orm_tiposangre"."id",
    #        "Orm_tiposangre"."tipo",
    #        "Orm_tiposangre"."descripcion"
    #   FROM "Orm_tiposangre"
    #  WHERE "Orm_tiposangre"."tipo" = 'A-'
    #  LIMIT 21

    # 3 )
    # SELECT "Orm_tiposangre"."id",
    #        "Orm_tiposangre"."tipo",
    #        "Orm_tiposangre"."descripcion"
    #   FROM "Orm_tiposangre"
    #  WHERE "Orm_tiposangre"."tipo" = 'X-'
    #  LIMIT 21

# ==============================================================================================

  # <<<<< ORM MODELO PACIENTE >>>>>
  def bulk_createPaciente(self):
    tipo_O_pos = TipoSangre.objects.get(tipo="O+")  # 1
    tipo_A = TipoSangre.objects.get(tipo="A-")  # 2
    tipo_ab_pos = TipoSangre.objects.get(tipo="X-")  # 3

    # Crear una lista de instancias de Paciente
    pacientes = [
      Paciente(
        nombres="Juanita",
        apellidos="Vera",
        cedula="0212547895",
        fecha_nacimiento="1990-01-15",
        telefono="0326598698",
        email="juanitaveraperez@example.com",
        sexo="F",
        estado_civil="C",
        direccion="Calle Av.  123",
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
        nombres="Daniela",
        apellidos="Rumazo",
        cedula="0123659856",
        fecha_nacimiento="2002-09-30",
        telefono="0987654321",
        email="annie123@example.com",
        sexo="F",
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

    #  CONSOLA SHELL PLUS >>>>>

    # SENTENCIA SQL <<<<<
    # INSERT INTO "Orm_paciente"
    # ("nombres", "apellidos", "cedula", "fecha_nacimiento", "telefono", "email", "sexo", "estado_civil", "direccion",
    #  "latitud", "longitud", "tipo_sangre_id", "alergias", "enfermedades_cronicas", "medicacion_actual",
    #  "cirugias_previas", "antecedentes_personales", "antecedentes_familiares")
    # VALUES
    # ('Juanita', 'Vera', '0212547895', '1990-01-15'
    #  ::date, '0326598698', 'juanitaveraperez@example.com', 'F', 'C', 'Calle Av. 123', -0.123456, -78.123456, 77, 'Ninguna', 'Hipertensión', 'Losartán', 'Apendicectomía', 'Diabetes en tratamiento', 'Corazón en la familia'),
    # ('María', 'Gómez', '0987654321', '1990-05-20'
    #  ::date, '0991234567', 'maria.gomez@example.com', 'F', 'S', 'Av. Libertad 456', -0.654321, -78.654321, 78, 'Penicilina', 'Asma', 'Salbutamol', 'Ninguna', 'No fuma', 'Madre con cáncer'),
    # ('Daniela', 'Rumazo', '0123659856', '2002-09-30'
    #  ::date, '0987654321', 'annie123@example.com', 'F', 'C', 'Calle 10 de Agosto 789', -0.3216, -78.3216, 77, 'Alergia a polvo', 'Migrañas', 'Ibuprofeno', 'Ninguna', 'Sana', 'Padre hipertenso');

# ==============================================================================================

  def allPaciente(self):
    # Consultar y mostrar todos los pacientes
    pacientes = Paciente.objects.all()
    for paciente in pacientes:
      print("===== Formulario de Paciente =====")
      print(f"Nombres:               {paciente.nombres}")
      print(f"Apellidos:             {paciente.apellidos}")
      print(f"Cédula:                {paciente.cedula}")
      print(f"Fecha de Nacimiento:   {paciente.fecha_nacimiento}")
      print(f"Teléfono:              {paciente.telefono}")
      print(f"Email:                 {paciente.email}")
      print(f"Sexo:                  {paciente.sexo}")
      print(f"Estado Civil:          {paciente.estado_civil}")
      print(f"Dirección:             {paciente.direccion}")
      print(f"Latitud:               {paciente.latitud}")
      print(f"Longitud:              {paciente.longitud}")
      print(f"Tipo de Sangre:        {paciente.tipo_sangre.tipo if paciente.tipo_sangre else 'No especificado'}")
      print(f"Alergias:              {paciente.alergias if paciente.alergias else 'Ninguna'}")
      print(f"Enfermedades Crónicas: {paciente.enfermedades_cronicas if paciente.enfermedades_cronicas else 'Ninguna'}")
      print(f"Medicación Actual:     {paciente.medicacion_actual if paciente.medicacion_actual else 'Ninguna'}")
      print(f"Cirugías Previas:      {paciente.cirugias_previas if paciente.cirugias_previas else 'Ninguna'}")
      print(
        f"Antecedentes Personales: {paciente.antecedentes_personales if paciente.antecedentes_personales else 'Ninguno'}")
      print(
        f"Antecedentes Familiares: {paciente.antecedentes_familiares if paciente.antecedentes_familiares else 'Ninguno'}")
      print("===============================")

      #  CONSOLA SHELL PLUS >>>>>
      # ============ Formulario de Paciente ============
      # Nombres:               Juanita
      # Apellidos:             Vera
      # Cédula:                0212547895
      # Fecha de Nacimiento:   1990-01-15
      # Teléfono:              0326598698
      # Email:                 juanitaveraperez@example.com
      # Sexo:                  F
      # Estado Civil:          C
      # Dirección:             Calle Av. 123
      # Latitud:               -0.123456
      # Longitud:              -78.123456
      # Tipo de Sangre:        O+
      # Alergias:              Ninguna
      # Enfermedades Crónicas: Hipertensión
      # Medicación Actual:     Losartán
      # Cirugías Previas:      Apendicectomía
      # Antecedentes Personales: Diabetes en tratamiento
      # Antecedentes Familiares: Corazón en la familia
      # ==========================================

      # ============ Formulario de Paciente ============
      # Nombres:               Daniela
      # Apellidos:             Rumazo
      # Cédula:                0123659856
      # Fecha de Nacimiento:   2002-09-30
      # Teléfono:              0987654321
      # Email:                 annie123@example.com
      # Sexo:                  F
      # Estado Civil:          C
      # Dirección:             Calle 10 de Agosto 789
      # Latitud:               -0.321600
      # Longitud:              -78.321600
      # Tipo de Sangre:        O+
      # Alergias:              Alergia a polvo
      # Enfermedades Crónicas: Migrañas
      # Medicación Actual:     Ibuprofeno
      # Cirugías Previas:      Ninguna
      # Antecedentes Personales: Sana
      # Antecedentes Familiares: Padre hipertenso
      # ==========================================

      # ============ Formulario de Paciente ============
      # Nombres:               Juanita
      # Apellidos:             Vera
      # Cédula:                0212547895
      # Fecha de Nacimiento:   1990-01-15
      # Teléfono:              0326598698
      # Email:                 juanitaveraperez@example.com
      # Sexo:                  F
      # Estado Civil:          C
      # Dirección:             Calle Av. 123
      # Latitud:               -0.123456
      # Longitud:              -78.123456
      # Tipo de Sangre:        O+
      # Alergias:              Ninguna
      # Enfermedades Crónicas: Hipertensión
      # Medicación Actual:     Losartán
      # Cirugías Previas:      Apendicectomía
      # Antecedentes Personales: Diabetes en tratamiento
      # Antecedentes Familiares: Corazón en la familia
      # ==========================================

      # SENTENCIA SQL <<<<<
      # SELECT "Orm_paciente"."id",
      #        "Orm_paciente"."nombres",
      #        "Orm_paciente"."apellidos",
      #        "Orm_paciente"."cedula",
      #        "Orm_paciente"."fecha_nacimiento",
      #        "Orm_paciente"."telefono",
      #        "Orm_paciente"."email",
      #        "Orm_paciente"."sexo",
      #        "Orm_paciente"."estado_civil",
      #        "Orm_paciente"."direccion",
      #        "Orm_paciente"."latitud",
      #        "Orm_paciente"."longitud",
      #        "Orm_paciente"."tipo_sangre_id",
      #        "Orm_paciente"."alergias",
      #        "Orm_paciente"."enfermedades_cronicas",
      #        "Orm_paciente"."medicacion_actual",
      #        "Orm_paciente"."cirugias_previas",
      #        "Orm_paciente"."antecedentes_personales",
      #        "Orm_paciente"."antecedentes_familiares"
      #   FROM "Orm_paciente"
      #  ORDER BY "Orm_paciente"."apellidos" ASC

# ==============================================================================================

  def findPaciente_O_Post(self):
    # Consultar pacientes con tipo de sangre O+
   return Paciente.objects.filter(tipo_sangre__tipo="O+")

    #  CONSOLA SHELL PLUS >>>>>
    # <QuerySet [<Paciente: Daniela>]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_paciente"."id",
    #        "Orm_paciente"."nombres",
    #        "Orm_paciente"."apellidos",
    #        "Orm_paciente"."cedula",
    #        "Orm_paciente"."fecha_nacimiento",
    #        "Orm_paciente"."telefono",
    #        "Orm_paciente"."email",
    #        "Orm_paciente"."sexo",
    #        "Orm_paciente"."estado_civil",
    #        "Orm_paciente"."direccion",
    #        "Orm_paciente"."latitud",
    #        "Orm_paciente"."longitud",
    #        "Orm_paciente"."tipo_sangre_id",
    #        "Orm_paciente"."alergias",
    #        "Orm_paciente"."enfermedades_cronicas",
    #        "Orm_paciente"."medicacion_actual",
    #        "Orm_paciente"."cirugias_previas",
    #        "Orm_paciente"."antecedentes_personales",
    #        "Orm_paciente"."antecedentes_familiares"
    #   FROM "Orm_paciente"
    #  INNER JOIN "Orm_tiposangre"
    #     ON ("Orm_paciente"."tipo_sangre_id" = "Orm_tiposangre"."id")
    #  WHERE "Orm_tiposangre"."tipo" = 'O+'
    #  ORDER BY "Orm_paciente"."apellidos" ASC
    #  LIMIT 21

# ==============================================================================================

  def findPaciente_O(self):
    # Consulta utilizando filtros de texto (icontains busca sin distinguir mayúsculas)
    return Paciente.objects.filter(tipo_sangre__tipo__icontains="O")

    #  CONSOLA SHELL PLUS >>>>>
    # <QuerySet [<Paciente: Marta>, <Paciente: Daniela>]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_paciente"."id",
    #        "Orm_paciente"."nombres",
    #        "Orm_paciente"."apellidos",
    #        "Orm_paciente"."cedula",
    #        "Orm_paciente"."fecha_nacimiento",
    #        "Orm_paciente"."telefono",
    #        "Orm_paciente"."email",
    #        "Orm_paciente"."sexo",
    #        "Orm_paciente"."estado_civil",
    #        "Orm_paciente"."direccion",
    #        "Orm_paciente"."latitud",
    #        "Orm_paciente"."longitud",
    #        "Orm_paciente"."tipo_sangre_id",
    #        "Orm_paciente"."alergias",
    #        "Orm_paciente"."enfermedades_cronicas",
    #        "Orm_paciente"."medicacion_actual",
    #        "Orm_paciente"."cirugias_previas",
    #        "Orm_paciente"."antecedentes_personales",
    #        "Orm_paciente"."antecedentes_familiares"
    #   FROM "Orm_paciente"
    #  INNER JOIN "Orm_tiposangre"
    #     ON ("Orm_paciente"."tipo_sangre_id" = "Orm_tiposangre"."id")
    #  WHERE UPPER("Orm_tiposangre"."tipo"::text) LIKE UPPER('%O%')
    #  ORDER BY "Orm_paciente"."apellidos" ASC
    #  LIMIT 21

# ==============================================================================================

  def findPaciente_init_YandW(self):
    # Buscar pacientes cuyos nombres comiencen con "y" o "w" (sin importar mayúsculas)
     return Paciente.objects.filter(nombres__iregex=r'^[yw]')

      #  CONSOLA SHELL PLUS >>>>>
      #  <QuerySet [<Paciente: Yoyo>, <Paciente: williams>]>

      # SENTENCIA SQL <<<<<
      # SELECT "Orm_paciente"."id",
      #        "Orm_paciente"."nombres",
      #        "Orm_paciente"."apellidos",
      #        "Orm_paciente"."cedula",
      #        "Orm_paciente"."fecha_nacimiento",
      #        "Orm_paciente"."telefono",
      #        "Orm_paciente"."email",
      #        "Orm_paciente"."sexo",
      #        "Orm_paciente"."estado_civil",
      #        "Orm_paciente"."direccion",
      #        "Orm_paciente"."latitud",
      #        "Orm_paciente"."longitud",
      #        "Orm_paciente"."tipo_sangre_id",
      #        "Orm_paciente"."alergias",
      #        "Orm_paciente"."enfermedades_cronicas",
      #        "Orm_paciente"."medicacion_actual",
      #        "Orm_paciente"."cirugias_previas",
      #        "Orm_paciente"."antecedentes_personales",
      #        "Orm_paciente"."antecedentes_familiares"
      #   FROM "Orm_paciente"
      #  WHERE "Orm_paciente"."nombres"::text ~* '^[yw]'
      #  ORDER BY "Orm_paciente"."apellidos" ASC
      #  LIMIT 21

# ==============================================================================================

  def findPaciente_Nac_2024(self):
    # Consultar pacientes nacidos en 2024 y mostrar apellidos y fecha de nacimiento
     return Paciente.objects.filter(fecha_nacimiento__year=2024).values('apellidos', 'fecha_nacimiento')

      #  CONSOLA SHELL PLUS >>>>>
      # <QuerySet [{'apellidos': 'Gómez', 'fecha_nacimiento': datetime.date(2024, 5, 20)}]>

      # SENTENCIA SQL <<<<<
      # SELECT "Orm_paciente"."apellidos",
      #        "Orm_paciente"."fecha_nacimiento"
      #   FROM "Orm_paciente"
      #  WHERE "Orm_paciente"."fecha_nacimiento" BETWEEN '2024-01-01'::date AND '2024-12-31'::date
      #  ORDER BY "Orm_paciente"."apellidos" ASC
      #  LIMIT 21

# ==============================================================================================

  def findPaciente_Before_2024(self):
    # Consultar pacientes que nacieron antes de 2024
    pacientes = Paciente.objects.filter(fecha_nacimiento__year__lt=2024).values('apellidos', 'fecha_nacimiento')
    return list(pacientes)  # Convertir a lista

      #  CONSOLA SHELL PLUS >>>>>
      #  [{'apellidos': 'Quiñonez', 'fecha_nacimiento': datetime.date(1999, 9, 30)},
      #  {'apellidos': 'Rumazo', 'fecha_nacimiento': datetime.date(1980, 9, 30)},
      #  {'apellidos': 'Vera', 'fecha_nacimiento': datetime.date(1990, 1, 15)}]

      # SENTENCIA SQL <<<<<
      # SELECT "Orm_paciente"."apellidos",
      #        "Orm_paciente"."fecha_nacimiento"
      #   FROM "Orm_paciente"
      #  WHERE "Orm_paciente"."fecha_nacimiento" < '2024-01-01'::date
      #  ORDER BY "Orm_paciente"."apellidos" ASC

# ==============================================================================================

  def findPaciente_TipSangre_XPost(self):
    # Obtener nombres y descripción del tipo de sangre de pacientes con "X+"
    return Paciente.objects.filter(tipo_sangre__tipo="X+").values('nombres', 'apellidos', 'tipo_sangre__descripcion')

      #  CONSOLA SHELL PLUS >>>>>
      # <QuerySet [{'nombres': 'williams', 'apellidos': 'Vera', 'tipo_sangre__descripcion': 'Tipo X positivo'}]>

      # SENTENCIA SQL <<<<<
      # SELECT "Orm_paciente"."nombres",
      #        "Orm_paciente"."apellidos",
      #        "Orm_tiposangre"."descripcion"
      #   FROM "Orm_paciente"
      #  INNER JOIN "Orm_tiposangre"
      #     ON ("Orm_paciente"."tipo_sangre_id" = "Orm_tiposangre"."id")
      #  WHERE "Orm_tiposangre"."tipo" = 'X+'
      #  ORDER BY "Orm_paciente"."apellidos" ASC
      #  LIMIT 21

# ==============================================================================================

  def findPaciente_Inversa_O_Post(self):
    # Consulta inversa: obtener todos los pacientes con tipo de sangre "AB+"
    tipo_sangre_ab = TipoSangre.objects.get(tipo="O+")
    return tipo_sangre_ab.tipos_sangre.all()

      #  CONSOLA SHELL PLUS >>>>>
      # <QuerySet [<Paciente: Marta>, <Paciente: Daniela>]>

      # SENTENCIA SQL <<<<<
      # SELECT "Orm_tiposangre"."id",
      #        "Orm_tiposangre"."tipo",
      #        "Orm_tiposangre"."descripcion"
      #   FROM "Orm_tiposangre"
      #  WHERE "Orm_tiposangre"."tipo" = 'O+'
      #  LIMIT 21

      # SELECT "Orm_paciente"."id",
      #        "Orm_paciente"."nombres",
      #        "Orm_paciente"."apellidos",
      #        "Orm_paciente"."cedula",
      #        "Orm_paciente"."fecha_nacimiento",
      #        "Orm_paciente"."telefono",
      #        "Orm_paciente"."email",
      #        "Orm_paciente"."sexo",
      #        "Orm_paciente"."estado_civil",
      #        "Orm_paciente"."direccion",
      #        "Orm_paciente"."latitud",
      #        "Orm_paciente"."longitud",
      #        "Orm_paciente"."tipo_sangre_id",
      #        "Orm_paciente"."alergias",
      #        "Orm_paciente"."enfermedades_cronicas",
      #        "Orm_paciente"."medicacion_actual",
      #        "Orm_paciente"."cirugias_previas",
      #        "Orm_paciente"."antecedentes_personales",
      #        "Orm_paciente"."antecedentes_familiares"
      #   FROM "Orm_paciente"
      #  WHERE "Orm_paciente"."tipo_sangre_id" = 77
      #  ORDER BY "Orm_paciente"."apellidos" ASC
      #  LIMIT 21

# ==============================================================================================

  def findPaciente_Nac_1980_and_O_Post(self):
    # Consulta con AND: pacientes nacidos en 1980 y tipo de sangre "O+"
    return Paciente.objects.filter(fecha_nacimiento__year=1980, tipo_sangre__tipo="O+")

      #  CONSOLA SHELL PLUS >>>>>
      #  <QuerySet [<Paciente: Daniela>]>

      # SENTENCIA SQL <<<<<
      # SELECT "Orm_paciente"."id",
      #        "Orm_paciente"."nombres",
      #        "Orm_paciente"."apellidos",
      #        "Orm_paciente"."cedula",
      #        "Orm_paciente"."fecha_nacimiento",
      #        "Orm_paciente"."telefono",
      #        "Orm_paciente"."email",
      #        "Orm_paciente"."sexo",
      #        "Orm_paciente"."estado_civil",
      #        "Orm_paciente"."direccion",
      #        "Orm_paciente"."latitud",
      #        "Orm_paciente"."longitud",
      #        "Orm_paciente"."tipo_sangre_id",
      #        "Orm_paciente"."alergias",
      #        "Orm_paciente"."enfermedades_cronicas",
      #        "Orm_paciente"."medicacion_actual",
      #        "Orm_paciente"."cirugias_previas",
      #        "Orm_paciente"."antecedentes_personales",
      #        "Orm_paciente"."antecedentes_familiares"
      #   FROM "Orm_paciente"
      #  INNER JOIN "Orm_tiposangre"
      #     ON ("Orm_paciente"."tipo_sangre_id" = "Orm_tiposangre"."id")
      #  WHERE ("Orm_paciente"."fecha_nacimiento" BETWEEN '1980-01-01'::date AND '1980-12-31'::date AND "Orm_tiposangre"."tipo" = 'O+')
      #  ORDER BY "Orm_paciente"."apellidos" ASC
      #  LIMIT 21

# ==============================================================================================

  def findPaciente_or_1980_O_Post(self):
    # Consulta con OR: pacientes nacidos en 1980 o con tipo de sangre "O+"
    return Paciente.objects.filter(Q(fecha_nacimiento__year=1980) | Q(tipo_sangre__tipo="O+"))

      #  CONSOLA SHELL PLUS >>>>>
      # <QuerySet [<Paciente: Marta>, <Paciente: Daniela>]>

      # SENTENCIA SQL <<<<<
      # SELECT "Orm_paciente"."id",
      #        "Orm_paciente"."nombres",
      #        "Orm_paciente"."apellidos",
      #        "Orm_paciente"."cedula",
      #        "Orm_paciente"."fecha_nacimiento",
      #        "Orm_paciente"."telefono",
      #        "Orm_paciente"."email",
      #        "Orm_paciente"."sexo",
      #        "Orm_paciente"."estado_civil",
      #        "Orm_paciente"."direccion",
      #        "Orm_paciente"."latitud",
      #        "Orm_paciente"."longitud",
      #        "Orm_paciente"."tipo_sangre_id",
      #        "Orm_paciente"."alergias",
      #        "Orm_paciente"."enfermedades_cronicas",
      #        "Orm_paciente"."medicacion_actual",
      #        "Orm_paciente"."cirugias_previas",
      #        "Orm_paciente"."antecedentes_personales",
      #        "Orm_paciente"."antecedentes_familiares"
      #   FROM "Orm_paciente"
      #   LEFT OUTER JOIN "Orm_tiposangre"
      #     ON ("Orm_paciente"."tipo_sangre_id" = "Orm_tiposangre"."id")
      #  WHERE ("Orm_paciente"."fecha_nacimiento" BETWEEN '1980-01-01'::date AND '1980-12-31'::date OR "Orm_tiposangre"."tipo" = 'O+')
      #  ORDER BY "Orm_paciente"."apellidos" ASC
      #  LIMIT 21

# ==============================================================================================

  def findPaciente_1980_or_O_Post_sin_alergias(self):
    # Filtrar pacientes nacidos en 1980 o con tipo de sangre "O+" y sin alergias
    return Paciente.objects.filter(Q(fecha_nacimiento__year=1980) | Q(tipo_sangre__tipo="O+"), alergias="Ninguna")

      #  CONSOLA SHELL PLUS >>>>>
      # <QuerySet [<Paciente: Marta>, <Paciente: Daniela>]>

      # SENTENCIA SQL <<<<<
      # SELECT "Orm_paciente"."id",
      #        "Orm_paciente"."nombres",
      #        "Orm_paciente"."apellidos",
      #        "Orm_paciente"."cedula",
      #        "Orm_paciente"."fecha_nacimiento",
      #        "Orm_paciente"."telefono",
      #        "Orm_paciente"."email",
      #        "Orm_paciente"."sexo",
      #        "Orm_paciente"."estado_civil",
      #        "Orm_paciente"."direccion",
      #        "Orm_paciente"."latitud",
      #        "Orm_paciente"."longitud",
      #        "Orm_paciente"."tipo_sangre_id",
      #        "Orm_paciente"."alergias",
      #        "Orm_paciente"."enfermedades_cronicas",
      #        "Orm_paciente"."medicacion_actual",
      #        "Orm_paciente"."cirugias_previas",
      #        "Orm_paciente"."antecedentes_personales",
      #        "Orm_paciente"."antecedentes_familiares"
      #   FROM "Orm_paciente"
      #   LEFT OUTER JOIN "Orm_tiposangre"
      #     ON ("Orm_paciente"."tipo_sangre_id" = "Orm_tiposangre"."id")
      #  WHERE (("Orm_paciente"."fecha_nacimiento" BETWEEN '1980-01-01'::date AND '
      # 1980-12-31'::date OR "Orm_tiposangre"."tipo" = 'O+') AND "Orm_paciente"."alergias" = 'Ninguna')
      #  ORDER BY "Orm_paciente"."apellidos" ASC
      #  LIMIT 21

# ==============================================================================================

  def findPaciente_excluir_O_Post(self):
    # Excluir pacientes con tipo de sangre "O+" y mostrar apellidos y descripción
    return Paciente.objects.exclude(tipo_sangre__tipo="O+").values('apellidos', 'tipo_sangre__descripcion')

      #  CONSOLA SHELL PLUS >>>>>
      # <QuerySet [{'apellidos': 'Gómez', 'tipo_sangre__descripcion': 'Tipo A negat
      # ivo'}, {'apellidos': 'Vera', 'tipo_sangre__descripcion': 'Tipo X positivo'}]>

      # SENTENCIA SQL <<<<<
      # SELECT "Orm_paciente"."apellidos",
      #        "Orm_tiposangre"."descripcion"
      #   FROM "Orm_paciente"
      #   LEFT OUTER JOIN "Orm_tiposangre"
      #     ON ("Orm_paciente"."tipo_sangre_id" = "Orm_tiposangre"."id")
      #  WHERE NOT ("Orm_tiposangre"."tipo" = 'O+' AND "Orm_tiposangre"."tipo" IS NOT NULL)
      #  ORDER BY "Orm_paciente"."apellidos" ASC
      #  LIMIT 21

# ==============================================================================================

  def findPaciente_nacidos_post_1980_excluir_O_Post(self):
    # Obtener pacientes nacidos después de 1980 excluyendo tipo de sangre "O+"
    return Paciente.objects.filter(fecha_nacimiento__year__gt=1980).exclude(tipo_sangre__tipo="O+").values('apellidos', 'tipo_sangre__descripcion')

      #  CONSOLA SHELL PLUS >>>>>
      # <QuerySet [{'apellidos': 'Gómez', 'tipo_sangre__descripcion': 'Tipo A negat
      # ivo'}, {'apellidos': 'Vera', 'tipo_sangre__descripcion': 'Tipo X positivo'}]>

      # SENTENCIA SQL <<<<<
      # SELECT "Orm_paciente"."apellidos",
      #        "Orm_tiposangre"."descripcion"
      #   FROM "Orm_paciente"
      #   LEFT OUTER JOIN "Orm_tiposangre"
      #     ON ("Orm_paciente"."tipo_sangre_id" = "Orm_tiposangre"."id")
      #  WHERE ("Orm_paciente"."fecha_nacimiento" > '1980-12-31'::date AND NOT ("Orm_tiposangre"."tipo" = 'O+' AND "Orm_tiposangre"."tipo" IS NOT NULL))
      #  ORDER BY "Orm_paciente"."apellidos" ASC
      #  LIMIT 21

# ==============================================================================================

  # <<<<< ORM MODELO CARGO >>>>>
  def createCargo(self):
    # Insertar un registro directamente en la base de datos
    Cargo.objects.create(nombre="Enfermera", descripcion="Su Rol es atender a los pacientes")

    #  CONSOLA SHELL PLUS >>>>>

    # SENTENCIA SQL <<<<<
    # INSERT INTO "Orm_cargo" ("nombre", "descripcion")
    # VALUES ('Enfermera', 'Su Rol es atender a los pacientes') RETURNING "Orm_cargo"."id"

# ==============================================================================================

  def bulk_createCargo(self):
    # Crear una lista de instancias de TipoSangre con varios tipos de sangre
    tipos_cargos = [
      Cargo(nombre="Limpieza", descripcion="Su Rol es tener limpio las salas"),
      Cargo(nombre="Bodeguero", descripcion="Su Rol es mantener la contabilidad de los productos"),
      Cargo(nombre="Secretario", descripcion="Su Rol es llevar acabo la gestion del Doctor"),
    ]

    # Insertar múltiples registros en la base de datos de una sola vez
    Cargo.objects.bulk_create(tipos_cargos)

    #  CONSOLA SHELL PLUS >>>>>

    # SENTENCIA SQL <<<<<
    # INSERT INTO "Orm_cargo" ("nombre", "descripcion")
    # VALUES ('Limpieza', 'Su Rol es tener limpio las salas'), ('Bodeguero', 'Su
    # Rol es mantener la contabilidad de los productos'), ('Secretario', 'Su Rol es llevar acabo la gestion del Doctor') RETURNING "Orm_cargo"."id"

# ==============================================================================================

  def obtener_cargo_por_id(self):
    # Obtener cargo con id 1 (ej. Enfermera)
    return Cargo.objects.get(id=1)

    #  CONSOLA SHELL PLUS >>>>>
    # Out[4]: <Cargo: Enfermera>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_cargo"."id",
    #        "Orm_cargo"."nombre",
    #        "Orm_cargo"."descripcion"
    #   FROM "Orm_cargo"
    #  WHERE "Orm_cargo"."id" = 1
    #  LIMIT 21

# ==============================================================================================

  # <<<<< ORM MODELO EMPLEADOS >>>>>
  def createEmpleados(self):
    # Crear y guardar empleados en la base de datos
    cargo_1 = Cargo.objects.get(id=1)
    cargo_2 = Cargo.objects.get(id=2)

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
      cargo=cargo_2,
      sueldo=1800.00,
      direccion="Calle 2, Ciudad",
      latitud=-0.654321,
      longitud=-78.654321,
    )
    empleado2.save()

    #  CONSOLA SHELL PLUS >>>>>

    # SENTENCIA SQL <<<<<
    # INSERT INTO "Orm_empleado" ("nombres", "apellidos", "cedula", "fecha_nacimiento", "cargo_id", "sueldo", "direccion", "latitud", "longitud", "foto")
    # VALUES ('Juan', 'Pérez', '1234567890', '1990-01-01'::date, 1, 1500, 'Calle 1, Ciudad', -0.123456, -78.123456, '') RETURNING "Orm_empleado"."id"
    #
    # INSERT INTO "Orm_empleado" ("nombres", "apellidos", "cedula", "fecha_nacimiento", "cargo_id", "sueldo", "direccion", "latitud", "longitud", "foto")
    # VALUES ('María', 'Gómez', '0987654321', '1985-05-15'::date, 2, 1800, 'Calle 2, Ciudad', -0.654321, -78.654321, '') RETURNING "Orm_empleado"."id"

# ==============================================================================================

  def printEmpleados(self):
    # Consultar todos los empleados y mostrar sus nombres, apellidos y cargos
    empleados = Empleado.objects.all()
    for empleado in empleados:
      print(f"{empleado.nombres} {empleado.apellidos} - Cargo: {empleado.cargo.descripcion}")

      #  CONSOLA SHELL PLUS >>>>>
      # Execution time: 0.001529s [Database: default]
      # Juan Pérez - Cargo: Su Rol es atender a los pacientes

      # Execution time: 0.000000s [Database: default]
      # María Gómez - Cargo: Su Rol es tener limpio las salas

      # SENTENCIA SQL <<<<<
      # SELECT "Orm_empleado"."id",
      #        "Orm_empleado"."nombres",
      #        "Orm_empleado"."apellidos",
      #        "Orm_empleado"."cedula",
      #        "Orm_empleado"."fecha_nacimiento",
      #        "Orm_empleado"."cargo_id",
      #        "Orm_empleado"."sueldo",
      #        "Orm_empleado"."direccion",
      #        "Orm_empleado"."latitud",
      #        "Orm_empleado"."longitud",
      #        "Orm_empleado"."foto"
      #   FROM "Orm_empleado"

# ==============================================================================================

    def obtener_nombres_y_sueldos_empleados(self):
      # Mostrar el nombre y el sueldo de todos los empleados
      return Empleado.objects.values('nombres', 'sueldo')
      #  CONSOLA SHELL PLUS >>>>>

      # SENTENCIA SQL <<<<<

# ==============================================================================================

  # <<<<< ORM MODELO PACIENTE && TIPO SANGRE >>>>>
  def counterPaciente_TipSangre(self):
    # Calcular el número de pacientes por tipo de sangre
    pacientes_por_tipo_sangre = Paciente.objects.values('tipo_sangre__tipo').annotate(total=Count('tipo_sangre'))
    for registro in pacientes_por_tipo_sangre:
      print(f"Tipo de Sangre: {registro['tipo_sangre__tipo']}, Total: {registro['total']}")

      #  CONSOLA SHELL PLUS >>>>>
      # Tipo de Sangre: X+, Total: 1
      # Tipo de Sangre: A-, Total: 1
      # Tipo de Sangre: O+, Total: 2

      # SENTENCIA SQL <<<<<
      # SELECT "Orm_tiposangre"."tipo",
      #        COUNT("Orm_paciente"."tipo_sangre_id") AS "total"
      #   FROM "Orm_paciente"
      #   LEFT OUTER JOIN "Orm_tiposangre"
      #     ON ("Orm_paciente"."tipo_sangre_id" = "Orm_tiposangre"."id")
      #  GROUP BY "Orm_tiposangre"."tipo"

# ==============================================================================================

  def obtener_aggregados_enfermeras(self):
    # Consulta de agregados para empleados con cargo "Enfermera"
    return Empleado.objects.filter(cargo__nombre__icontains="Enfermera").aggregate(
      total_sueldo=Sum('sueldo'),
      promedio_sueldo=Avg('sueldo'),
      max_sueldo=Max('sueldo'),
      min_sueldo=Min('sueldo'),
      cantidad_enfermeras=Count('id')
    )

    #  CONSOLA SHELL PLUS >>>>>
    # Out[2]:
    # {'total_sueldo': Decimal('1500.00'),
    #  'promedio_sueldo': Decimal('1500.0000000000000000'),
    #  'max_sueldo': Decimal('1500.00'),
    #  'min_sueldo': Decimal('1500.00'),
    #  'cantidad_enfermeras': 1}

    # SENTENCIA SQL <<<<<
    # SELECT SUM("Orm_empleado"."sueldo") AS "total_sueldo",
    #        AVG("Orm_empleado"."sueldo") AS "promedio_sueldo",
    #        MAX("Orm_empleado"."sueldo") AS "max_sueldo",
    #        MIN("Orm_empleado"."sueldo") AS "min_sueldo",
    #        COUNT("Orm_empleado"."id") AS "cantidad_enfermeras"
    #   FROM "Orm_empleado"
    #  INNER JOIN "Orm_cargo"
    #     ON ("Orm_empleado"."cargo_id" = "Orm_cargo"."id")
    #  WHERE UPPER("

# ==============================================================================================

  def obtener_aggregados_cargo(self):
    # Consulta de agregados agrupados por cargo
    return Empleado.objects.values('cargo__nombre').annotate(
      total_sueldo=Sum('sueldo'),
      promedio_sueldo=Avg('sueldo'),
      max_sueldo=Max('sueldo'),
      min_sueldo=Min('sueldo'),
      cantidad_empleados=Count('id')
    )

    #  CONSOLA SHELL PLUS >>>>>
    # <QuerySet [{'cargo__nombre': 'Limpieza', 'total_sueldo': Decimal('1800.00')
    # , 'promedio_sueldo': Decimal('1800.0000000000000000'), 'max_sueldo': Decima
    # l('1800.00'), 'min_sueldo': Decimal('1800.00'), 'cantidad_empleados': 1}, {
    # 'cargo__nombre': 'Enfermera', 'total_sueldo': Decimal('1500.00'), 'promedio
    # _sueldo': Decimal('1500.0000000000000000'), 'max_sueldo': Decimal('1500.00'), 'min_sueldo': Decimal('1500.00'), 'cantidad_empleados': 1}]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_cargo"."nombre",
    #        SUM("Orm_empleado"."sueldo") AS "total_sueldo",
    #        AVG("Orm_empleado"."sueldo") AS "promedio_sueldo",
    #        MAX("Orm_empleado"."sueldo") AS "max_sueldo",
    #        MIN("Orm_empleado"."sueldo") AS "min_sueldo",
    #        COUNT("Orm_empleado"."id") AS "cantidad_empleados"
    #   FROM "Orm_empleado"
    #  INNER JOIN "Orm_cargo"
    #     ON ("Orm_empleado"."cargo_id" = "Orm_cargo"."id")
    #  GROUP BY "Orm_cargo"."nombre"
    #  LIMIT 21

# ==============================================================================================

  def obtener_aggregados_cargo_sueldo(self):
    # Consulta de agregados agrupados por cargo y sueldo
    return Empleado.objects.values('cargo__nombre', 'sueldo').annotate(
      cantidad_empleados=Count('id')
    ).order_by('cargo__nombre', 'sueldo')

    #  CONSOLA SHELL PLUS >>>>>
    # <QuerySet [{'cargo__nombre': 'Enfermera', 'sueldo': Decimal('1500.00'), 'ca
    # ntidad_empleados': 1}, {'cargo__nombre': 'Limpieza', 'sueldo': Decimal('1800.00'), 'cantidad_empleados': 1}]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_cargo"."nombre",
    #        "Orm_empleado"."sueldo",
    #        COUNT("Orm_empleado"."id") AS "cantidad_empleados"
    #   FROM "Orm_empleado"
    #  INNER JOIN "Orm_cargo"
    #     ON ("Orm_empleado"."cargo_id" = "Orm_cargo"."id")
    #  GROUP BY "Orm_cargo"."nombre",
    #           "Orm_empleado"."sueldo"
    #  ORDER BY "Orm_cargo"."nombre" ASC,
    #           "Orm_empleado"."sueldo" ASC
    #  LIMIT 21

# ==============================================================================================

  def obtener_empleados_alias_cargo(self):
    # Consulta de empleados con el nombre del cargo como alias
    return Empleado.objects.annotate(cargo_descripcion=F('cargo__nombre'))

    #  CONSOLA SHELL PLUS >>>>>
    # <QuerySet [<Empleado: Pérez>, <Empleado: Gómez>]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_empleado"."id",
    #        "Orm_empleado"."nombres",
    #        "Orm_empleado"."apellidos",
    #        "Orm_empleado"."cedula",
    #        "Orm_empleado"."fecha_nacimiento",
    #        "Orm_empleado"."cargo_id",
    #        "Orm_empleado"."sueldo",
    #        "Orm_empleado"."direccion",
    #        "Orm_empleado"."latitud",
    #        "Orm_empleado"."longitud",
    #        "Orm_empleado"."foto",
    #        "Orm_cargo"."nombre" AS "cargo_descripcion"
    #   FROM "Orm_empleado"
    #  INNER JOIN "Orm_cargo"
    #     ON ("Orm_empleado"."cargo_id" = "Orm_cargo"."id")
    #  LIMIT 21

# ==============================================================================================

  def actualizar_sueldos_enfermeras(self):
    # Actualizar los sueldos en un 10% para empleados cuyo cargo sea "Enfermera"
    Empleado.objects.filter(cargo__nombre="Enfermera").update(sueldo=F('sueldo') * 1.10, direccion='Guayaquil')

    #  CONSOLA SHELL PLUS >>>>>

    # SENTENCIA SQL <<<<<
    # UPDATE "Orm_empleado"
    #    SET "sueldo" = ("Orm_empleado"."sueldo" * 1.1),
    #        "direccion" = 'Guayaquil'
    #  WHERE "Orm_empleado"."id" IN (
    #         SELECT U0."id"
    #           FROM "Orm_empleado" U0
    #          INNER JOIN "Orm_cargo" U1
    #             ON (U0."cargo_id" = U1."id")
    #          WHERE U1."nombre" = 'Enfermera'
    #        )

# ==============================================================================================

  def actualizar_cargo_descripcion(self):
    # Actualizar la descripción del cargo con id 3
    cargo = Cargo.objects.get(id=3)
    cargo.nombre = "Doctora"
    cargo.descripcion = "Su Rol es de gestionar Enfermeros y atender pacientes"
    cargo.save()

    #  CONSOLA SHELL PLUS >>>>>

    # SENTENCIA SQL <<<<<
    # UPDATE "Orm_cargo"
    #    SET "nombre" = 'Doctora',
    #        "descripcion" = 'Su Rol es de gestionar Enfermeros y atender pacientes'
    #  WHERE "Orm_cargo"."id" = 3

# ==============================================================================================

  # <<<<< MODEL TIPO SANGRE >>>>>
  def eliminar_tipos_sangre_positivo(self):
    # Eliminar los tipos de sangre cuya descripción contenga "positivo"
    return TipoSangre.objects.filter(descripcion__iendswith="positivo").delete()

    #  CONSOLA SHELL PLUS >>>>>
    # Out[4]: (4, {'Orm.TipoSangre': 4})

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_tiposangre"."id",
    #        "Orm_tiposangre"."tipo",
    #        "Orm_tiposangre"."descripcion"
    #   FROM "Orm_tiposangre"
    #  WHERE UPPER("Orm_tiposangre"."descripcion"::text) LIKE UPPER('%positivo')

# ==============================================================================================

  # <<<<< MODELO CARGO >>>>>
  def eliminar_cargo(self):
    # Eliminar el cargo con id 3
    cargo = Cargo.objects.get(id=3)
    cargo.delete()

    #  CONSOLA SHELL PLUS >>>>>
    # ProtectedError: ("Cannot delete some instances of model 'Cargo' because the
    # y are referenced through protected foreign keys: 'Empleado.cargo'.", {<Empleado: Quinteros>})

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_empleado"."id",
    #        "Orm_empleado"."nombres",
    #        "Orm_empleado"."apellidos",
    #        "Orm_empleado"."cedula",
    #        "Orm_empleado"."fecha_nacimiento",
    #        "Orm_empleado"."cargo_id",
    #        "Orm_empleado"."sueldo",
    #        "Orm_empleado"."direccion",
    #        "Orm_empleado"."latitud",
    #        "Orm_empleado"."longitud",
    #        "Orm_empleado"."foto"
    #   FROM "Orm_empleado"
    #  WHERE "Orm_empleado"."cargo_id" IN (3)

# ==============================================================================================
