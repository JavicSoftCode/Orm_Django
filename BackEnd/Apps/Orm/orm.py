from django.db.models import F
from django.db.models import Q
from django.db.models import Sum, Avg, Max, Min, Count
from django.db import connection
from BackEnd.Apps.Orm.models import *


# from BackEnd.Apps.Orm.orm import Orm
# orm_instance = Orm()

# Comandos
# python manage.py shell
# python manage.py shell_plus --print-sql      USAR ESTE DE AQUI


# Practica JavicSoftCode
class Orm:
  def createTipoSangre(self):
    try:
        # Crea el registro y obtiene la última consulta SQL si fue exitoso
        tipoSangre = TipoSangre.objects.create(tipo="P+", descripcion="Tipo P positivo")
        last_query = connection.queries[-1]['sql'] if tipoSangre else None

        # Imprime la consulta SQL o un mensaje de error si no se creó el registro
        print(f"Consulta SQL ejecutada: {last_query}" if last_query else "Hubo un error al crear el registro")

    except Exception as e:
        # Maneja errores
        print(f'Error: {str(e)}')

  def saveTipoSangre(self):
    try:
      # Crea la instancia y guarda el registro en la base de datos
      tipoSangre = TipoSangre(tipo="J-", descripcion="Tipo J negativo")
      tipoSangre.save()

      # Si se guardó correctamente, extrae la última consulta SQL
      last_query = connection.queries[-1]['sql']
      print(f"Consulta SQL ejecutada:\n{last_query}")

    except Exception as e:
      # Maneja errores
      print(f'Error: {str(e)}')

  def bulk_createTiposSangre(self):
    try:
        # Crear una lista de instancias de TipoSangre
        tipos_sangre = [
            TipoSangre(tipo="V+", descripcion="Tipo V positivo"),
            TipoSangre(tipo="X-", descripcion="Tipo X negativo"),
        ]

        # Construir la sentencia SQL de inserción manualmente
        values = ', '.join([f"('{tipo.tipo}', '{tipo.descripcion}')" for tipo in tipos_sangre])
        formatted_query = f"INSERT INTO \"Orm_tiposangre\" (\"tipo\", \"descripcion\") VALUES {values};"

        # Insertar múltiples registros en la base de datos
        TipoSangre.objects.bulk_create(tipos_sangre)

        # Imprimir la consulta SQL construida manualmente
        print(f"Consulta SQL ejecutada:\n{formatted_query}")

    except Exception as e:
        # Manejar errores
        print(f'Error: {str(e)}')

  def allTiposSangre(self):
    # Obtener todos los registros de TipoSangre
    tipos_sangre = TipoSangre.objects.all()

    # Usar una comprensión de listas para crear una representación formateada
    tipos_sangre_info = [f"Tipo: {tipo.tipo}, Descripción: {tipo.descripcion}" for tipo in tipos_sangre]

    # Imprimir cada tipo de sangre en una línea
    print("\n".join(tipos_sangre_info))

    # Imprimir la última consulta SQL ejecutada
    if connection.queries:
      last_query = connection.queries[-1]['sql']
      print(f"\nConsulta SQL ejecutada:\n{last_query}")

  def findTiposSangre(self):
    # Definir los tipos de sangre a buscar
    tipo_O_pos = "O+"
    tipo_A = "A+"
    tipo_ab_pos = "AB+"

    # Lista de tipos de sangre que deseas buscar
    tipos = [tipo_O_pos, tipo_A, tipo_ab_pos]

    # Seleccionamos el tipo de sangre que quieres buscar (por ejemplo, A+)
    tipo_a_buscar = tipos[2]  # Puedes cambiar el índice para seleccionar otro tipo

    try:
      # Intentar obtener el registro por tipo de sangre
      tipo_sangre = TipoSangre.objects.get(tipo=tipo_a_buscar)
      # Si existe, muestra la información
      print(f"Tipo: {tipo_sangre.tipo}, Descripción: {tipo_sangre.descripcion}")

    except TipoSangre.DoesNotExist:
      # Si no existe, muestra el mensaje personalizado
      print(f"No existe el tipo de sangre: {tipo_a_buscar}")

    finally:
      # Siempre imprime la última consulta SQL, exista o no el registro
      if connection.queries:
        last_query = connection.queries[-1]['sql']
        print(f"\nConsulta SQL ejecutada para '{tipo_a_buscar}':\n{last_query}")



# # Practica Julissa
# # Insertar un registro directamente en la base de datos
# tipo1 = TipoSangre.objects.create(tipo="X+", descripcion="Tipo X positivo")
#
# # Terminal Shell Plus >>>>>
# # In [1]: tipo1 = TipoSangre.objects.create(tipo="X+", descripcion="Tipo X positivo")
#
# # CONSULTA SQL <<<<<
# # INSERT INTO "Orm_tiposangre" ("tipo", "descripcion")
# # VALUES ('X+', 'Tipo X positivo') RETURNING "Orm_tiposangre"."id"
#
# # =========================================================================================
#
# # Crear el registro en memoria (sin guardarlo aún en la base de datos)
# tipo2 = TipoSangre(tipo="V-", descripcion="Tipo V negativo")
# # Guardar el registro en la base de datos
# tipo2.save()
#
# # Terminal Shell Plus >>>>>
# # In [2]: tipo2 = TipoSangre(tipo="V-", descripcion="Tipo V negativo")
# #   ...: tipo2.save()
#
# # CONSULTA SQL <<<<<
# # INSERT INTO "Orm_tiposangre" ("tipo", "descripcion")
# # VALUES ('V-', 'Tipo V negativo') RETURNING "Orm_tiposangre"."id"
