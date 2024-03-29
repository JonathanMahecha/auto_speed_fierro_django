# Generated by Django 5.0.2 on 2024-03-15 00:17

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('garantias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headLine', models.CharField(max_length=30, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'db_table': 'comment',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('contact', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='El número de contacto debe tener 10 dígitos numéricos', regex='^[0-9]{10}$')], verbose_name='Número de celular')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
                'db_table': 'contacts',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='imagen', verbose_name='Imagen_servicio')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'db_table': 'servicio',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='cite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50, verbose_name='Nombre del cliente')),
                ('client_email', models.EmailField(max_length=254, verbose_name='Email del cliente')),
                ('client_id', models.IntegerField(verbose_name='Identificación del cliente')),
                ('brand', models.CharField(choices=[('Toyota', 'Toyota'), ('Ford', 'Ford'), ('Volkswagen', 'Volkswagen'), ('BMW', 'BMW (Bayerische Motoren Werke)'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Honda', 'Honda'), ('Chevrolet', 'Chevrolet'), ('Audi', 'Audi'), ('Nissan', 'Nissan'), ('Tesla', 'Tesla'), ('Hyundai', 'Hyundai'), ('Kia', 'Kia'), ('Subaru', 'Subaru'), ('Porsche', 'Porsche'), ('Fiat', 'Fiat'), ('Mazda', 'Mazda'), ('Volvo', 'Volvo'), ('Jaguar', 'Jaguar'), ('Land Rover', 'Land Rover'), ('Jeep', 'Jeep'), ('Renault', 'Renault'), ('Suzuki', 'Suzuki'), ('Mitsubishi', 'Mitsubishi'), ('Peugeot', 'Peugeot'), ('Citroën', 'Citroën'), ('Chery', 'Chery'), ('Great Wall Motors', 'Great Wall Motors'), ('BYD', 'BYD'), ('Geely', 'Geely'), ('JAC Motors', 'JAC Motors'), ('Dongfeng', 'Dongfeng'), ('Tata Motors', 'Tata Motors'), ('Mahindra', 'Mahindra'), ('SsangYong', 'SsangYong'), ('Isuzu', 'Isuzu'), ('Zotye', 'Zotye'), ('Foton', 'Foton'), ('Mini', 'Mini'), ('Alfa Romeo', 'Alfa Romeo'), ('MG', 'MG'), ('Lada', 'Lada'), ('Haima', 'Haima'), ('GAC Motors', 'GAC Motors'), ('BAIC', 'BAIC'), ('Haval', 'Haval'), ('Wuling', 'Wuling'), ('DS Automobiles', 'DS Automobiles'), ('Proton', 'Proton'), ('Perodua', 'Perodua'), ('Changan', 'Changan'), ('Hawtai', 'Hawtai'), ('FAW', 'FAW'), ('SAIC Motor', 'SAIC Motor'), ('Roewe', 'Roewe'), ('Soueast Motors', 'Soueast Motors'), ('VinFast', 'VinFast'), ("Chang'an", "Chang'an"), ('Lifan', 'Lifan')], max_length=50, verbose_name='Marca del vehiculo')),
                ('model', models.CharField(max_length=50, verbose_name='Modelo del vehiculo')),
                ('year', models.PositiveIntegerField(verbose_name='Año del vehiculo')),
                ('color', models.CharField(choices=[('Blanco', 'Blanco'), ('Negro', 'Negro'), ('Gris', 'Gris'), ('Azul', 'Azul'), ('Rojo', 'Rojo'), ('Verde', 'Verde'), ('Amarillo', 'Amarillo'), ('Naranja', 'Naranja'), ('Marrón', 'Marrón'), ('Beige', 'Beige'), ('Rosa', 'Rosa'), ('Morado', 'Morado'), ('Turquesa', 'Turquesa'), ('Celeste', 'Celeste'), ('Plateado', 'Plateado'), ('Dorado', 'Dorado'), ('Crema', 'Crema'), ('Verde oliva', 'Verde oliva'), ('Azul marino', 'Azul marino'), ('Violeta', 'Violeta'), ('Cian', 'Cian'), ('Magenta', 'Magenta'), ('Lavanda', 'Lavanda'), ('Aguamarina', 'Aguamarina'), ('Coral', 'Coral'), ('Marfil', 'Marfil'), ('Esmeralda', 'Esmeralda'), ('Índigo', 'Índigo'), ('Melocotón', 'Melocotón'), ('Borgoña', 'Borgoña'), ('Lima', 'Lima'), ('Teal', 'Teal'), ('Amaranto', 'Amaranto'), ('Gris perla', 'Gris perla'), ('Fucsia', 'Fucsia'), ('Menta', 'Menta'), ('Ocre', 'Ocre'), ('Caqui', 'Caqui'), ('Ámbar', 'Ámbar'), ('Carmesí', 'Carmesí'), ('Púrpura', 'Púrpura'), ('Rubí', 'Rubí'), ('Gris pizarra', 'Gris pizarra'), ('Ónice', 'Ónice'), ('Mauve', 'Mauve'), ('Lima oscuro', 'Lima oscuro')], max_length=50, verbose_name='Color del vehículo')),
                ('plate_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='La placa debe tener el formato correcto: tres letras seguidas de tres números.', regex='^[A-Za-z]{3}\\d{3}$')], verbose_name='Número de placa')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Detalles del vehículo')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('estado', models.CharField(choices=[('En espera', 'En espera'), ('En proceso', 'En proceso'), ('Re agendada', 'Re agendada'), ('Ausente', 'Ausente'), ('Finalizada', 'Finalizada')], max_length=50, null=True, verbose_name='Estado de cita')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garantias.serviciocongarantia')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
                'db_table': 'cite',
                'ordering': ['id'],
            },
        ),
    ]
