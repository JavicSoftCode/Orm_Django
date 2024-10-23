from django.db.models import F
from django.db.models import Q
from django.db.models import Sum, Avg, Max, Min, Count
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

  def saveTipoSangre(self):
    pass

  def bulk_createTiposSangre(self):
    pass

  def allTiposSangre(self):
    pass

  def findTiposSangre(self):
    pass


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
