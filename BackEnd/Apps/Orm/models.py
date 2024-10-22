from django.db import models

from BackEnd.Apps.Orm.const import *

"""Modelo que representa los diferentes tipos de sangre.
Se gestiona como un modelo separado para mantener flexibilidad
y permitir futuras actualizaciones."""


class TipoSangre(models.Model):
  # almacena la descripcion del tipo de sangre
  tipo = models.CharField(max_length=10, verbose_name="Tipo de Sangre", unique=True)
  descripcion = models.CharField(max_length=100, verbose_name="Descripcion")

  class Meta:
    # Nombre en singular y plural del modelo en la interfaz de administración
    verbose_name = "Tipo de Sangre"
    verbose_name_plural = "Tipos de Sangre"

  def __str__(self):
    return self.tipo


""" Modelo que representa a los pacientes de la clínica. 
Almacena información personal, de contacto, ubicación y detalles médicos.
También incluye información completa de la historia clínica. """


class Paciente(models.Model):
  # Información personal
  # Nombre completo del paciente
  nombres = models.CharField(max_length=100, verbose_name="Nombres")
  apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
  # Cédula de identidad del paciente, debe ser única
  cedula = models.CharField(max_length=10, unique=True, verbose_name="Cédula")
  # Fecha de nacimiento del paciente
  fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
  # Número de teléfono de contacto del paciente
  telefono = models.CharField(max_length=20, verbose_name="Teléfono(s)")
  # Correo electrónico del paciente, puede ser nulo o estar vacío
  email = models.EmailField(verbose_name="Correo", null=True, blank=True)
  # Sexo del paciente (Masculino o Femenino)
  sexo = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name="Sexo")
  # Estado civil del paciente (Soltero, Casado, etc.)
  estado_civil = models.CharField(max_length=10, choices=CIVIL_CHOICES, verbose_name="Estado Civil")
  # Ubicación geográfica
  # Dirección domiciliaria del paciente
  direccion = models.CharField(max_length=255, verbose_name="Dirección Domiciliaria")
  # Latitud de la ubicación del paciente (coordenada geográfica)
  latitud = models.DecimalField(max_digits=18, decimal_places=6, verbose_name="Latitud", null=True, blank=True)
  # Longitud de la ubicación del paciente (coordenada geográfica)
  longitud = models.DecimalField(max_digits=18, decimal_places=6, verbose_name="Longitud", null=True, blank=True)
  # Historia clínica
  # Relación con el modelo TipoSangre, permite seleccionar el tipo de sangre del paciente
  tipo_sangre = models.ForeignKey(TipoSangre, on_delete=models.SET_NULL, null=True, verbose_name="Tipo de Sangre",
                                  related_name="tipos_sangre")
  # Alergias conocidas del paciente
  alergias = models.CharField(max_length=100, verbose_name="Alergias", null=True, blank=True)
  # Enfermedades crónicas que sufre el paciente
  enfermedades_cronicas = models.CharField(max_length=100, verbose_name="Enfermedades Crónicas", null=True, blank=True)
  # Medicación que el paciente toma de manera regular
  medicacion_actual = models.CharField(max_length=100, verbose_name="Medicación Actual", null=True, blank=True)
  # Cirugías que el paciente ha tenido previamente
  cirugias_previas = models.CharField(max_length=100, verbose_name="Cirugías Previas", null=True, blank=True)
  # Antecedentes médicos personales del paciente (enfermedades pasadas, hábitos, etc.)
  antecedentes_personales = models.TextField(verbose_name="Antecedentes Personales", null=True, blank=True)
  # Antecedentes médicos familiares del paciente (enfermedades hereditarias, condiciones genéticas)
  antecedentes_familiares = models.TextField(verbose_name="Antecedentes Familiares", null=True, blank=True)

  class Meta:
    # Define el orden predeterminado de los pacientes por nombre
    ordering = ['apellidos']
    indexes = [models.Index(fields=['apellidos'])]
    # Nombre en singular y plural del modelo en la interfaz de administración
    verbose_name = "Paciente"
    verbose_name_plural = "Pacientes"

  def nombre_completo(self):
    return f"{self.apellidos} {self.nombres}"

  def __str__(self):
    return self.nombres


"""
Modelo que representa las diferentes especialidades médicas.
Cada doctor puede tener una o varias especialidades.
"""


class Especialidad(models.Model):
  # Nombre de la especialidad médica (ej. Cardiología, Neurología, etc.)
  nombre = models.CharField(max_length=100, verbose_name="Nombre de la Especialidad")
  # Descripción de la especialidad (opcional)
  descripcion = models.TextField(verbose_name="Descripción de la Especialidad", null=True, blank=True)

  def __str__(self):
    return self.nombre

  class Meta:
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Especialidad"
    verbose_name_plural = "Especialidades"


# Modelo que representa a los doctores que trabajan en la clínica.
# Almacena información personal, profesional, y detalles importantes
# como su especialidad, curriculum y datos médicos adicionales.
class Doctor(models.Model):
  # Nombre del doctor
  nombres = models.CharField(max_length=100, verbose_name="Nombres")
  # Apellido del doctor
  apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
  # Cédula de identidad única del doctor
  cedula = models.CharField(max_length=10, unique=True, verbose_name="Cédula")
  # Fecha de nacimiento del doctor
  fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
  # Direccion del doctor
  direccion = models.CharField(max_length=10, unique=True, verbose_name="Direccion Trabajo")
  # Latitud de la ubicación del paciente (coordenada geográfica)
  latitud = models.DecimalField(max_digits=18, decimal_places=6, verbose_name="Latitud", null=True, blank=True)
  # Longitud de la ubicación del paciente (coordenada geográfica)
  longitud = models.DecimalField(max_digits=18, decimal_places=6, verbose_name="Longitud", null=True, blank=True)
  # Código único del doctor, utilizado para identificarlo internamente en la clínica
  codigoUnicoDoctor = models.CharField(max_length=20, unique=True, verbose_name="Código Único del Doctor")
  # Relación con el modelo Especialidad, permite asociar una o varias especialidades al doctor
  especialidad = models.ManyToManyField('Especialidad', verbose_name="Especialidades", related_name="especialidades")
  # Número de teléfono de contacto del doctor
  telefonos = models.CharField(max_length=20, verbose_name="Teléfonos")
  # Dirección de correo electrónico del doctor
  email = models.EmailField(verbose_name="Correo", null=True, blank=True)
  # Hora de inicio y fin de atención del doctor
  horario_atencion = models.TextField(verbose_name="Horario de Atencion")
  # tiempo de atencion en minutos
  duracion_cita = models.IntegerField(verbose_name="Tiempo de Atencion(minutos)", default=30)
  # Curriculum vitae del doctor en formato de archivo
  curriculum = models.FileField(upload_to='curriculums/', verbose_name="Curriculum Vitae", null=True, blank=True)
  # Firma digital del doctor (imagen o archivo)
  firmaDigital = models.ImageField(upload_to='firmas/', verbose_name="Firma Digital", null=True, blank=True)
  # Fotografía del doctor
  foto = models.ImageField(upload_to='doctores/', verbose_name="Foto", null=True, blank=True)
  # Imagen que se utilizará en las recetas firmadas por el doctor
  imagen_receta = models.ImageField(upload_to='recetas/', verbose_name="Imagen para Recetas", null=True, blank=True)

  def __str__(self):
    return f"{self.apellidos}"

  def nombre_completo(self):
    return f"{self.apellidos} {self.nombres}"

  class Meta:
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Doctor"
    verbose_name_plural = "Doctores"


# Modelo que representa los diferentes cargos que pueden tener los empleados en la clínica.
# Cada cargo puede tener un nombre y una descripción.
class Cargo(models.Model):
  # Nombre del cargo (ej. Médico, Enfermero, Administrador, etc.)
  nombre = models.CharField(max_length=100, verbose_name="Nombre del Cargo", unique=True)
  # Descripción del cargo (opcional)
  descripcion = models.TextField(verbose_name="Descripción del Cargo", null=True, blank=True)

  def __str__(self):
    return self.nombre

  class Meta:
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Cargo"
    verbose_name_plural = "Cargos"


# Modelo que representa a los empleados que trabajan en la clínica.
# Incluye información personal, profesional y datos de contacto.
class Empleado(models.Model):
  # Nombre del empleado
  nombres = models.CharField(max_length=100, verbose_name="Nombre del Empleado")
  # Apellido del empleado
  apellidos = models.CharField(max_length=100, verbose_name="Apellido del Empleado")
  # Cédula de identidad única del empleado
  cedula = models.CharField(max_length=10, unique=True, verbose_name="Cédula")
  # Fecha de nacimiento del empleado
  fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
  # Relación con el modelo Cargo, permite asociar un cargo específico al empleado
  cargo = models.ForeignKey('Cargo', on_delete=models.PROTECT, verbose_name="Cargo", related_name="cargos")
  # Sueldo del empleado
  sueldo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Sueldo")
  # Dirección de residencia del empleado
  direccion = models.CharField(max_length=255, verbose_name="Dirección")
  # Latitud para la ubicación de la residencia del empleado
  latitud = models.FloatField(verbose_name="Latitud", null=True, blank=True)
  # Longitud para la ubicación de la residencia del empleado
  longitud = models.FloatField(verbose_name="Longitud", null=True, blank=True)
  # Fotografía del empleado
  foto = models.ImageField(upload_to='empleados/', verbose_name="Foto del Empleado", null=True, blank=True)

  def __str__(self):
    return f"{self.apellidos}"

  def nombre_completo(self):
    return f"{self.apellidos} {self.nombres}"

  class Meta:
    # Ordena los empleados alfabéticamente por apellido y nombre
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Empleado"
    verbose_name_plural = "Empleados"


# Modelo que representa los diferentes tipos de medicamentos disponibles.
# Cada tipo de medicamento puede tener un nombre y una descripción.
class TipoMedicamento(models.Model):
  # Nombre del tipo de medicamento (ej. Analgésico, Antibiótico, etc.)
  nombre = models.CharField(max_length=100, verbose_name="Tipo de Medicamento", unique=True)
  # Descripción del tipo de medicamento (opcional)
  descripcion = models.TextField(verbose_name="Descripción", null=True, blank=True)

  def __str__(self):
    return self.nombre

  class Meta:
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Tipo de Medicamento"
    verbose_name_plural = "Tipos de Medicamentos"


class MarcaMedicamento(models.Model):
  # Nombre del tipo de medicamento (ej. Analgésico, Antibiótico, etc.)
  nombre = models.CharField(max_length=100, verbose_name="Marca de Medicamento", unique=True)
  # Descripción del tipo de medicamento (opcional)
  descripcion = models.TextField(verbose_name="Descripción", null=True, blank=True)

  def __str__(self):
    return self.nombre

  class Meta:
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Tipo de Medicamento"
    verbose_name_plural = "Tipos de Medicamentos"


# Modelo que representa los medicamentos que están disponibles en la clínica.
# Incluye información sobre el nombre, tipo, y detalles adicionales del medicamento.
class Medicamento(models.Model):
  # tipo de medicamento
  tipo = models.ForeignKey('TipoMedicamento', on_delete=models.PROTECT, verbose_name="Tipo de Medicamento",
                           related_name="tipos_medicamentos")
  marca_medicamento = models.ForeignKey(MarcaMedicamento, on_delete=models.PROTECT, verbose_name="Marca",
                                        related_name="marca_medicamentos", null=True, blank=True)
  # Descripción del medicamento (opcional)
  nombre = models.CharField(max_length=100, verbose_name="Nombre del Medicamento", db_index=True, unique=True)
  # Descripción del medicamento (opcional)
  descripcion = models.TextField(verbose_name="Descripción del Medicamento", null=True, blank=True)
  # concentracion del medicamento
  concentracion = models.CharField(max_length=50, verbose_name="Concentración del Medicamento", null=True, blank=True)
  # Cantidad disponible del medicamento en inventario
  cantidad = models.PositiveIntegerField(verbose_name="Stock")
  # Precio del medicamento
  precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
  # Campo que indica si el medicamento es genérico o comercial
  comercial = models.BooleanField(default=True,
                                  verbose_name="Comercial"
                                  )

  def __str__(self):
    return f"{self.nombre} - ({self.tipo})"

  class Meta:
    # Ordena los medicamentos alfabéticamente por nombre
    ordering = ['nombre']
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Medicamento"
    verbose_name_plural = "Medicamentos"


# Modelo que representa los diagnósticos médicos.
# Incluye un código único, descripción y un campo adicional para información relevante.
class Diagnostico(models.Model):
  # Código único del diagnóstico (ej. CIE-10, ICD-10, etc.)
  codigo = models.CharField(max_length=20, unique=True, verbose_name="Código del Diagnóstico")
  # Descripción detallada del diagnóstico
  descripcion = models.CharField(max_length=100, verbose_name="Descripción del Diagnóstico")
  # Campo adicional para información relevante sobre el diagnóstico (opcional)
  datos_adicionales = models.TextField(verbose_name="Datos Adicionales", null=True, blank=True)

  def __str__(self):
    return f"{self.codigo} - {self.descripcion}"

  class Meta:
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Diagnóstico"
    verbose_name_plural = "Diagnósticos"


# Modelo que representa una categoría de exámenes.
# Agrupa varios tipos de exámenes bajo una misma categoría (ej. Sangre, Orina, Colesterol).
class CategoriaExamen(models.Model):
  # Nombre de la categoría (ej. Sangre, Orina, Colesterol)
  nombre = models.CharField(max_length=100, verbose_name="Nombre de la Categoría")
  # Descripción opcional de la categoría
  descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción de la Categoría")

  def __str__(self):
    return self.nombre

  class Meta:
    # Ordena las categorías por nombre
    ordering = ['nombre']
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Categoría de Examen"
    verbose_name_plural = "Categorías de Exámenes"


# Modelo que representa un tipo de examen médico.
# Cada examen está asociado a una categoría (ej. Sangre, Orina, Colesterol)
# y tiene valores mínimos y máximos de referencia.
class TipoCategoria(models.Model):
  # Relación con la categoría del examen (ej. Sangre, Orina, etc.)
  categoria_examen = models.ForeignKey('CategoriaExamen', on_delete=models.CASCADE, verbose_name="Categoría del Examen",
                                       related_name="categorias_examen")
  # Nombre del tipo de examen (ej. Colesterol, Hemoglobina, Glucosa)
  nombre = models.CharField(max_length=255, verbose_name="Nombre del Examen")
  # Descripción opcional del examen, con información adicional si aplica
  descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción del Examen")
  # Valor mínimo de referencia para este tipo de examen (ej. 70 mg/dL para glucosa)
  valor_minimo = models.CharField(max_length=100, null=True, blank=True, verbose_name="Valor Mínimo")
  # Valor máximo de referencia para este tipo de examen (ej. 100 mg/dL para glucosa)
  valor_maximo = models.CharField(max_length=100, null=True, blank=True, verbose_name="Valor Máximo")

  def __str__(self):
    return f"{self.categoria_examen} - {self.nombre}"

  class Meta:
    # Ordena los tipos de examen por categoría y nombre
    ordering = ['categoria_examen', 'nombre']
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Tipo de Examen"
    verbose_name_plural = "Tipos de Exámenes"


# Modelo que representa los días y horas de atención de un doctor.
# Incluye los días de la semana, la hora de inicio y la hora de fin de la atención.
class HorarioAtencion(models.Model):
  # Relación con el modelo Doctor, indica qué doctor está disponible en este horario
  doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, verbose_name="Doctor", related_name="doctores")
  # Días de la semana en los que el doctor atiende
  dia_semana = models.CharField(max_length=10, choices=DIA_SEMANA_CHOICES, verbose_name="Día de la Semana", unique=True)
  # Hora de inicio de atención del doctor
  hora_inicio = models.TimeField(verbose_name="Hora de Inicio")
  # Hora de fin de atención del doctor
  hora_fin = models.TimeField(verbose_name="Hora de Fin")
  # Inicio de descanso de atención del doctor
  Intervalo_desde = models.TimeField(verbose_name="Intervalo desde")
  # Fin de descanso de atención del doctor
  Intervalo_hasta = models.TimeField(verbose_name="Intervalo Hasta")

  def __str__(self):
    return f"{self.doctor} - {self.dia_semana}"

  class Meta:
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Horario de Atenciónl Doctor"
    verbose_name_plural = "Horarios de Atención de los Doctores"


# modelo que almacena los datos de la cita de los pacientes
class CitaMedica(models.Model):
  # Relación con el modelo Doctor, indica qué doctor verá al paciente en la cita
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Doctor", related_name="doctores_citas")
  # Relación con el modelo Paciente, indica qué paciente ha reservado la cita
  paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente",
                               related_name="pacientes_citas")
  # Fecha de la cita médica
  fecha = models.DateField(verbose_name="Fecha de la Cita")
  # Hora de la cita médica
  hora_cita = models.TimeField(verbose_name="Hora de la Cita")
  # Estado de la cita (ej. Programada, Cancelada, Realizada)
  estado = models.CharField(
    max_length=1,
    choices=CITA_CHOICES,
    verbose_name="Estado de la Cita"
  )

  def __str__(self):
    return f"Cita {self.paciente} con {self.doctor} el {self.fecha} a las {self.hora_cita}"

  class Meta:
    # Ordena las citas por fecha y hora
    ordering = ['fecha', 'hora_cita']
    indexes = [
      models.Index(fields=['fecha', 'hora_cita'], name='idx_fecha_hora'),
    ]
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Cita Médica"
    verbose_name_plural = "Citas Médicas"


# Modelo que representa la cabecera de una atención médica.
# Contiene la información general del paciente, diagnóstico, motivo de consulta y tratamiento.
class Atencion(models.Model):
  # Relación con el modelo Paciente, identifica al paciente que recibe la atención médica
  paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, verbose_name="Paciente",
                               related_name="doctores_atencion")
  # Fecha en la que se realizó la atención médica
  fecha_atencion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Atención")
  # Relación con el modelo Diagnóstico, permite asociar uno o varios diagnósticos a la atención médica
  diagnostico = models.ManyToManyField(Diagnostico, verbose_name="Diagnósticos", related_name="diagnosticos_atencion")
  # Motivo por el cual el paciente acudió a consulta
  motivo_consulta = models.TextField(verbose_name="Motivo de Consulta")
  # Tratamiento o recomendaciones dadas al paciente
  tratamiento = models.TextField(verbose_name="Tratamiento")
  # Comentarios adicionales del doctor sobre la atención o el estado del paciente
  comentario = models.TextField(null=True, blank=True, verbose_name="Comentario")

  def __str__(self):
    return f"Atención de {self.paciente} el {self.fecha_atencion}"

  class Meta:
    # Ordena las atenciones por fecha de forma descendente
    ordering = ['-fecha_atencion']
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Atención"
    verbose_name_plural = "Atenciones"


# Modelo que representa el detalle de una atención médica.
# Relaciona cada atención con los medicamentos recetados y su cantidad.
class DetalleAtencion(models.Model):
  # Relación con el modelo CabeceraAtencion, indica a qué atención pertenece este detalle
  atencion = models.ForeignKey(Atencion, on_delete=models.CASCADE, verbose_name="Cabecera de Atención",
                               related_name="atenciones")
  # Relación con el modelo Medicamento, indica qué medicamento fue recetado en esta atención
  medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, verbose_name="Medicamento",
                                  related_name="medicamentos")

  # Cantidad de medicamento recetado
  cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
  # Prescripción o indicaciones sobre cómo tomar el medicamento
  prescripcion = models.TextField(verbose_name="Prescripción")
  # Campo adicional: duración del tratamiento con el medicamento (en días)
  duracion_tratamiento = models.PositiveIntegerField(verbose_name="Duración del Tratamiento (días)", null=True,
                                                     blank=True)

  def __str__(self):
    return f"Detalle de {self.medicamento} para {self.atencion}"

  class Meta:
    # Ordena los detalles por cabecera de atención
    ordering = ['atencion']
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Detalle de Atención"
    verbose_name_plural = "Detalles de Atención"


# Modelo que representa los exámenes médicos solicitados durante una atención.
# Permite registrar los exámenes solicitados, su estado y resultados.
class ExamenSolicitado(models.Model):
  # Nombre o tipo de examen solicitado (ej. Hemograma, Radiografía, etc.)
  nombre_examen = models.CharField(max_length=255, verbose_name="Nombre del Examen")
  # Relación con el modelo Paciente, identifica al paciente que recibe la atención médica
  paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, verbose_name="Paciente",
                               related_name="pacientes_examenes")
  # Fecha en la que se solicitó el examen
  fecha_solicitud = models.DateField(auto_now_add=True, verbose_name="Fecha de Solicitud")
  # Campo adicional: archivo para subir el resultado del examen (opcional)
  resultado = models.FileField(upload_to='resultados_examenes/', null=True, blank=True,
                               verbose_name="Resultado del Examen")
  # Comentarios adicionales sobre el examen, si es necesario
  comentario = models.TextField(null=True, blank=True, verbose_name="Comentario")
  # Estado del examen (ej. Pendiente, En Proceso, Completado)
  estado = models.CharField(
    max_length=20,
    choices=EXAMEN_CHOICES,
    verbose_name="Estado del Examen"
  )

  def __str__(self):
    return f"Examen {self.nombre_examen}"

  class Meta:
    # Ordena los exámenes por fecha de solicitud
    ordering = ['-fecha_solicitud']

    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Examen Médico"
    verbose_name_plural = "Exámenes Médicos"


# Modelo que representa un servicio adicional ofrecido durante una atención médica.
# Puede incluir exámenes, procedimientos, o cualquier otro servicio.
class ServiciosAdicionales(models.Model):
  # Nombre del servicio (ej. Radiografía, Laboratorio, Procedimiento menor, etc.)
  nombre_servicio = models.CharField(max_length=255, verbose_name="Nombre del Servicio")
  # Costo unitario del servicio adicional
  costo_servicio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo del Servicio")
  # Descripción opcional sobre el servicio adicional
  descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción del Servicio")

  def __str__(self):
    return self.nombre_servicio

  class Meta:
    # Ordena los servicios por nombre
    ordering = ['nombre_servicio']
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Servicio Adicional"
    verbose_name_plural = "Servicios Adicionales"


# Modelo que representa los costos asociados a una atención médica,
# incluyendo consulta, servicios adicionales (exámenes, procedimientos), y otros costos.
class CostosAtencion(models.Model):
  # Relación con el modelo CabeceraAtencion, indica a qué atención médica pertenece el costo
  atencion = models.ForeignKey(Atencion, on_delete=models.PROTECT, verbose_name="Atención",
                               related_name="costos_atencion")
  # Relación ManyToMany con los servicios adicionales utilizados durante la atención
  servicios_adicionales = models.ManyToManyField(ServiciosAdicionales, blank=True, verbose_name="Servicios Adicionales",
                                                 related_name="servicios_adicionales")
  # Total de los costos calculado
  total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total", default=0.00)
  # Fecha en que se registraron los costos
  fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

  def __str__(self):
    return f"Costos para {self.atencion} - Total: {self.total}"

  class Meta:
    # Ordena los costos por fecha de registro
    ordering = ['-fecha_registro']
    # Nombre singular y plural del modelo en la interfaz administrativa
    verbose_name = "Costo de Atención"
    verbose_name_plural = "Costos de Atención"
