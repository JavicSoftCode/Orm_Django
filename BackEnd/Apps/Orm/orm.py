from django.db.models import F
from django.db.models import Q
from django.db.models import Sum, Avg, Max, Min, Count
from BackEnd.Apps.Orm.models import *


# Comandos 
# python manage.py shell
# python manage.py shell_plus --print-sql      USAR ESTE DE AQUI


# Practica Julissa
# Insertar un registro directamente en la base de datos
tipo1 = TipoSangre.objects.create(tipo="X+", descripcion="Tipo X positivo")

# Terminal Shell Plus >>>>>
# In [1]: tipo1 = TipoSangre.objects.create(tipo="X+", descripcion="Tipo X positivo") 

# CONSULTA SQL <<<<<
# INSERT INTO "Orm_tiposangre" ("tipo", "descripcion")
# VALUES ('X+', 'Tipo X positivo') RETURNING "Orm_tiposangre"."id"

# =========================================================================================

# Crear el registro en memoria (sin guardarlo aún en la base de datos)
tipo2 = TipoSangre(tipo="V-", descripcion="Tipo V negativo")
# Guardar el registro en la base de datos
tipo2.save()

# Terminal Shell Plus >>>>>
# In [2]: tipo2 = TipoSangre(tipo="V-", descripcion="Tipo V negativo")
#   ...: tipo2.save()

# CONSULTA SQL <<<<<
# INSERT INTO "Orm_tiposangre" ("tipo", "descripcion")
# VALUES ('V-', 'Tipo V negativo') RETURNING "Orm_tiposangre"."id"