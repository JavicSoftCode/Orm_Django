# Generated by Django 5.1.2 on 2024-10-23 02:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre del Cargo')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción del Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='CategoriaExamen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Categoría')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción de la Categoría')),
            ],
            options={
                'verbose_name': 'Categoría de Examen',
                'verbose_name_plural': 'Categorías de Exámenes',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True, verbose_name='Código del Diagnóstico')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción del Diagnóstico')),
                ('datos_adicionales', models.TextField(blank=True, null=True, verbose_name='Datos Adicionales')),
            ],
            options={
                'verbose_name': 'Diagnóstico',
                'verbose_name_plural': 'Diagnósticos',
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Especialidad')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción de la Especialidad')),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='MarcaMedicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Marca de Medicamento')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo de Medicamento',
                'verbose_name_plural': 'Tipos de Medicamentos',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Cédula')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('telefono', models.CharField(max_length=20, verbose_name='Teléfono(s)')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='Sexo')),
                ('estado_civil', models.CharField(choices=[('S', 'Soltero'), ('C', 'Casado'), ('U', 'Union Libre'), ('D', 'Divorciado'), ('V', 'Viudo')], max_length=10, verbose_name='Estado Civil')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección Domiciliaria')),
                ('latitud', models.DecimalField(blank=True, decimal_places=6, max_digits=18, null=True, verbose_name='Latitud')),
                ('longitud', models.DecimalField(blank=True, decimal_places=6, max_digits=18, null=True, verbose_name='Longitud')),
                ('alergias', models.CharField(blank=True, max_length=100, null=True, verbose_name='Alergias')),
                ('enfermedades_cronicas', models.CharField(blank=True, max_length=100, null=True, verbose_name='Enfermedades Crónicas')),
                ('medicacion_actual', models.CharField(blank=True, max_length=100, null=True, verbose_name='Medicación Actual')),
                ('cirugias_previas', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cirugías Previas')),
                ('antecedentes_personales', models.TextField(blank=True, null=True, verbose_name='Antecedentes Personales')),
                ('antecedentes_familiares', models.TextField(blank=True, null=True, verbose_name='Antecedentes Familiares')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['apellidos'],
            },
        ),
        migrations.CreateModel(
            name='ServiciosAdicionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(max_length=255, verbose_name='Nombre del Servicio')),
                ('costo_servicio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Costo del Servicio')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción del Servicio')),
            ],
            options={
                'verbose_name': 'Servicio Adicional',
                'verbose_name_plural': 'Servicios Adicionales',
                'ordering': ['nombre_servicio'],
            },
        ),
        migrations.CreateModel(
            name='TipoMedicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Tipo de Medicamento')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo de Medicamento',
                'verbose_name_plural': 'Tipos de Medicamentos',
            },
        ),
        migrations.CreateModel(
            name='TipoSangre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10, unique=True, verbose_name='Tipo de Sangre')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de Sangre',
                'verbose_name_plural': 'Tipos de Sangre',
            },
        ),
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_atencion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Atención')),
                ('motivo_consulta', models.TextField(verbose_name='Motivo de Consulta')),
                ('tratamiento', models.TextField(verbose_name='Tratamiento')),
                ('comentario', models.TextField(blank=True, null=True, verbose_name='Comentario')),
                ('diagnostico', models.ManyToManyField(related_name='diagnosticos_atencion', to='Orm.diagnostico', verbose_name='Diagnósticos')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='doctores_atencion', to='Orm.paciente', verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'Atención',
                'verbose_name_plural': 'Atenciones',
                'ordering': ['-fecha_atencion'],
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombre del Empleado')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellido del Empleado')),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Cédula')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Sueldo')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('latitud', models.FloatField(blank=True, null=True, verbose_name='Latitud')),
                ('longitud', models.FloatField(blank=True, null=True, verbose_name='Longitud')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='empleados/', verbose_name='Foto del Empleado')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cargos', to='Orm.cargo', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Cédula')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('direccion', models.CharField(max_length=10, unique=True, verbose_name='Direccion Trabajo')),
                ('latitud', models.DecimalField(blank=True, decimal_places=6, max_digits=18, null=True, verbose_name='Latitud')),
                ('longitud', models.DecimalField(blank=True, decimal_places=6, max_digits=18, null=True, verbose_name='Longitud')),
                ('codigoUnicoDoctor', models.CharField(max_length=20, unique=True, verbose_name='Código Único del Doctor')),
                ('telefonos', models.CharField(max_length=20, verbose_name='Teléfonos')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo')),
                ('horario_atencion', models.TextField(verbose_name='Horario de Atencion')),
                ('duracion_cita', models.IntegerField(default=30, verbose_name='Tiempo de Atencion(minutos)')),
                ('curriculum', models.FileField(blank=True, null=True, upload_to='curriculums/', verbose_name='Curriculum Vitae')),
                ('firmaDigital', models.ImageField(blank=True, null=True, upload_to='firmas/', verbose_name='Firma Digital')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='doctores/', verbose_name='Foto')),
                ('imagen_receta', models.ImageField(blank=True, null=True, upload_to='recetas/', verbose_name='Imagen para Recetas')),
                ('especialidad', models.ManyToManyField(related_name='especialidades', to='Orm.especialidad', verbose_name='Especialidades')),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctores',
            },
        ),
        migrations.CreateModel(
            name='HorarioAtencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miércoles', 'Miércoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sábado', 'Sábado'), ('domingo', 'Domingo')], max_length=10, unique=True, verbose_name='Día de la Semana')),
                ('hora_inicio', models.TimeField(verbose_name='Hora de Inicio')),
                ('hora_fin', models.TimeField(verbose_name='Hora de Fin')),
                ('Intervalo_desde', models.TimeField(verbose_name='Intervalo desde')),
                ('Intervalo_hasta', models.TimeField(verbose_name='Intervalo Hasta')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='doctores', to='Orm.doctor', verbose_name='Doctor')),
            ],
            options={
                'verbose_name': 'Horario de Atenciónl Doctor',
                'verbose_name_plural': 'Horarios de Atención de los Doctores',
            },
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Nombre del Medicamento')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción del Medicamento')),
                ('concentracion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Concentración del Medicamento')),
                ('cantidad', models.PositiveIntegerField(verbose_name='Stock')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('comercial', models.BooleanField(default=True, verbose_name='Comercial')),
                ('marca_medicamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='marca_medicamentos', to='Orm.marcamedicamento', verbose_name='Marca')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tipos_medicamentos', to='Orm.tipomedicamento', verbose_name='Tipo de Medicamento')),
            ],
            options={
                'verbose_name': 'Medicamento',
                'verbose_name_plural': 'Medicamentos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='DetalleAtencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('prescripcion', models.TextField(verbose_name='Prescripción')),
                ('duracion_tratamiento', models.PositiveIntegerField(blank=True, null=True, verbose_name='Duración del Tratamiento (días)')),
                ('atencion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atenciones', to='Orm.atencion', verbose_name='Cabecera de Atención')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicamentos', to='Orm.medicamento', verbose_name='Medicamento')),
            ],
            options={
                'verbose_name': 'Detalle de Atención',
                'verbose_name_plural': 'Detalles de Atención',
                'ordering': ['atencion'],
            },
        ),
        migrations.CreateModel(
            name='ExamenSolicitado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_examen', models.CharField(max_length=255, verbose_name='Nombre del Examen')),
                ('fecha_solicitud', models.DateField(auto_now_add=True, verbose_name='Fecha de Solicitud')),
                ('resultado', models.FileField(blank=True, null=True, upload_to='resultados_examenes/', verbose_name='Resultado del Examen')),
                ('comentario', models.TextField(blank=True, null=True, verbose_name='Comentario')),
                ('estado', models.CharField(choices=[('S', 'Solicitado'), ('R', 'Realizado')], max_length=20, verbose_name='Estado del Examen')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pacientes_examenes', to='Orm.paciente', verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'Examen Médico',
                'verbose_name_plural': 'Exámenes Médicos',
                'ordering': ['-fecha_solicitud'],
            },
        ),
        migrations.CreateModel(
            name='CostosAtencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Total')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')),
                ('atencion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='costos_atencion', to='Orm.atencion', verbose_name='Atención')),
                ('servicios_adicionales', models.ManyToManyField(blank=True, related_name='servicios_adicionales', to='Orm.serviciosadicionales', verbose_name='Servicios Adicionales')),
            ],
            options={
                'verbose_name': 'Costo de Atención',
                'verbose_name_plural': 'Costos de Atención',
                'ordering': ['-fecha_registro'],
            },
        ),
        migrations.CreateModel(
            name='TipoCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del Examen')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción del Examen')),
                ('valor_minimo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Valor Mínimo')),
                ('valor_maximo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Valor Máximo')),
                ('categoria_examen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorias_examen', to='Orm.categoriaexamen', verbose_name='Categoría del Examen')),
            ],
            options={
                'verbose_name': 'Tipo de Examen',
                'verbose_name_plural': 'Tipos de Exámenes',
                'ordering': ['categoria_examen', 'nombre'],
            },
        ),
        migrations.AddField(
            model_name='paciente',
            name='tipo_sangre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tipos_sangre', to='Orm.tiposangre', verbose_name='Tipo de Sangre'),
        ),
        migrations.CreateModel(
            name='CitaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de la Cita')),
                ('hora_cita', models.TimeField(verbose_name='Hora de la Cita')),
                ('estado', models.CharField(choices=[('P', 'Programada'), ('C', 'Cancelada'), ('R', 'Realizada')], max_length=1, verbose_name='Estado de la Cita')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctores_citas', to='Orm.doctor', verbose_name='Doctor')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pacientes_citas', to='Orm.paciente', verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'Cita Médica',
                'verbose_name_plural': 'Citas Médicas',
                'ordering': ['fecha', 'hora_cita'],
                'indexes': [models.Index(fields=['fecha', 'hora_cita'], name='idx_fecha_hora')],
            },
        ),
        migrations.AddIndex(
            model_name='paciente',
            index=models.Index(fields=['apellidos'], name='Orm_pacient_apellid_5c2f64_idx'),
        ),
    ]
