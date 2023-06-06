# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aprobadores(models.Model):
    idaprobadores = models.IntegerField(primary_key=True)
    nombreaprobador1 = models.CharField(max_length=45)
    nombreaprobador2 = models.CharField(max_length=45)
    fechadeaprobacion1 = models.DateTimeField()
    fechadeaprobacion2 = models.CharField(max_length=45)
    solicitante = models.CharField(max_length=45)
    correoaprob1 = models.CharField(max_length=45)
    correoaprob2 = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'aprobadores'


class AprobadoresHasSolicitudes(models.Model):
    aprobadores_idaprobadores = models.OneToOneField(Aprobadores, models.DO_NOTHING, db_column='aprobadores_idaprobadores', primary_key=True)  # The composite primary key (aprobadores_idaprobadores, solicitudes_idsolicitudes, solicitudes_usuarios_idusuario) found, that is not supported. The first column is selected.
    solicitudes_idsolicitudes = models.ForeignKey('Solicitudes', models.DO_NOTHING, db_column='solicitudes_idsolicitudes')
    solicitudes_usuarios_idusuario = models.ForeignKey('Solicitudes', models.DO_NOTHING, db_column='solicitudes_usuarios_idusuario', to_field='usuarios_idusuario', related_name='aprobadoreshassolicitudes_solicitudes_usuarios_idusuario_set')

    class Meta:
        managed = False
        db_table = 'aprobadores_has_solicitudes'
        unique_together = (('aprobadores_idaprobadores', 'solicitudes_idsolicitudes', 'solicitudes_usuarios_idusuario'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Solicitudes(models.Model):
    idsolicitudes = models.IntegerField(primary_key=True)  # The composite primary key (idsolicitudes, usuarios_idusuario) found, that is not supported. The first column is selected.
    fechasolicitud = models.DateTimeField()
    solicitante = models.CharField(max_length=45)
    tiposolicitud = models.CharField(max_length=45)
    descripcionsol = models.CharField(max_length=45)
    tecnico2 = models.CharField(max_length=45)
    responsabledeposito = models.CharField(max_length=45)
    actividad = models.CharField(max_length=45)
    departamento = models.CharField(max_length=45)
    municipio = models.CharField(max_length=45)
    diasviaticos = models.IntegerField()
    diashotel = models.IntegerField()
    asigespeciales = models.CharField(max_length=45, blank=True, null=True)
    valorasigespeciales = models.CharField(max_length=45, blank=True, null=True)
    estado = models.IntegerField()
    usuarios_idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usuarios_idusuario')

    class Meta:
        managed = False
        db_table = 'solicitudes'
        unique_together = (('idsolicitudes', 'usuarios_idusuario'),)


class Usuarios(models.Model):
    idusuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=45)
    rol = models.CharField(max_length=45)
    regional = models.CharField(max_length=45)
    cargo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'usuarios'
