from django.db import models


# Manager personalizado para el modelo Libro
class LibroManager(models.Manager):
  def buscar_por_isbn(self, isbn):
    try:
      return self.get(pk=isbn)
    except models.ObjectDoesNotExist:
      return f'No existe el libro con ISBN {isbn}'


# Modelo: Editorial
class Editorial(models.Model):
  nombre = models.CharField(max_length=100)

  class Meta:
    managed = True
    db_table = 'libreria_editorial'


# Modelo: Autor
class Autor(models.Model):
    nombre = models.CharField(max_length=70)


class Libro(models.Model):
  isbn = models.CharField(max_length=13, primary_key=True)
  titulo = models.CharField(max_length=70, blank=True)
  paginas = models.PositiveIntegerField()
  fecha_publicacion = models.DateField(null=True)
  imagen = models.URLField(max_length=85, null=True)
  desc_corta = models.CharField(max_length=2000)
  estatus = models.CharField(max_length=1)
  categoria = models.CharField(max_length=50)
  editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT, null=True, related_name='libros')

  objects = LibroManager()


class LibroAutor(models.Model):
  libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_autores')
  autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='autor_libros')


# Modelo: AutorCapitulo (relación Many-to-Many extendida con datos adicionales)
class AutorCapitulo(models.Model):
  autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
  libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True)
  numero_capitulos = models.IntegerField(default=0)

  class Meta:
    db_table = 'autor_capitulo'


# Modelo: LibroCronica (relación One-to-One con Libro)
class LibroCronica(models.Model):
  descripcion_larga = models.TextField(null=True)
  libro = models.OneToOneField(Libro, on_delete=models.CASCADE, primary_key=True)
