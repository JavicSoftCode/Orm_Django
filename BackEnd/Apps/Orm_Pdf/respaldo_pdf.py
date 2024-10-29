from django.db.models import Min, Max, Avg, Sum, Count, F, Q, Prefetch # Funciones de agregación
from django.db.models.functions import Left  # 134 line
from django.db.models import Value as V  # 140
from django.db.models.functions import Left, Concat  # 140
from django.db.models import CharField, Case, Value as V  # 146
from django.db.models.functions import Left, Concat, Replace  # 146
from BackEnd.Apps.Orm_Pdf.models import *  # Importar modelos base
from django.db.models import Case, When, Value as V, CharField
from django.db.models.functions import Length, Concat, Left
from django.db.models import Prefetch
# from django.db.models import Q

# Inserción básica
Autor.objects.create(nombre="Autor desde el ORM")

# Inserción masiva
Autor.objects.bulk_create([
  Autor(nombre="Autor 1M"),
  Autor(nombre="Autor 2M"),
  Autor(nombre="Autor 3M")
])

# Consultar todos los registros
Autor.objects.all()

# Si conocemos la clave primaria del registro que estamos buscando podemos usar el método get.
Libro.objects.get(isbn='1935182080')

Libro.objects.get(pk='1935182080')

# Ahora podemos usar nuestra función como parte del modelo
Libro.objects.buscar_por_isbn("1935182080")

# Obtener solo el primer resultado
Libro.objects.all().first()

# Obtener solo el ultimo resultado
Libro.objects.all().last()

# Ejemplo de obtener los primeros 5 libros
let = Libro.objects.all()[:3]

# Ejempo de obtener los libros cuyo isbn comience con un 16
Libro.objects.filter(isbn__startswith="16")

# Ejemplo de los libros que tienen mas de 200 paginas
Libro.objects.filter(paginas__gt=200)

# Ejemplo de libros que tienen mas de 200 paginas pero cuyo isbn no sea ninguno de estos dos
# ('1933988592','1884777600')
let_libro = Libro.objects.filter(paginas__gt=200).exclude(isbn__in=('1933988592', '1884777600'))

# Ejemplo de libros que tiene 200 o mas paginas
Libro.objects.filter(paginas__gte=200)

# Ejemplo de una consulta de los libros que tienen 200 o mas paginas, pero solo muestra las columnas isbn y paginas
Libro.objects.filter(paginas__gte=200).values('isbn', 'paginas')

# Ejemplo de los libros que tienen menos de 200 paginas
Libro.objects.filter(paginas__lt=200)

# Ejemplo de libros que tienes 200 o menos paginas
Libro.objects.filter(paginas__lte=200)

# Ejemplo de contar los libros que tienen menos de 200 paginas
Libro.objects.filter(paginas__lt=200).count()

# Ejemplo de consulta de los libros con 200 paginas o con 300 paginas
consulta1 = Libro.objects.filter(paginas=200)
consulta2 = Libro.objects.filter(paginas=300)
(consulta1 | consulta2).values('isbn', 'paginas')

# Ejemplo de una consulta que muestra los libros cuya fecha de publicación es 2012
Libro.objects.filter(fecha_publicacion__year=2012).values('isbn', 'fecha_publicacion')

# Consultar los libros cuyo isbn comience con un 19 seguido de 8 digitos
Libro.objects.filter(isbn__regex=r'19\d{8}$').values('isbn')

# Unir en una sola consulta el nombre los Autores que contengan la palabra hill con las Editoriales cuyo nombre contenga
# también la palabra hill.
a1 = Autor.objects.filter(nombre__contains='hill').values('nombre')
e1 = Editorial.objects.filter(nombre__contains='hill').values('nombre')
a1.union(e1)

# Obtener el cuarto libro con mas paginas
let3 = Libro.objects.values('isbn', 'paginas').order_by('-paginas')[3]

# Obtener el cuarto y quinto libro con mas paginas
let4 = Libro.objects.values('isbn', 'paginas').order_by('-paginas')[3:5]

# Usando la función podemos seleccionar por ejemplo la pagina 3
Libro.objects.LibroPorPaginas(3)  # pendiente

# Usando la función vamos a volver a seleccionar la pagina 3 , y veremos como obtenemos las mismas consultas sql que
# con la función que hicimos a mano, solo que en esta ocasión los cálculos los realizo Django por nosotros.
Libro.objects.LibroPorPaginasDjango(3) # pendiente

let5 = Libro.objects.filter(paginas__gte=200).explain

# Calcular cual es el numero minimo de paginas que puede tener un libro, en esta consulta no tomamos en cuenta
# los libros que no se especifico su numero de paginas por lo cual es 0 y este seria el mínimo numero de paginas.
resultado = Libro.objects.filter(paginas__gt=0).aggregate(Min('paginas'))

# Calcular cual es el numero máximo de paginas que puede tener un libro, aquí no necesitamos filtrar, este seria el
# máximo numero de paginas
Libro.objects.aggregate(Max('paginas'))

# Calcular cual es el numero medio de paginas que puede tener un libro, en esta consulta no tomamos en cuenta
# los libros que no se especifico su numero de paginas para así solo considerar los libros con paginas.
Libro.objects.filter(paginas__gt=0).aggregate(Avg('paginas'))

# Sumar el total de paginas de todos los libros que tenemos
Libro.objects.filter(categoria__icontains='python').aggregate(Sum('paginas'))

#  Agrupar los libros que son de Python por categoría y contar cuantos libros de cada categoría hay.
Libro.objects.filter(categoria__contains='python').values('categoria').annotate(NumeroLibros=Count('*'))

# Agrupar los libros que son de Python por categoría y por el nombre de la editorial y contar cuantos libros hay, a
# diferencia del ejemplo anterior en este ejemplo se involucran dos modelos Libro y Editorial, por lo que estamos
# hablando también de una union.
Libro.objects.filter(categoria__icontains='python').values('categoria', 'editorial__nombre').annotate(
  NumeroLibros=Count('*'))

# Para poder filtrar lo que agrupamos utilizamos filter solo que ahora utilizaremos alguna de las columnas que
# especificamos dentro de annotate, en este ejemplo agrupamos los libros por fecha_publicacion y filtramos solo
# las tengan mas de 5 libros publicados en esa fecha
Libro.objects.values('fecha_publicacion').annotate(cant_fec_pub=Count('fecha_publicacion')
                                                   ).filter(cant_fec_pub__gte=5)

# Si quisiéramos obtener el detalle de los libros de la consulta anterior podemos hacer lo siguiente
Consulta_fechas = Libro.objects.values('fecha_publicacion').annotate(cant_fec_pub=Count('fecha_publicacion')).filter(
  cant_fec_pub__gte=5).values_list('fecha_publicacion')

Libro.objects.filter(fecha_publicacion__in=consulta1).values('isbn')

# Devolver valores únicos de una para evitar ver valores duplicados, en este ejemplo usamos distinct sobre
# paginas ya que muchos libros tienen 0 paginas.
Libro.objects.values('paginas').filter(paginas__lt=200).distinct()

# Queremos que nuestra desc_corta solo muestre los primeros 15 caracteres
Libro.objects.annotate(desc_resumida=Left('desc_corta', 15)).values('isbn', 'desc_resumida')

# Queremos concatenar tres puntos (…) al fina de los valores de nuestra desc_resumida, para poder concatenar
# usamos la función Concat y para especificar la cadena a concatenar usamos Value.
Libro.objects.annotate(desc_resumida=Concat(Left('desc_corta', 15), V('...'))).values('isbn', 'desc_resumida')

# En el ejemplo anterior le pusimos los tres puntos (…) a todas las filas, en este ejemplo solo se los pondremos a
# las cadenas cuya longitud sea mayor de 15.
Libro.objects.annotate(longitud=Length('desc_corta')).annotate(
  desc_resumida=Case(
    When(longitud__gt=50,
         then=Concat(Left('desc_corta', 15), V('...')))
    ,
    default=('desc_corta'),
    output_field=CharField(),
  )).values('isbn', 'desc_resu mida', 'longitud')

# Queremos saber que libros tienen un titulo igual a su desc_corta dentro de sus primeros 50 caracteres, para
# especificar que lo que va a comparar es una columna del modelo y no una cadena de texto usamos
# F(nombre_columna)
Libro.objects.annotate(tit50=Left('titulo', 50), desc50=Left('desc_corta', 50)).filter(tit50=F('desc50')).values('isbn',
                                                                                                                 'tit50',
                                                                                                                 'desc50')

# Queremos quitarle las comillas a los nombres de nuestra categoría y remplazarlas por un *
Libro.objects.annotate(categoria_sin_comillas=Replace('categoria', V('"'), V('*'))).values('isbn', 'categoria',
                                                                                           'categoria_sin_comillas')

# Recuerda que no estamos afectando la base de datos solo estamos mostrando los datos, si quisieras afectar la
# base de datos y cambiar las comillas por * tendrías que hacer lo siguiente:
Libro.objects.filter(categoria='[]').update(categoria=Replace('categoria', V('"'), V('*')))

# En este ejemplo queremos las categorías que sean sobre Python o Java o net y que no tengan paginas igual a 0
Libro.objects.filter(
  (Q(categoria__contains='python') |
   Q(categoria__contains='java') |
   Q(categoria__contains='net')) & ~Q(paginas=0))

# La relación la podemos hacer directamente desde nuestro Libro usando el nombre de la tabla librocronica,
# nuestra consulta quedaría de esta manera:
Libro.objects.filter(librocronica__descripcion_larga__isnull=True).values('isbn', 'titulo',
                                                                          'librocronica__descripcion_larga')

# Existe otra forma de hacer la relacion uno a uno de Libro y LibroCronica y es usando select_related(modelo_relacion).
Libro.objects.select_related('librocronica').filter(categoria__contains='python')

# En el ejemplo anterior hicimos las consultas desde el modelo Libro, que pasaría si lo hiciéramos ahora desde el
# modelo, vamos a consultar primero nuestro modelo LibroCronica
let6 = LibroCronica.objects.all()[:3]

# Vamos a ver que pasa si utilizamos select_related
let6 = LibroCronica.objects.select_related('libro').all()[:3]

# Queremos consultar los libros cuya categoría sea Python y entonces imprimir el nombre de su editorial el cual se
# encuentra en el modelo Editoria, así que una primera forma de hacerlo seria la siguiente:
categorias = Libro.objects.all().filter(categoria__icontains='python')
for libro in categorias:
  print(libro.editorial.nombre)

# Vamos a realizar la consulta anterior pero ahora agregándole select_related especificándole que la relación es
# sobre el modelo editorial
categorias = Libro.objects.all().select_related('editorial').filter(categoria__icontains='python')
for libro in categorias:
  print(libro.editorial.nombre)

consulta = Libro.objects.all().select_related('editorial').filter(categoria__icontains
                                                                  ='python')
dic_libros = dict(consulta.values_list('isbn', 'editorial__nombre'))
print(dic_libros)

# En este ejemplo vamos a consultar 2 Autores y después vamos a buscar todos los libros que han escrito, como
# veremos esta forma no es optima debido a que primero realiza una consulta para traer los datos de los dos autores y a
# continuación realiza una consulta por cada autor dentro de la tabla de libros
autores = Autor.objects.filter(pk__in=(398, 523))
for autor in autores:
  print(f'Autor: {autor}')
  print('Libros escritos:')
  for libro in autor.libro.all():
    print(libro.titulo)

# Vamos a realizar la misma consulta anterior pero ahora usaremos el método prefetch_related para especificarle que
# Autor tiene una relación con libros, y como veremos ahora solo realizara 2 consultas no importa el numero de autores
# que consultemos
autores = Autor.objects.filter(pk__in=(398, 523)).prefetch_related('libro')
for autor in autores:
  print(f'Autor: {autor}')
  print('Libros escritos:')
  for libro in autor.libro.all():
    print(libro.titulo)

# Nuestro primer intento será consultar los Autores utilizando prefetch_related como lo vimos en el ejemplo
# anterior, así podemos listar cada uno de sus libros, pero ahora debemos mostrar el nombre de la editorial por cada uno
# de los libros
autores = Autor.objects.filter(pk__in=(398, 523)).prefetch_related('libro')
for autor in autores:
  print(f'Autor: {autor}')
  print('Libros escritos:')
  for libro in autor.libro.all():
    print(f'{libro.isbn} Editorial: {
libro.editorial.nombre}')

# Vamos a realizar la misma consulta que en el ejemplo anterior solo que esta vez en el prefetch_related le indicaremos
# que también existe una relación entre el libro y la editorial.
autores = Autor.objects.filter(pk__in=(398, 523)).prefetch_related('libro__editorial')

for autor in autores:
    print(f'Autor: {autor}')
    print('Libros escritos:')
    for libro in autor.libro.all():
        print(f'{libro.isbn} Editorial: {libro.editorial.nombre}')


# Existe una clase llamada Prefetch que podemos usar para controlar un poco mas las operaciones que va a
# realizar prefetch_related, en esta consulta utilizamos el método select_related que ya habíamos visto en las consultas
# uno a muchos y esta consulta se la especificamos dentro del Prefectch en su propiedad queryset.
libro_y_editorial = Libro.objects.select_related('editorial')
autores = Autor.objects.filter(pk__in=(398, 523)).prefetch_related(
    Prefetch('libro', queryset=libro_y_editorial)
)

for autor in autores:
    print(f'Autor: {autor}')
    print('Libros escritos:')
    for libro in autor.libro.all():
        print(f'{libro.isbn} Editorial: {libro.editorial.nombre}')

# Prefetch nos permite darle un nombre de atributo usando to_attr con lo cual en la consulta anterior podríamos
# usar este nombre, en este ejemplo pueden ver que no necesitamos llamar autor.libro.all() sino que llamamos
# autor.libaut, esto no modifica la consulta sql, es la misma del ejemplo anterior.
libro_y_editorial = Libro.objects.filter(titulo__contains='u').select_related('editorial')
autores = Autor.objects.filter(pk__in=(398, 523)).prefetch_related(
    Prefetch('libro', queryset=libro_y_editorial, to_attr='libaut')
)

for autor in autores:
    print(f'Autor: {autor}')
    print('Libros escritos:')
    for libro in autor.libaut:
        print(f'{libro.isbn} Editorial: {libro.editorial.nombre}')

# Para realizar esto hacemos uso del nombre que le pusimos a nuestra relación en related_name='libros_autores', en este
 # ejemplo consultamos algunos Libros y mostramos su Editorial y el Autor o Autores que los escribieron}
libros = Libro.objects.filter(
  isbn__in=('1234567898745', '1234567898747')
).select_related('editorial').prefetch_related('libro_autores__autor')

for p in libros:
  autores_nombres = [q.autor.nombre for q in p.libro_autores.all()]
  autores_str = ', '.join(autores_nombres)
  print(f'{p.isbn} - {p.titulo} - Editorial: {p.editorial.nombre} Escrito por: {autores_str}')
