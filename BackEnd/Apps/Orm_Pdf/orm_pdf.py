from django.db.models import Min, Max, Avg, Sum, Count  # Funciones de agregación

from BackEnd.Apps.Orm_Pdf.models import *  # Importar modelos base


# Comando python manage.py shell_plus --print-sql
# %load_ext autoreload
# %autoreload 2

# from BackEnd.Apps.Orm_Pdf.orm_pdf import Orm_Pdf
# ormPdf_instance = Orm_Pdf()

#  CONSOLA SHELL PLUS >>>>>

# SENTENCIA SQL <<<<<


# ==============================================================================================


class Orm_Pdf:

  def createAutor(self):
    # Inserción básica
    return Autor.objects.create(nombre="Autor desde el ORM")

    #  CONSOLA SHELL PLUS >>>>>
    # In [4]: ormPdf_instance.createAutor()
    # Out[4]: <Autor: Autor object (1)>

    # SENTENCIA SQL <<<<<
    # INSERT INTO "Orm_Pdf_autor" ("nombre")
    # VALUES ('Autor desde el ORM') RETURNING "Orm_Pdf_autor"."id"

  # ==============================================================================================

  def bulk_createAutor(self):
    # Inserción masiva
    return Autor.objects.bulk_create([
      Autor(nombre="Autor 1M"),
      Autor(nombre="Autor 2M"),
      Autor(nombre="Autor 3M")
    ])

    #  CONSOLA SHELL PLUS >>>>>
    # In [6]: ormPdf_instance.bulk_createAutor()
    # Out[6]: [<Autor: Autor object (5)>,
    #  <Autor: Autor object (6)>,
    #  <Autor: Autor object (7)>]

    # SENTENCIA SQL <<<<<
    # INSERT INTO "Orm_Pdf_autor" ("nombre")
    # VALUES ('Autor 1M'), ('Autor 2M'), ('Autor 3M') RETURNING "Orm_Pdf_autor"."id"

  # ==============================================================================================

  def all_Autor(self):
    # Consultar todos los registros
    return Autor.objects.all()

    #  CONSOLA SHELL PLUS >>>>>
    # In [7]: ormPdf_instance.all_Autor()
    # Out[7]: <QuerySet [<Autor: Autor object (1)>,
    # <Autor: Autor object (2)>,
    # <Autor: Autor object (3)>,
    # <Autor: Autor object (4)>,
    # <Autor: Autor object (5)>,
    # <Autor: Autor object (6)>,
    # <Autor: Autor object (7)>]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_autor"."id",
    #  "Orm_Pdf_autor"."nombre"
    #  FROM "Orm_Pdf_autor"
    # LIMIT 21

  # ==============================================================================================

  def create_Libro(self):
    # Obtén la instancia de Editorial con ID 1
    editorial_instance = Editorial.objects.get(id=1)

    # Crea el libro utilizando la instancia de Editorial
    return Libro.objects.create(
      isbn="1234567898745",
      titulo="Pinocho",
      paginas=10,
      fecha_publicacion="2024-10-27",
      imagen="",
      desc_corta="Aventuras con Pinocho",
      estatus="A",
      categoria="Cuentos",
      editorial=editorial_instance,
      edicion_anterior=None
    )

    #  CONSOLA SHELL PLUS >>>>>
    # In [8]: ormPdf_instance.create_Libro()
    # Out[8]: <Libro: Libro object (1234567898745)>

    # SENTENCIA SQL <<<<<
    # SELECT "libreria_editorial"."id",
    #                 "libreria_editorial"."nombre"
    #   FROM "libreria_editorial"
    #  WHERE "libreria_editorial"."id" = 1
    #  LIMIT 21
    #
    # INSERT INTO "Orm_Pdf_libro" ("isbn", "titulo", "paginas", "fecha_publicacion", "imagen", "desc_corta", "estatus", "categoria", "editorial_id", "edicion_anterior_id")
    # VALUES ('1234567898745', 'Pinocho', 10, '2024-10-27'::date, '', 'Aventuras con Pinocho', 'A', 'Cuentos', 1, NULL)

  # ==============================================================================================

  def bulk_createLibros(self):
    # Obtén la instancia de Editorial con ID 1
    editorial_instance = Editorial.objects.get(id=1)

    # Crea una lista de instancias de Libro
    libros = [
      Libro(
        isbn="2325236589898",
        titulo="Pinocho",
        paginas=10,
        fecha_publicacion="2024-10-27",
        imagen="",
        desc_corta="Aventuras con Pinocho",
        estatus="A",
        categoria="Cuentos",
        editorial=editorial_instance,
        edicion_anterior=None
      ),
      Libro(
        isbn="1234567898746",
        titulo="Cenicienta",
        paginas=8,
        fecha_publicacion="2024-10-27",
        imagen="",
        desc_corta="La historia de Cenicienta",
        estatus="A",
        categoria="Cuentos",
        editorial=editorial_instance,
        edicion_anterior=None
      ),
      Libro(
        isbn="1234567898747",
        titulo="La Bella Durmiente",
        paginas=12,
        fecha_publicacion="2024-10-27",
        imagen="",
        desc_corta="La Bella Durmiente y su sueño eterno",
        estatus="A",
        categoria="Cuentos",
        editorial=editorial_instance,
        edicion_anterior=None
      )
    ]

    return Libro.objects.bulk_create(libros)

    # CONSOLA SHELL PLUS >>>>>
    # In [13]: ormPdf_instance.bulk_createLibros()
    # Out[13]:
    # [<Libro: Libro object (2325236589898)>,
    #  <Libro: Libro object (1234567898746)>,
    #  <Libro: Libro object (1234567898747)>]

    # SENTENCIA SQL <<<<<
    # SELECT "libreria_editorial"."id",
    #        "libreria_editorial"."nombre"
    #   FROM "libreria_editorial"
    #  WHERE "libreria_editorial"."id" = 1
    #  LIMIT 21
    #
    # INSERT INTO "Orm_Pdf_libro" ("isbn", "titulo", "paginas", "fecha_publicacion", "imagen", "desc_corta", "estatus", "categoria", "editorial_id", "edicion_anterior_id")
    # VALUES ('2325236589898', 'Pinocho', 10, '2024-10-27'::date, '', 'Aventuras con Pinocho', 'A', 'Cuentos', 1,
    #  NULL), ('1234567898746', 'Cenicienta', 8, '2024-10-27'::date, '', 'La historia de Cenicienta', 'A', 'Cuent
    # os', 1, NULL), ('1234567898747', 'La Bella Durmiente', 12, '2024-10-27'::date, '', 'La Bella Durmiente y su sueño eterno', 'A', 'Cuentos', 1, NULL)

  # ==============================================================================================

  def all_Libro(self):
    # Consultar todos los registros
    return Libro.objects.all()

    #  CONSOLA SHELL PLUS >>>>>
    # In [14]: ormPdf_instance.all_Libro()
    # Out[14]:
    # <QuerySet [<Libro: Libro object (1234567898745)>,
    # <Libro: Libro object (2325236589898)>,
    # <Libro: Libro object (1234567898746)>,
    # <Libro: Libro object (1234567898747)>]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."titulo",
    #        "Orm_Pdf_libro"."paginas",
    #        "Orm_Pdf_libro"."fecha_publicacion",
    #        "Orm_Pdf_libro"."imagen",
    #        "Orm_Pdf_libro"."desc_corta",
    #        "Orm_Pdf_libro"."estatus",
    #        "Orm_Pdf_libro"."categoria",
    #        "Orm_Pdf_libro"."editorial_id",
    #        "Orm_Pdf_libro"."edicion_anterior_id"
    #   FROM "Orm_Pdf_libro"
    #  LIMIT 21

  # ==============================================================================================

  def get_objects(self):
    # Si conocemos la clave primaria del registro que estamos buscando podemos usar el método get.
    isbn = Libro.objects.get(isbn='1234567898746')

    pk = Libro.objects.get(pk='2325236589898')

    return isbn, pk

    #  CONSOLA SHELL PLUS >>>>>
    # In [18]: ormPdf_instance.get_objects()
    # Out[18]: (<Libro: Libro object (1234567898746)>, <Libro: Libro object (2325236589898)>)

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."titulo",
    #        "Orm_Pdf_libro"."paginas",
    #        "Orm_Pdf_libro"."fecha_publicacion",
    #        "Orm_Pdf_libro"."imagen",
    #        "Orm_Pdf_libro"."desc_corta",
    #        "Orm_Pdf_libro"."estatus",
    #        "Orm_Pdf_libro"."categoria",
    #        "Orm_Pdf_libro"."editorial_id",
    #        "Orm_Pdf_libro"."edicion_anterior_id"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."isbn" = '1234567898746'
    #  LIMIT 21
    #
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."titulo",
    #        "Orm_Pdf_libro"."paginas",
    #        "Orm_Pdf_libro"."fecha_publicacion",
    #        "Orm_Pdf_libro"."imagen",
    #        "Orm_Pdf_libro"."desc_corta",
    #        "Orm_Pdf_libro"."estatus",
    #        "Orm_Pdf_libro"."categoria",
    #        "Orm_Pdf_libro"."editorial_id",
    #        "Orm_Pdf_libro"."edicion_anterior_id"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."isbn" = '2325236589898'
    #  LIMIT 21

  # ==============================================================================================

  def funtion_models(self):
    # Ahora podemos usar nuestra función como parte del modelo
    return Libro.objects.buscar_por_isbn("1234567898747")

    #  CONSOLA SHELL PLUS >>>>>
    # In [4]: ormPdf_instance.funtion_models()
    # Out[4]: <Libro: Libro object (1234567898747)>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."titulo",
    #        "Orm_Pdf_libro"."paginas",
    #        "Orm_Pdf_libro"."fecha_publicacion",
    #        "Orm_Pdf_libro"."imagen",
    #        "Orm_Pdf_libro"."desc_corta",
    #        "Orm_Pdf_libro"."estatus",
    #        "Orm_Pdf_libro"."categoria",
    #        "Orm_Pdf_libro"."editorial_id",
    #        "Orm_Pdf_libro"."edicion_anterior_id"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."isbn" = '1234567898747'
    #  LIMIT 21

  # ==============================================================================================

  def first_resultLibro(self):
    # Obtener solo el primer resultado
    return Libro.objects.all().first()

    #  CONSOLA SHELL PLUS >>>>>
    # In [6]: ormPdf_instance.first_resultLibro()
    # Out[6]: <Libro: Libro object (1234567898745)>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."titulo",
    #        "Orm_Pdf_libro"."paginas",
    #        "Orm_Pdf_libro"."fecha_publicacion",
    #        "Orm_Pdf_libro"."imagen",
    #        "Orm_Pdf_libro"."desc_corta",
    #        "Orm_Pdf_libro"."estatus",
    #        "Orm_Pdf_libro"."categoria",
    #        "Orm_Pdf_libro"."editorial_id"
    #   FROM "Orm_Pdf_libro"
    #  ORDER BY "Orm_Pdf_libro"."isbn" ASC
    #  LIMIT 1

  # ==============================================================================================

  def ultimate_resultLibro(self):
    # Obtener solo el ultimo resultado
    return Libro.objects.all().last()

    #  CONSOLA SHELL PLUS >>>>>
    # In [17]: ormPdf_instance.ultimate_resultLibro()
    # Out[17]: <Libro: Libro object (2325236589898)>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."titulo",
    #        "Orm_Pdf_libro"."paginas",
    #        "Orm_Pdf_libro"."fecha_publicacion",
    #        "Orm_Pdf_libro"."imagen",
    #        "Orm_Pdf_libro"."desc_corta",
    #        "Orm_Pdf_libro"."estatus",
    #        "Orm_Pdf_libro"."categoria",
    #        "Orm_Pdf_libro"."editorial_id"
    #   FROM "Orm_Pdf_libro"
    #  ORDER BY "Orm_Pdf_libro"."isbn" DESC
    #  LIMIT 1

  # ==============================================================================================

  def rangue_firstLibro(self):
    # Ejemplo de obtener los primeros 5 libros
    return Libro.objects.all()[:3]

    #  CONSOLA SHELL PLUS >>>>>
    # In [18]: ormPdf_instance.rangue_firstLibro()
    # Out[18]: <QuerySet [<Libro: Libro object (1234567898745)>,
    # <Libro: Libro object (2325236589898)>,
    # <Libro: Libro object (1234567898746)>]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."titulo",
    #        "Orm_Pdf_libro"."paginas",
    #        "Orm_Pdf_libro"."fecha_publicacion",
    #        "Orm_Pdf_libro"."imagen",
    #        "Orm_Pdf_libro"."desc_corta",
    #        "Orm_Pdf_libro"."estatus",
    #        "Orm_Pdf_libro"."categoria",
    #        "Orm_Pdf_libro"."editorial_id"
    #   FROM "Orm_Pdf_libro"
    #  LIMIT 3

  # ==============================================================================================

  def find_first_isbn(self):
    # Ejempo de obtener los libros cuyo isbn comience con un 16
    return Libro.objects.filter(isbn__startswith="16")

    #  CONSOLA SHELL PLUS >>>>>
    # In [20]: ormPdf_instance.find_first_isbn()
    # Out[20]: <QuerySet [<Libro: Libro object (1659865985986)>]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."titulo",
    #        "Orm_Pdf_libro"."paginas",
    #        "Orm_Pdf_libro"."fecha_publicacion",
    #        "Orm_Pdf_libro"."imagen",
    #        "Orm_Pdf_libro"."desc_corta",
    #        "Orm_Pdf_libro"."estatus",
    #        "Orm_Pdf_libro"."categoria",
    #        "Orm_Pdf_libro"."editorial_id"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."isbn"::text LIKE '16%'
    #  LIMIT 21

  # ==============================================================================================

  def more_pagesLibro(self):
    # Ejemplo de los libros que tienen mas de 200 paginas
    return Libro.objects.filter(paginas__gt=200)

    #  CONSOLA SHELL PLUS >>>>>
    # In [21]: ormPdf_instance.more_pagesLibro()
    # Out[21]: <QuerySet [<Libro: Libro object (1234567898745)>,
    # <Libro: Libro object (1234567898746)>,
    # <Libro: Libro object (1234567898747)>]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."titulo",
    #        "Orm_Pdf_libro"."paginas",
    #        "Orm_Pdf_libro"."fecha_publicacion",
    #        "Orm_Pdf_libro"."imagen",
    #        "Orm_Pdf_libro"."editorial_id"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."paginas" > 200
    #  LIMIT 21

  # ==============================================================================================

  def more_pagesLibro_excludeISBN(self):
    # Ejemplo de libros que tienen mas de 200 paginas pero cuyo isbn no sea ninguno de estos dos
    # ('1234567898747','1659865985986')
    return Libro.objects.filter(paginas__gt=200).exclude(isbn__in=('1234567898747', '1659865985986'))

    #  CONSOLA SHELL PLUS >>>>>
    # In [22]: ormPdf_instance.more_pagesLibro_excludeISBN()
    # Out[22]: <QuerySet [<Libro: Libro object (1234567898745)>, <Libro: Libro object (1234567898746)>]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."titulo",
    #        "Orm_Pdf_libro"."paginas",
    #        "Orm_Pdf_libro"."fecha_publicacion",
    #        "Orm_Pdf_libro"."imagen",
    #        "Orm_Pdf_libro"."desc_corta",
    #        "Orm_Pdf_libro"."estatus",
    #        "Orm_Pdf_libro"."categoria",
    #        "Orm_Pdf_libro"."editorial_id"
    #   FROM "Orm_Pdf_libro"
    #  WHERE ("Orm_Pdf_libro"."paginas" > 200 AND NOT ("Orm_Pdf_libro"."isbn" IN ('1234567898747', '1659865985986')))
    #  LIMIT 21

  # ==============================================================================================

  def more_pagesLibro_or_more(self):
    # Ejemplo de libros que tiene 200 o mas paginas
    return Libro.objects.filter(paginas__gte=200)

    #  CONSOLA SHELL PLUS >>>>>
    # In [23]: ormPdf_instance.more_pagesLibro_or_more()
    # Out[23]: <QuerySet [<Libro: Libro object (1234567898745)>,
    # <Libro: Libro object (1234567898746)>,
    # <Libro: Libro object (1234567898747)>,
    # <Libro: Libro object (1659865985986)>]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."titulo",
    #        "Orm_Pdf_libro"."paginas",
    #        "Orm_Pdf_libro"."fecha_publicacion",
    #        "Orm_Pdf_libro"."imagen",
    #        "Orm_Pdf_libro"."desc_corta",
    #        "Orm_Pdf_libro"."estatus",
    #        "Orm_Pdf_libro"."categoria",
    #        "Orm_Pdf_libro"."editorial_id"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."paginas" >= 200
    #  LIMIT 21

  # ==============================================================================================

  def more_pagesLibro_includeCell(self):
    # Ejemplo de una consulta de los libros que tienen 200 o mas paginas, pero solo muestra las columnas isbn y paginas
    return Libro.objects.filter(paginas__gte=200).values('isbn', 'paginas')

    #  CONSOLA SHELL PLUS >>>>>
    # In [24]: ormPdf_instance.more_pagesLibro_includeCell()
    # Out[24]: <QuerySet [{'isbn': '1234567898745', 'paginas': 2000},
    # {'isbn': '1234567898746', 'paginas': 5000},
    # {'isbn': '1234567898747', 'paginas': 500},
    # {'isbn': '1659865985986', 'paginas': 200}]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."paginas"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."paginas" >= 200
    #  LIMIT 21

  # ==============================================================================================

  def lower_pagesLibro(self):
    # Ejemplo de los libros que tienen menos de 200 paginas
    return Libro.objects.filter(paginas__lt=200)

    #  CONSOLA SHELL PLUS >>>>>
    # In [25]: ormPdf_instance.lower_pagesLibro()
    # Out[25]: <QuerySet [<Libro: Libro object (2325236589898)>]>

    # SENTENCIA SQL <<<<<
    #  SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."titulo",
    #        "Orm_Pdf_libro"."paginas",
    #        "Orm_Pdf_libro"."fecha_publicacion",
    #        "Orm_Pdf_libro"."imagen",
    #        "Orm_Pdf_libro"."desc_corta",
    #        "Orm_Pdf_libro"."estatus",
    #        "Orm_Pdf_libro"."categoria",
    #        "Orm_Pdf_libro"."editorial_id"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."paginas" < 200
    #  LIMIT 21

  # ==============================================================================================

  def lower_pagesLibro_or_lower(self):
    # Ejemplo de libros que tienes 200 o menos paginas
    return Libro.objects.filter(paginas__lte=200)

    #  CONSOLA SHELL PLUS >>>>>
    # In [26]: ormPdf_instance.lower_pagesLibro_or_lower()
    # Out[26]: <QuerySet [<Libro: Libro object (2325236589898)>, <Libro: Libro object (1659865985986)>]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."titulo",
    #        "Orm_Pdf_libro"."paginas",
    #        "Orm_Pdf_libro"."fecha_publicacion",
    #        "Orm_Pdf_libro"."imagen",
    #        "Orm_Pdf_libro"."desc_corta",
    #        "Orm_Pdf_libro"."estatus",
    #        "Orm_Pdf_libro"."categoria",
    #        "Orm_Pdf_libro"."editorial_id"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."paginas" <= 200
    #  LIMIT 21

  # ==============================================================================================

  def counter_lowerPagesLibro(self):
    # Ejemplo de contar los libros que tienen menos de 200 paginas
    return Libro.objects.filter(paginas__lt=200).count()

    #  CONSOLA SHELL PLUS >>>>>
    # In [27]: ormPdf_instance.counter_lowerPagesLibro()
    # Out[27]: 1

    # SENTENCIA SQL <<<<<
    # SELECT COUNT(*) AS "__count"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."paginas" < 200

  # ==============================================================================================

  def consult_Libros_forPages(self):
    # Ejemplo de consulta de los libros con 200 paginas o con 100 paginas
    consulta1 = Libro.objects.filter(paginas=200)
    consulta2 = Libro.objects.filter(paginas=100)
    return (consulta1 | consulta2).values('isbn', 'paginas')

    #  CONSOLA SHELL PLUS >>>>>
    # In [28]: ormPdf_instance.consult_Libros_forPages()
    # Out[28]:  <QuerySet [{'isbn': '2325236589898', 'paginas': 100}, {'isbn': '1659865985986', 'paginas': 200}]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."paginas"
    #   FROM "Orm_Pdf_libro"
    #  WHERE ("Orm_Pdf_libro"."paginas" = 200 OR "Orm_Pdf_libro"."paginas" = 100)
    #  LIMIT 21

  # ==============================================================================================

  def consult_yearPublicLibro(self):
    # Ejemplo de una consulta que muestra los libros cuya fecha de publicación es 2012
    return Libro.objects.filter(fecha_publicacion__year=2012).values('isbn', 'fecha_publicacion')

    #  CONSOLA SHELL PLUS >>>>>
    # In [29]: ormPdf_instance.consult_yearPublicLibro()
    # Out[29]: <QuerySet [{'isbn': '1912458965698', 'fecha_publicacion': datetime.date(2012, 10, 28)}]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."fecha_publicacion"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."fecha_publicacion" BETWEEN '2012-01-01'::date AND '2012-12-31'::date
    #  LIMIT 21

  # ==============================================================================================

  def consult_Libro_first_followerDig(self):
    # Consultar los libros cuyo isbn comience con un 19 seguido de 8 digitos
    return Libro.objects.filter(isbn__regex=r'19\d{8}$').values('isbn')

    #  CONSOLA SHELL PLUS >>>>>
    # In [32]: ormPdf_instance.consult_Libro_first_followerDig()
    # Out[32]: <QuerySet []>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."isbn"::text ~ '19\d{8}$'
    #  LIMIT 21

  # ==============================================================================================

  def union_Editorial_and_Autor_names(self):
    # Unir en una sola consulta el nombre los Autores que contengan la palabra (depende lo que tenga el campo nombre) con las Editoriales cuyo nombre contenga
    # también la palabra (depende lo que tenga el campo nombre).
    a1 = Autor.objects.filter(nombre__contains='Autor 1M').values('nombre')
    e1 = Editorial.objects.filter(nombre__contains='Extra').values('nombre')
    return a1.union(e1)

    #  CONSOLA SHELL PLUS >>>>>
    # In [33]: ormPdf_instance.union_Editorial_and_Autor_names()
    # Out[33]: <QuerySet [{'nombre': 'Autor 1M'}, {'nombre': 'Extra'}]>

    # SENTENCIA SQL <<<<<
    #  (
    #         SELECT "Orm_Pdf_autor"."nombre" AS "col1"
    #           FROM "Orm_Pdf_autor"
    #          WHERE "Orm_Pdf_autor"."nombre"::text LIKE '%Autor 1M%'
    #        )
    #  UNION (
    #         SELECT "libreria_editorial"."nombre" AS "col1"
    #           FROM "libreria_editorial"
    #          WHERE "libreria_editorial"."nombre"::text LIKE '%Extra%'
    #        )
    #  LIMIT 21

  # ==============================================================================================

  def Libro_morePages_Position(self):
    # Obtener el cuarto libro con mas paginas
    return Libro.objects.values('isbn', 'paginas').order_by('-paginas')[3]

    #  CONSOLA SHELL PLUS >>>>>
    # In [34]: ormPdf_instance.Libro_morePages_Position()
    # Out[34]: {'isbn': '1912458965698', 'paginas': 300}

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."paginas"
    #   FROM "Orm_Pdf_libro"
    #  ORDER BY "Orm_Pdf_libro"."paginas" DESC
    #  LIMIT 1
    # OFFSET 3

  # ==============================================================================================

  def Libro_morePages_Positions(self):
    # Obtener el cuarto y quinto libro con mas paginas
    return Libro.objects.values('isbn', 'paginas').order_by('-paginas')[3:5]

    #  CONSOLA SHELL PLUS >>>>>
    # In [35]: ormPdf_instance.Libro_morePages_Positions()
    # Out[35]: <QuerySet [{'isbn': '1912458965698', 'paginas': 300}, {'isbn': '1659865985986', 'paginas': 200}]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."paginas"
    #   FROM "Orm_Pdf_libro"
    #  ORDER BY "Orm_Pdf_libro"."paginas" DESC
    #  LIMIT 2
    # OFFSET 3

  # ==============================================================================================

  def explain_filterPages(self):
    return Libro.objects.filter(paginas__gte=200).explain

    #  CONSOLA SHELL PLUS >>>>>
    # In [39]: ormPdf_instance.explain_filterPages()
    # Out[39]: <bound method QuerySet.explain of <QuerySet [<Libro: Libro object (1234567898745)>,
    # <Libro: Libro object (1234567898746)>,
    # <Libro: Libro object (1234567898747)>,
    # <Libro: Libro object (1659865985986)>,
    # <Libro: Libro object (1912458965698)>]>>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."isbn",
    #        "Orm_Pdf_libro"."titulo",
    #        "Orm_Pdf_libro"."paginas",
    #        "Orm_Pdf_libro"."fecha_publicacion",
    #        "Orm_Pdf_libro"."imagen",
    #        "Orm_Pdf_libro"."desc_corta",
    #        "Orm_Pdf_libro"."estatus",
    #        "Orm_Pdf_libro"."categoria",
    #        "Orm_Pdf_libro"."editorial_id"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."paginas" >= 200
    #  LIMIT 21

  # ==============================================================================================

  def calculate_MinPages(self):
    # Calcular cual es el numero minimo de paginas que puede tener un libro, en esta consulta no tomamos en cuenta
    # los libros que no se especifico su numero de paginas por lo cual es 0 y este seria el mínimo numero de paginas.
    return Libro.objects.filter(paginas__gt=0).aggregate(Min('paginas'))

    #  CONSOLA SHELL PLUS >>>>>
    # In [42]: ormPdf_instance.calculate_MinPages()
    # Out[42]: {'paginas__min': 100}

    # SENTENCIA SQL <<<<<
    # SELECT MIN("Orm_Pdf_libro"."paginas") AS "paginas__min"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."paginas" > 0

  # ==============================================================================================

  def calculate_MaxPages(self):
    # Calcular cual es el numero máximo de paginas que puede tener un libro, aquí no necesitamos filtrar, este seria el
    # máximo numero de paginas
    return Libro.objects.aggregate(Max('paginas'))

    #  CONSOLA SHELL PLUS >>>>>
    # In [43]: ormPdf_instance.calculate_MaxPages()
    # Out[43]: {'paginas__max': 5000}

    # SENTENCIA SQL <<<<<
    # SELECT MAX("Orm_Pdf_libro"."paginas") AS "paginas__max"
    #   FROM "Orm_Pdf_libro"

  # ==============================================================================================

  def calculate_AvgPages(self):
    # Calcular cual es el numero medio de paginas que puede tener un libro, en esta consulta no tomamos en cuenta
    # los libros que no se especifico su numero de paginas para así solo considerar los libros con paginas.
    return Libro.objects.filter(paginas__gt=0).aggregate(Avg('paginas'))

    #  CONSOLA SHELL PLUS >>>>>
    # In [44]: ormPdf_instance.calculate_AvgPages()
    # Out[44]: {'paginas__avg': 1350.0}

    # SENTENCIA SQL <<<<<
    # SELECT AVG("Orm_Pdf_libro"."paginas") AS "paginas__avg"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."paginas" > 0

  # ==============================================================================================

  def counter_PagesLibro(self):
    # Sumar el total de paginas de todos los libros que tenemos
    return Libro.objects.filter(categoria__icontains='Cuentos').aggregate(Sum('paginas'))

    #  CONSOLA SHELL PLUS >>>>>
    # In [46]: ormPdf_instance.counter_PagesLibro()
    # Out[46]: {'paginas__sum': 7900}

    # SENTENCIA SQL <<<<<
    # SELECT SUM("Orm_Pdf_libro"."paginas") AS "paginas__sum"
    #   FROM "Orm_Pdf_libro"
    #  WHERE UPPER("Orm_Pdf_libro"."categoria"::text) LIKE UPPER('%Cuentos%')

  # ==============================================================================================

  def counter_all_Libro_Group(self):
    #  Agrupar los libros que son de Anime por categoría y contar cuantos libros de cada categoría hay.
    return Libro.objects.filter(categoria__contains='Anime').values('categoria').annotate(NumeroLibros=Count('*'))

    #  CONSOLA SHELL PLUS >>>>>
    # In [47]: ormPdf_instance.counter_all_Libro_Group()
    # Out[47]: <QuerySet [{'categoria': 'Anime', 'NumeroLibros': 1}]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."categoria",
    #        COUNT(*) AS "NumeroLibros"
    #   FROM "Orm_Pdf_libro"
    #  WHERE "Orm_Pdf_libro"."categoria"::text LIKE '%Anime%'
    #  GROUP BY "Orm_Pdf_libro"."categoria"
    #  LIMIT 21

  # ==============================================================================================

  def couner_all_Libros_and_Editorial_Groups(self):
    # Agrupar los libros que son de Python por categoría y por el nombre de la editorial y contar cuantos libros hay, a
    # diferencia del ejemplo anterior en este ejemplo se involucran dos modelos Libro y Editorial, por lo que estamos
    # hablando también de una union.
    return Libro.objects.filter(categoria__icontains='Cuento').values('categoria', 'editorial__nombre').annotate(
      NumeroLibros=Count('*'))

    #  CONSOLA SHELL PLUS >>>>>
    # In [48]: ormPdf_instance.couner_all_Libros_and_Editorial_Groups()
    # Out[48]: <QuerySet [{'categoria': 'Cuentos', 'editorial__nombre': 'Extra', 'NumeroLibros': 5}]>

    # SENTENCIA SQL <<<<<
    # SELECT "Orm_Pdf_libro"."categoria",
    #        "libreria_editorial"."nombre",
    #        COUNT(*) AS "NumeroLibros"
    #   FROM "Orm_Pdf_libro"
    #   LEFT OUTER JOIN "libreria_editorial"
    #     ON ("Orm_Pdf_libro"."editorial_id" = "libreria_editorial"."id")
    #  WHERE UPPER("Orm_Pdf_libro"."categoria"::text) LIKE UPPER('%Cuento%')
    #  GROUP BY "Orm_Pdf_libro"."categoria",
    #           "libreria_editorial"."nombre"
    #  LIMIT 21

  # ==============================================================================================

  def annotate_filter_libros(self):
    pass


# FILA 2
# # 1. Crea 5 autores y relaciónalos con el libro “Ciencia para Todos” usando bulk_create.

Autor.objects.bulk_create([
  Autor(nombre="Autor 1"),
  Autor(nombre="Autor 2"),
  Autor(nombre="Autor 3"),
  Autor(nombre="Autor 4"),
  Autor(nombre="Autor 5")
])

editorial_instance = Editorial.objects.get(id=2)

Libro.objects.create(
      isbn="2563236598563",
      titulo="Ciencia para Todos",
      paginas=350,
      fecha_publicacion="2020-10-27",
      imagen="",
      desc_corta="Conocimiento de la ciencia",
      estatus="A",
      categoria="Ciencia",
      editorial=editorial_instance,
      edicion_anterior=None
    )

#  CONSOLA SHELL PLUS >>>>>

# SENTENCIA SQL <<<<<

# ==============================================================================================

# # 2. Encuentra todos los autores cuyos nombres contengan la letra "e" y que hayan escrito un libro en la categoría "Educación".

#  CONSOLA SHELL PLUS >>>>>

# SENTENCIA SQL <<<<<

# ==============================================================================================

# # 3. Busca libros publicados entre los años 2018 y 2022, con más de 300 páginas, y que no pertenezcan a la categoría "Historia".

#  CONSOLA SHELL PLUS >>>>>

# SENTENCIA SQL <<<<<

# ==============================================================================================

# # 4. Dado el libro “Cuentos Cortos”, muestra todos sus autores.

#  CONSOLA SHELL PLUS >>>>>

# SENTENCIA SQL <<<<<

# ==============================================================================================

# # 5. Decrementa el número de páginas en 25 para todos los libros con más de 200 páginas y cuyo autor sea “Luis”.


from django.db.models import Min, Max, Avg, Sum, Count
from Orm_Pdf.models import Autor, Libro, Editorial, LibroCronica, AutorCapitulo
from django.db.models.functions import Left, Concat, Replace
from django.db.models import CharField, Case, Value as V
from django.db.models import F
from django.db.models import Q
from django.db.models import Prefetch

#Inserción básica
Autor.objects.create(nombre="Autor desde el ORM")

#Inserción masiva
Autor.objects.bulk_create([
Autor(nombre="Autor 1M"),
Autor(nombre="Autor 2M"),
Autor(nombre="Autor 3M")
])
#In [1]: Autor.objects.create(nombre="Gabriel García Márquez")
#   ...:
#   ...: # Inserción masiva
#   ...: Autor.objects.bulk_create([
#   ...:     Autor(nombre="Isabel Allende"),
#   ...:     Autor(nombre="Julio Cortázar"),
#   ...:     Autor(nombre="Mario Vargas Llosa")
#   ...: ])
#INSERT INTO "Orm_Pdf_autor" ("nombre")
#VALUES ('Gabriel García Márquez') RETURNING "Orm_Pdf_autor"."id"
#Execution time: 0.006180s [Database: default]
#BEGIN
#Execution time: 0.000000s [Database: default]
#INSERT INTO "Orm_Pdf_autor" ("nombre")
#VALUES ('Isabel Allende'), ('Julio Cortázar'), ('Mario Vargas Llosa') RETURNING "Orm_Pdf_autor"."id"
#Execution time: 0.000000s [Database: default]
#Out[1]:
#[<Autor: Yo soy Isabel Allende>,
#<Autor: Yo soy Julio Cortázar>,
#<Autor: Yo soy Mario Vargas Llosa>]

##Consultar todos los registros
Autor.objects.all() 
#Out[1]: SELECT "Orm_Pdf_autor"."id",
#       "Orm_Pdf_autor"."nombre"
# FROM "Orm_Pdf_autor"
# LIMIT 21
#Execution time: 0.014981s [Database: default]
#<QuerySet [<Autor: Yo soy Gabriel García Márquez>, <Autor: Yo soy Isabel Allende>, <Autor: Yo soy Julio Cortázar>, <Autor: Yo soy Mario Vargas Llosa>]>

#Si conocemos la clave primaria del registro que estamos buscando podemos usar el método get.
Libro.objects.get(isbn='1935182080')
#In [2]: Libro.objects.get(isbn='1935182080')
#   ...:
#SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."isbn" = '1935182080'
# LIMIT 21
#Execution time: 0.000000s [Database: default]
#Out[2]: <Libro: El libro es Nuevo Libro de Prueba>

###Obtener solo el primer resultado
#In [4]: Libro.objects.all().first()
#   ...:
#SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#      "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
# ORDER BY "Orm_Pdf_libro"."isbn" ASC
# LIMIT 1
#Execution time: 0.000000s [Database: default]
#Out[4]: <Libro: El libro es Nuevo Libro de Prueba>

#Obtener solo el ultimo resultado
Libro.objects.all().last() 
#In [7]: Libro.objects.all().last()
#SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
 #ORDER BY "Orm_Pdf_libro"."isbn" DESC
 #LIMIT 1
#Execution time: 0.000000s [Database: default]
#Out[7]: <Libro: El libro es El Vuelo de las Águilas>

#Obtener los primeros N resultados, Ejemplo de obtener los primeros 5 libros
let = Libro.objects.all()[:2]
#In [9]: let
#Out[9]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
 #      "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
# LIMIT 2
#Execution time: 0.000557s [Database: default]
#<QuerySet [<Libro: El libro es Nuevo Libro de Prueba>, <Libro: El libro es El Misterio del Bosque>]>

#Ejempo de obtener los libros cuyo isbn comience con un 16
Libro.objects.filter(isbn__startswith="2")
#In [10]: Libro.objects.filter(isbn__startswith="2")
#Out[10]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."isbn" LIKE '2%' ESCAPE '\'
# LIMIT 21
#Execution time: 0.005522s [Database: default]
#<QuerySet [<Libro: El libro es Los Secretos del Mar>]>

#Ejemplo de los libros que tienen mas de 200 paginas
Libro.objects.filter(paginas__gt=200)
#In [12]: Libro.objects.filter(paginas__gt=200)
#Out[12]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."paginas" > 200
# LIMIT 21

#Execution time: 0.000000s [Database: default]
#<QuerySet [<Libro: El libro es Nuevo Libro de Prueba>, <Libro: El libro es Los Secretos del Mar>]>

#Ejemplo de libros que tienen mas de 200 paginas pero cuyo isbn no sea ninguno de estos dos
#('1933988592','1884777600')
let_libro = Libro.objects.filter(paginas__gt=200).exclude(isbn__in=('1933988592','1884777600'))
#In [14]:  let_libro
#Out[14]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
# WHERE ("Orm_Pdf_libro"."paginas" > 200 AND NOT ("Orm_Pdf_libro"."isbn" IN ('1933988592', '1884777600')))
# LIMIT 21

#Execution time: 0.000549s [Database: default]
#QuerySet [<Libro: El libro es Nuevo Libro de Prueba>, <Libro: El libro es Los Secretos del Mar>]>


#Ejemplo de libros que tienes 200 o mas paginas
Libro.objects.filter(paginas__gte=200)
#In [15]: Libro.objects.filter(paginas__gte=200)
#Out[15]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
# FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."paginas" >= 200
# LIMIT 21
#Execution time: 0.000461s [Database: default]
#<QuerySet [<Libro: El libro es El Misterio del Bosque>, <Libro: El libro es Nuevo Libro de Prueba>, <Libro: El libro es Los Secretos del Mar>]> 

#Ejemplo de una consulta de los libros que tienen 200 o mas paginas, pero solo muestra las columnas isbn 
Libro.objects.filter(paginas__gte=100).values('isbn','paginas')
#Out[16]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas"
#  FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."paginas" >= 100
# LIMIT 21

#Execution time: 0.013968s [Database: default]
#<QuerySet [{'isbn': '3333333333333', 'paginas': 150}, {'isbn': '1111111111111', 'paginas': 200}, {'isbn': '1935182080', 'paginas': 300}, {'isbn': '2222222222222', 'paginas': 350}]>

#Ejemplo de los libros que tienen menos de 200 paginas
Libro.objects.filter(paginas__lt=200)

#Ejemplo de una consulta de los libros que tienen 200 o mas paginas, pero solo muestra las columnas isbn 
#Libro.objects.filter(paginas__gte=200).values('isbn','paginas')
#In [20]: Libro.objects.filter(paginas__gte=200).values('isbn','paginas')
#Out[20]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas"
#  FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."paginas" >= 200
# LIMIT 21

#Execution time: 0.006634s [Database: default]
#<QuerySet [{'isbn': '1111111111111', 'paginas': 200}, {'isbn': '1935182080', 'paginas': 300}, {'isbn': '2222222222222', 'paginas': 350}]>    

#Ejemplo de libros que tienes 200 o menos paginas
Libro.objects.filter(paginas__lte=350)

#In [21]: Libro.objects.filter(paginas__lte=350)
#Out[21]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#      "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."paginas" <= 350
# LIMIT 21

#Execution time: 0.000304s [Database: default]
#<QuerySet [<Libro: El libro es El Vuelo de las Águilas>, <Libro: El libro es El Misterio del Bosque>, <Libro: El libro es Nuevo Libro de Prueba>, <Libro: El libro es Los Secretos del Mar>]>

#Ejemplo de contar los libros que tienen menos de 200 paginas
Libro.objects.filter(paginas__lt=250).count() 
#In [22]: Libro.objects.filter(paginas__lt=250).count()
#SELECT COUNT(*) AS "__count"
#  FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."paginas" < 250

#Execution time: 0.000000s [Database: default]
#Out[22]: 2

#Ejemplo de consulta de los libros con 200 paginas o con 300 paginas
consulta1 = Libro.objects.filter(paginas=200)

#In [24]: consulta1
#Out[24]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."paginas" = 200
# LIMIT 21

#Execution time: 0.000616s [Database: default]
#<QuerySet [<Libro: El libro es El Misterio del Bosque>]>

consulta2 = Libro.objects.filter(paginas=300)
(consulta1 | consulta2).values('isbn','paginas')

#In [25]: consulta2 = Libro.objects.filter(paginas=300)
#    ...: (consulta1 | consulta2).values('isbn','paginas')
#Out[25]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas"
#  FROM "Orm_Pdf_libro"
# WHERE ("Orm_Pdf_libro"."paginas" = 200 OR "Orm_Pdf_libro"."paginas" = 300)
# LIMIT 21

##Execution time: 0.000000s [Database: default]
#<QuerySet [{'isbn': '1111111111111', 'paginas': 200}, {'isbn': '1935182080', 'paginas': 300}]>

#Ejemplo de una consulta que muestra los libros cuya fecha de publicación es 2012
Libro.objects.filter(fecha_publicacion__year=2019).values('isbn','fecha_publicacion')
#In [26]: Libro.objects.filter(fecha_publicacion__year=2019).values('isbn','fecha_publicacion')
#Out[26]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."fecha_publicacion"
#  FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."fecha_publicacion" BETWEEN '2019-01-01' AND '2019-12-31'
# LIMIT 21

#Execution time: 0.000000s [Database: default]
#<QuerySet [{'isbn': '3333333333333', 'fecha_publicacion': datetime.date(2019, 11, 30)}]>

#Consultar los libros cuyo isbn comience con un 19 seguido de 8 digitos
Libro.objects.filter(isbn__regex=r'19\d{8}$').values('isbn')
#In [27]: Libro.objects.filter(isbn__regex=r'19\d{8}$').values('isbn')
#Out[27]: SELECT "Orm_Pdf_libro"."isbn"
#  FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."isbn" REGEXP '19\d{8}$'
# LIMIT 21

#Execution time: 0.001001s [Database: default]
#<QuerySet [{'isbn': '1935182080'}]>

#Unir en una sola consulta el nombre los Autores que contengan la palabra hill con las Editoriales cuyo nombre contenga
#también la palabra hill.
a1 = Autor.objects.filter(nombre__contains='hill').values('nombre')
#Out[29]: SELECT "Orm_Pdf_autor"."nombre"
#  FROM "Orm_Pdf_autor"
# WHERE "Orm_Pdf_autor"."nombre" LIKE '%hill%' ESCAPE '\'
# LIMIT 21

#Execution time: 0.000000s [Database: default]
#<QuerySet []>

#Obtener el cuarto libro con mas paginas
let_libro2= Libro.objects.values('isbn','paginas').order_by('-paginas')[3]
# [30]: let_libro2= Libro.objects.values('isbn','paginas').order_by('-paginas')[3]
#SELECT "Orm_Pdf_libro"."isbn",
 #      "Orm_Pdf_libro"."paginas"
#  FROM "Orm_Pdf_libro"
# ORDER BY "Orm_Pdf_libro"."paginas" DESC
 #LIMIT 1
#OFFSET 3

#Execution time: 0.000000s [Database: default]

#Obtener el cuarto y quinto libro con mas pagina
let_libro3= Libro.objects.values('isbn','paginas').order_by('-paginas')[1:2]

#In [32]: let_libro3
#Out[32]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas"
#  FROM "Orm_Pdf_libro"
# ORDER BY "Orm_Pdf_libro"."paginas" DESC
# LIMIT 1
#OFFSET 1

#Execution time: 0.000000s [Database: default]
#<QuerySet [{'isbn': '1935182080', 'paginas': 300}]>
 
 #podemos seleccionar por ejemplo la pagina 3
Libro.objects.LibroPorPaginas(3)


#/////
#In [6]: let
#Out[6]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#      "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."paginas" >= 200
# LIMIT 21

#Execution time: 0.003384s [Database: default]
#<bound method QuerySet.explain of <QuerySet [<Libro: El libro es El Misterio del Bosque>, <Libro: El libro es Nuevo Libro de Prueba>, <Libro: El libro es Los Secretos del Mar>]>>

#Calcular cual es el numero minimo de paginas que puede tener un libro
let_librof= Libro.objects.filter(paginas__gt=0).aggregate(Min('paginas'))
#In [7]: let_librof= Libro.objects.filter(paginas__gt=0).aggregate(Min('paginas'))
#SELECT MIN("Orm_Pdf_libro"."paginas") AS "paginas__min"
 # FROM "Orm_Pdf_libro"
 #WHERE "Orm_Pdf_libro"."paginas" > 0

#Execution time: 0.000000s [Database: default]

#Calcular cual es el numero máximo de paginas que puede tener un libro, aquí no necesitamos filtrar, este seria el
Libro.objects.aggregate(Max('paginas'))
#SELECT MAX("Orm_Pdf_libro"."paginas") AS "paginas__max"
#  FROM "Orm_Pdf_libro"

#Execution time: 0.001006s [Database: default]
#Out[8]: {'paginas__max': 350}

#Calcular cual es el numero medio de paginas que puede tener un libro
Libro.objects.filter(paginas__gt=0).aggregate(Avg('paginas'))
#SELECT AVG("Orm_Pdf_libro"."paginas") AS "paginas__avg"
#  FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."paginas" > 0

#Execution time: 0.000000s [Database: default]
#Out[9]: {'paginas__avg': 250.0}

#Sumar el total de paginas de todos los libros que tenemos de Python
Libro.objects.filter(categoria__icontains='Ficción').aggregate(Sum('paginas'))
#SELECT SUM("Orm_Pdf_libro"."paginas") AS "paginas__sum"
#  FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."categoria" LIKE '%Ficción%' ESCAPE '\'

#Execution time: 0.000575s [Database: default]
#Out[11]: {'paginas__sum': 650}

#Agrupar libros de Python por categoría y editorial, contando cuántos hay en cada grupo.
Libro.objects.filter(categoria__icontains='Ficción').values('categoria','editorial__nombre').annotate(NumeroLibros=Count('*'))
#In [12]: Libro.objects.filter(categoria__icontains='Ficción').values('categoria','editorial__nombr 
#    ...: e').annotate(NumeroLibros=Count('*'))
#Out[12]: SELECT "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_editorial"."nombre",
#       COUNT(*) AS "NumeroLibros"
#  FROM "Orm_Pdf_libro"
# INNER JOIN "Orm_Pdf_editorial"
#    ON ("Orm_Pdf_libro"."editorial_id" = "Orm_Pdf_editorial"."id")
# WHERE "Orm_Pdf_libro"."categoria" LIKE '%Ficción%' ESCAPE '\'
# GROUP BY "Orm_Pdf_libro"."categoria",
#          "Orm_Pdf_editorial"."nombre"
# LIMIT 21

#Execution time: 0.000516s [Database: default]
#<QuerySet [{'categoria': 'Ficción', 'editorial__nombre': 'Editorial Ficción', 'NumeroLibros': 1}, {'categoria': 'Ficción', 'editorial__nombre': 'Editorial de Prueba', 'NumeroLibros': 1}]>

#Agrupar los libros por fecha_publicacion y filtrar para mostrar solo las fechas que tienen más de 5 libros publicados.
#Libro.objects.values('fecha_publicacion').annotate(cant_fec_pub=Count('fecha_publicacion')).filter(cant_fec_pub__gte=3)
#Out[14]: SELECT "Orm_Pdf_libro"."fecha_publicacion",
#       COUNT("Orm_Pdf_libro"."fecha_publicacion") AS "cant_fec_pub"
#  FROM "Orm_Pdf_libro"
# GROUP BY "Orm_Pdf_libro"."fecha_publicacion"
#HAVING COUNT("Orm_Pdf_libro"."fecha_publicacion") >= 3
# LIMIT 21

#Execution time: 0.000000s [Database: default]
#<QuerySet []>

#Si quisiéramos obtener el detalle de los libros de la consulta anterior podemos hacer lo siguiente
Consulta_fechas =Libro.objects.values('fecha_publicacion').annotate(cant_fec_pub=Count('fecha_publicacion')).filter(cant_fec_pub__gte=3).values_list('fecha_publicacion')
#Out[16]: SELECT "Orm_Pdf_libro"."fecha_publicacion"
#  FROM "Orm_Pdf_libro"
# GROUP BY "Orm_Pdf_libro"."fecha_publicacion"
#HAVING COUNT("Orm_Pdf_libro"."fecha_publicacion") >= 3
# LIMIT 21

##Execution time: 0.000000s [Database: default]
#<QuerySet []>

#Usar distinct sobre paginas para obtener solo valores únicos y evitar duplicados, especialmente para excluir los libros con 0 páginas.
Libro.objects.values('paginas').filter(paginas__lt=200).distinct()
#In [19]: Libro.objects.values('paginas').filter(paginas__lt=200).distinct()
#Out[19]: SELECT DISTINCT "Orm_Pdf_libro"."paginas"
#  FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."paginas" < 200
# LIMIT 21

#Execution time: 0.001002s [Database: default]
#<QuerySet [{'paginas': 150}]>

#Queremos que nuestra desc_corta solo muestre los primeros 15 caracteres
Libro.objects.annotate(desc_resumida=Left('desc_corta',15)).values('isbn','desc_resumida')
#In [22]: Libro.objects.annotate(desc_resumida=Left('desc_corta',15)).values('isbn','desc_resumida' 
#    ...: )
#Out[22]: SELECT "Orm_Pdf_libro"."isbn",
#       SUBSTR("Orm_Pdf_libro"."desc_corta", 1, 15) AS "desc_resumida"
#  FROM "Orm_Pdf_libro"
#LIMIT 21

#Execution time: 0.000000s [Database: default]
#<QuerySet [{'isbn': '1935182080', 'desc_resumida': 'Descripción bre'}, {'isbn': '1111111111111', 'desc_resumida': 'Una historia ll'}, {'isbn': '2222222222222', 'desc_resumida': 'Exploración de '}, {'isbn': '3333333333333', 'desc_resumida': 'Una narrativa é'}]>

# Concatenamos al final de desc_resumida usando Concat y Value
Libro.objects.annotate(desc_resumida=Concat(Left('desc_corta',15),V('...'))).values('isbn','desc_resumida')
#Out[24]: SELECT "Orm_Pdf_libro"."isbn",
#       (COALESCE(SUBSTR("Orm_Pdf_libro"."desc_corta", 1, 15), '') || COALESCE('...', '')) AS "desc_resumida"
#  FROM "Orm_Pdf_libro"
# LIMIT 21

#Execution time: 0.000000s [Database: default]
#<QuerySet [{'isbn': '1935182080', 'desc_resumida': 'Descripción bre...'}, {'isbn': '1111111111111', 'desc_resumida': 'Una historia ll...'}, {'isbn': '2222222222222', 'desc_resumida': 'Exploración de ...'}, {'isbn': '3333333333333', 'desc_resumida': 'Una narrativa é...'}]>

#Queremos saber que libros tienen un titulo igual a su desc_corta dentro de sus primeros 50 caracteres, para especificar que lo que va a comparar es una columna del modelo y no una cadena de texto usamos F(nombre_columna)
Libro.objects.annotate(tit50= Left('titulo',50), desc50= Left('desc_corta',50)).filter(tit50 = F('desc50')).values('isbn','tit50','desc50')
#In [25]: Libro.objects.annotate(tit50= Left('titulo',50), desc50= Left('desc_corta',50)).filter(ti 
 #   ...: t50 = F('desc50')).values('isbn','tit50','desc50')
 #   ...:
#Out[25]: SELECT "Orm_Pdf_libro"."isbn",
#       SUBSTR("Orm_Pdf_libro"."titulo", 1, 50) AS "tit50",
#       SUBSTR("Orm_Pdf_libro"."desc_corta", 1, 50) AS "desc50"
 # FROM "Orm_Pdf_libro"
 #WHERE SUBSTR("Orm_Pdf_libro"."titulo", 1, 50) = (SUBSTR("Orm_Pdf_libro"."desc_corta", 1, 50))     
 #LIMIT 21

#Execution time: 0.001000s [Database: default]
#<QuerySet []>

#Queremos quitarle las comillas a los nombres de nuestra categoría y remplazarlas por un *
Libro.objects.annotate(categoria_sin_comillas = Replace('categoria', V('"'),V('*'))).values('isbn','categoria','categoria_sin_comillas')
#In [26]: Libro.objects.annotate(categoria_sin_comillas = Replace('categoria', V('"'),V('*'))).valu 
#    ...: es('isbn','categoria','categoria_sin_comillas')
#   ...:
#Out[26]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."categoria",
#       REPLACE("Orm_Pdf_libro"."categoria", '"', '*') AS "categoria_sin_comillas"
#  FROM "Orm_Pdf_libro"
# LIMIT 21

#Execution time: 0.002607s [Database: default]
#<QuerySet [{'isbn': '1935182080', 'categoria': 'Ficción', 'categoria_sin_comillas': 'Ficción'}, {'isbn': '1111111111111', 'categoria': 'Aventura', 'categoria_sin_comillas': 'Aventura'}, {'isbn': '2222222222222', 'categoria': 'Ficción', 'categoria_sin_comillas': 'Ficción'}, {'isbn': '3333333333333', 'categoria': 'Naturaleza', 'categoria_sin_comillas': 'Naturaleza'}]>

#En este ejemplo queremos las categorías que sean sobre Python o Java o net y que no tengan paginas igual a 0
Libro.objects.filter(
(Q(categoria__contains='ficcion') |
Q(categoria__contains='aventura') |
Q(categoria__contains='naturaleza')) &
~Q(paginas=0))

#In [27]: Libro.objects.filter(
#    ...: (Q(categoria__contains='ficcion') |
#    ...: Q(categoria__contains='aventura') |
#    ...: Q(categoria__contains='naturaleza')) &
#    ...: ~Q(paginas=0))
#Out[27]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
 #      "Orm_Pdf_libro"."estatus",
 #      "Orm_Pdf_libro"."categoria",
 #      "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
# WHERE (("Orm_Pdf_libro"."categoria" LIKE '%ficcion%' ESCAPE '\' OR "Orm_Pdf_libro"."categoria" LIKE '%aventura%' ESCAPE '\' OR "Orm_Pdf_libro"."categoria" LIKE '%naturaleza%' ESCAPE '\') AND NOT ("Orm_Pdf_libro"."paginas" = 0))
# LIMIT 21

#Execution time: 0.000000s [Database: default]
#<QuerySet [<Libro: El libro es El Misterio del Bosque>, <Libro: El libro es El Vuelo de las Águilas>]>


#La relación la podemos hacer directamente desde nuestro Libro usando el nombre de la tabla librocronica,
#nuestra consulta quedaría de esta manera:
Libro.objects.filter(librocronica__descripcion_larga__isnull=True).values('isbn','titulo','librocronica__descripcion_larga')
#In [28]: Libro.objects.filter(librocronica__descripcion_larga__isnull=True).values('isbn','titulo' 
#    ...: ,'librocronica__descripcion_larga')
#    ...:
#Out[28]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_librocronica"."descripcion_larga"
#  FROM "Orm_Pdf_libro"
#  LEFT OUTER JOIN "Orm_Pdf_librocronica"
#    ON ("Orm_Pdf_libro"."isbn" = "Orm_Pdf_librocronica"."libro_id")
# WHERE "Orm_Pdf_librocronica"."descripcion_larga" IS NULL
# LIMIT 21

#Execution time: 0.001003s [Database: default]
#<QuerySet [{'isbn': '1935182080', 'titulo': 'Nuevo Libro de Prueba', 'librocronica__descripcion_larga': None}, {'isbn': '1111111111111', 'titulo': 'El Misterio del Bosque', 'librocronica__descripcion_larga': None}, {'isbn': '2222222222222', 'titulo': 'Los Secretos del Mar', 'librocronica__descripcion_larga': None}, {'isbn': '3333333333333', 'titulo': 'El Vuelo de las Águilas', 'librocronica__descripcion_larga': None}]>


#la relacion uno a uno de Libro y LibroCronica y es usando select_related(modelo_relacion).

Libro.objects.select_related('librocronica').filter(categoria__contains='naturaleza')
#In [29]: Libro.objects.select_related('librocronica').filter(categoria__contains='naturaleza')     
#Out[29]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#      "Orm_Pdf_libro"."editorial_id",
#       "Orm_Pdf_librocronica"."descripcion_larga",
#       "Orm_Pdf_librocronica"."libro_id"
#  FROM "Orm_Pdf_libro"
#  LEFT OUTER JOIN "Orm_Pdf_librocronica"
#    ON ("Orm_Pdf_libro"."isbn" = "Orm_Pdf_librocronica"."libro_id")
# WHERE "Orm_Pdf_libro"."categoria" LIKE '%naturaleza%' ESCAPE '\'
# LIMIT 21

#Execution time: 0.000522s [Database: default]
#<QuerySet [<Libro: El libro es El Vuelo de las Águilas>]>

# consultar primero nuestro modelo LibroCronica.
LibroCronica.objects.select_related('libro').all()[:3]
#Out[30]: SELECT "Orm_Pdf_librocronica"."descripcion_larga",
#       "Orm_Pdf_librocronica"."libro_id",
#       "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_librocronica"
# INNER JOIN "Orm_Pdf_libro"
#    ON ("Orm_Pdf_librocronica"."libro_id" = "Orm_Pdf_libro"."isbn")
# LIMIT 3

#Execution time: 0.001491s [Database: default]
#<QuerySet []

#Queremos consultar los libros cuya categoría sea Python y entonces imprimir el nombre de su editorial el cual se
#encuentra en el modelo 

categorias = Libro.objects.all().filter(categoria__icontains='aventura')
#In [32]: categorias
#Out[32]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
#WHERE "Orm_Pdf_libro"."categoria" LIKE '%aventura%' ESCAPE '\'
# LIMIT 21

#Execution time: 0.000000s [Database: default]
#<QuerySet [<Libro: El libro es El Misterio del Bosque

#SELECT "Orm_Pdf_editorial"."id",
#       "Orm_Pdf_editorial"."nombre"
#  FROM "Orm_Pdf_editorial"
# WHERE "Orm_Pdf_editorial"."id" = 2
# LIMIT 21

#Execution time: 0.000000s [Database: default]
#Editorial Aventura

#En este ejemplo vamos a consultar 2 Autores y después vamos a buscar todos los libros que han escrito
autores = Autor.objects.filter(pk__in=(3,2))
for autor in autores:
 print(f'Autor: {autor}')
 print('Libros escritos:')
 for libro in autor.libro.all():
     print(libro.titulo)
     
#SELECT "Orm_Pdf_autor"."id",
#       "Orm_Pdf_autor"."nombre"
#  FROM "Orm_Pdf_autor"
# WHERE "Orm_Pdf_autor"."id" IN (3, 2)

#Execution time: 0.000000s [Database: default]
#Autor: Yo soy Gabriel García Márquez
#Libros escritos:
#SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#      "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
# INNER JOIN "Orm_Pdf_autorcapitulo"
#    ON ("Orm_Pdf_libro"."isbn" = "Orm_Pdf_autorcapitulo"."libro_id")
# WHERE "Orm_Pdf_autorcapitulo"."autor_id" = 2

#Execution time: 0.001573s [Database: default]
#Nuevo Libro de Prueba
#Autor: Yo soy Isabel Allende
#Libros escritos:
#SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#      "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
# INNER JOIN "Orm_Pdf_autorcapitulo"
#    ON ("Orm_Pdf_libro"."isbn" = "Orm_Pdf_autorcapitulo"."libro_id")
# WHERE "Orm_Pdf_autorcapitulo"."autor_id" = 3

#Execution time: 0.000000s [Database: default]
#El Misterio del Bosque

#usaremos el método prefetch_related para especificarle que
#Autor tiene una relación con libros
autores = Autor.objects.filter(pk__in= (2,3)).prefetch_related('libro')

for autor in autores:
 print(f'Autor: {autor}')
 print('Libros escritos:')
 for libro in autor.libro.all():
     print(libro.titulo)
     
#In [46]: autores = Autor.objects.filter(pk__in= (2,3)).prefetch_related('libro')
#    ...:
#    ...: for autor in autores:
#    ...:  print(f'Autor: {autor}')
#    ...:  print('Libros escritos:')
#    ...:  for libro in autor.libro.all():
#    ...:      print(libro.titulo)
#    ...:
#SELECT "Orm_Pdf_autor"."id",
#       "Orm_Pdf_autor"."nombre"
#  FROM "Orm_Pdf_autor"
# WHERE "Orm_Pdf_autor"."id" IN (2, 3)

#Execution time: 0.000000s [Database: default]
#SELECT ("Orm_Pdf_autorcapitulo"."autor_id") AS "_prefetch_related_val_autor_id",
#       "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
# INNER JOIN "Orm_Pdf_autorcapitulo"
#    ON ("Orm_Pdf_libro"."isbn" = "Orm_Pdf_autorcapitulo"."libro_id")
# WHERE "Orm_Pdf_autorcapitulo"."autor_id" IN (2, 3)

#Execution time: 0.001063s [Database: default]
#Autor: Yo soy Gabriel García Márquez
#Libros escritos:
#Nuevo Libro de Prueba
#Autor: Yo soy Isabel Allende
#Libros escritos:
#El Misterio del Bosque

#mostrar el nombre de la editorial por cada uno de los libros
autores = Autor.objects.filter(pk__in=(1,3)).prefetch_related('libro')

for autor in autores:
    print(f'Autor: {autor}')
    print('Libros escritos:')
    for libro in autor.libro.all():
        print(f'{libro.isbn} Editorial: {libro.editorial.nombre}')
        
#SELECT "Orm_Pdf_autor"."id",
#       "Orm_Pdf_autor"."nombre"
#  FROM "Orm_Pdf_autor"
# WHERE "Orm_Pdf_autor"."id" IN (1, 3)

#Execution time: 0.000000s [Database: default]
#SELECT ("Orm_Pdf_autorcapitulo"."autor_id") AS "_prefetch_related_val_autor_id",
#       "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
# INNER JOIN "Orm_Pdf_autorcapitulo"
#    ON ("Orm_Pdf_libro"."isbn" = "Orm_Pdf_autorcapitulo"."libro_id")
# WHERE "Orm_Pdf_autorcapitulo"."autor_id" IN (3)

#Execution time: 0.000000s [Database: default]
#Autor: Yo soy Isabel Allende
#Libros escritos:
#SELECT "Orm_Pdf_editorial"."id",
#       "Orm_Pdf_editorial"."nombre"
#  FROM "Orm_Pdf_editorial"
# WHERE "Orm_Pdf_editorial"."id" = 2
# LIMIT 21
#Execution time: 0.000000s [Database: default]
#1111111111111 Editorial: Editorial Aventura

#va buscar el editorial y pone el nombre especifico del editorial del id que se le haya puesto
libro_y_editorial = Libro.objects.select_related('editorial')
autores = Autor.objects.filter(pk__in=(2, 3)).prefetch_related(
    Prefetch('libro', queryset=libro_y_editorial)
)

for autor in autores:
    print(f'Autor: {autor}')
    print('Libros escritos:')
    for libro in autor.libro.all():
        print(f'{libro.isbn} Editorial: {libro.editorial.nombre}')

#Execution time: 0.001012s [Database: default]
#Autor: Yo soy Gabriel García Márquez
#Libros escritos:
#1935182080 Editorial: Editorial de Prueba
#Autor: Yo soy Isabel Allende
#Libros escritos:
#1111111111111 Editorial: Editorial Aventura


#FILA 2
# 1. Crea 5 autores y relaciónalos con el libro “Ciencia para Todos” usando bulk_create.
Autor.objects.bulk_create([
Autor(nombre="Julissa"),
Autor(nombre="kevin"),
Autor(nombre="Alan"),
Autor(nombre="Teo"),
Autor(nombre="Zimba"),
Autor(nombre="Lulu"),
])
#CONSOLA SHELL PLUS 
#In [1]: Autor.objects.bulk_create([
#   ...: Autor(nombre="Julissa"),
#   ...: Autor(nombre="kevin"),
#   ...: Autor(nombre="Alan"),
#   ...: Autor(nombre="Teo"),
#   ...: Autor(nombre="Zimba"),
#   ...: Autor(nombre="Lulu"),
#   ...: ])
#BEGIN
#
#Execution time: 0.000000s [Database: default]
#INSERT INTO "Orm_Pdf_autor" ("nombre")
#VALUES ('Julissa'), ('kevin'), ('Alan'), ('Teo'), ('Zimba'), ('Lulu') RETURNING "Orm_Pdf_autor"."id"
#
#Execution time: 0.000000s [Database: default]
#Out[1]: 
#[<Autor: Yo soy Julissa>,
# <Autor: Yo soy kevin>,
# <Autor: Yo soy Alan>,
# <Autor: Yo soy Teo>,
# <Autor: Yo soy Zimba>,
# <Autor: Yo soy Lulu>]


# 2. Encuentra todos los autores cuyos nombres contengan la letra "e" y que hayan escrito un libro en la categoría "Educación".
# Filtrar los autores cuyos nombres contienen la letra 'e' y que tienen libros en la categoría 'Educación'
autores_en_educacion = Autor.objects.filter(
    nombre__contains='e',
    libros_autores__categoria='Ficción'
).distinct().values('nombre')


# 3. Busca libros publicados entre los años 2018 y 2022, con más de 300 páginas, y que no pertenezcan a la categoría "Historia".
Libro.objects.filter(fecha_publicacion__year=2019).values('isbn','fecha_publicacion')
Libro.objects.filter(paginas=150)
Libro.objects.filter(categoria__icontains='Aventura')

#
#In [17]: Libro.objects.filter(fecha_publicacion__year=2019).values('isbn','fecha_publicacion')
#    ...: Libro.objects.filter(paginas=150)
#    ...: Libro.objects.filter(categoria__icontains='Aventura')
#Out[17]: SELECT "Orm_Pdf_libro"."isbn",
#       "Orm_Pdf_libro"."paginas",
#       "Orm_Pdf_libro"."titulo",
#       "Orm_Pdf_libro"."fecha_publicacion",
#       "Orm_Pdf_libro"."imagen",
#       "Orm_Pdf_libro"."desc_corta",
#       "Orm_Pdf_libro"."estatus",
#       "Orm_Pdf_libro"."categoria",
#       "Orm_Pdf_libro"."editorial_id"
#  FROM "Orm_Pdf_libro"
# WHERE "Orm_Pdf_libro"."categoria" LIKE '%Aventura%' ESCAPE '\'
# LIMIT 21
#
#Execution time: 0.000000s [Database: default]
#<QuerySet [<Libro: El libro es El Misterio del Bosque>]>

# 4. Dado el libro “Cuentos Cortos”, muestra todos sus autores.
libro = Libro.objects.get(titulo="Nuevo Libro de Prueba")
autores = libro.autores.all()


# 5. Decrementa el número de páginas en 25 para todos los libros con más de 200 páginas y cuyo autor sea “Luis”.
libros = Libro.objects.filter(
    paginas__gt=100,
    autores__nombre="Gabriel García Márquez"
).update(paginas=F('paginas') - 300)









