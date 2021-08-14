# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Hospital(models.Model):
    idhospital = models.AutoField(primary_key=True)
    nomehospital = models.CharField(db_column='nomeHospital', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cnpj = models.IntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=45, blank=True, null=True)
    capacidademaxima = models.IntegerField(db_column='capacidadeMaxima', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hospital'


class Leito(models.Model):
    idleito = models.AutoField(db_column='idLeito', primary_key=True)  # Field name made lowercase.
    tempodelimpeza = models.TimeField(db_column='tempoDeLimpeza', blank=True, null=True)  # Field name made lowercase.
    especializacao = models.IntegerField(blank=True, null=True)
    hospital_idhospital = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='hospital_idhospital')

    class Meta:
        managed = False
        db_table = 'leito'
        unique_together = (('idleito', 'hospital_idhospital'),)


class Medico(models.Model):
    idmedico = models.AutoField(db_column='idMedico', primary_key=True)  # Field name made lowercase.
    nomemedico = models.CharField(db_column='nomeMedico', max_length=45, blank=True, null=True)  # Field name made lowercase.
    crm = models.IntegerField(blank=True, null=True)
    especialidade = models.CharField(max_length=45, blank=True, null=True)
    hospital_idhospital = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='hospital_idhospital')

    class Meta:
        managed = False
        db_table = 'medico'
        unique_together = (('idmedico', 'hospital_idhospital'),)


class Paciente(models.Model):
    idpaciente = models.AutoField(db_column='idPaciente', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=45, blank=True, null=True)
    cpf = models.CharField(db_column='CPF', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rg = models.CharField(db_column='RG', max_length=45, blank=True, null=True)  # Field name made lowercase.
    convenio = models.IntegerField(blank=True, null=True)
    datanascimento = models.DateField(db_column='dataNascimento', blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'


class PacienteHasLeito(models.Model):
    paciente_idpaciente = models.OneToOneField(Paciente, models.DO_NOTHING, db_column='Paciente_idPaciente', primary_key=True)  # Field name made lowercase.
    leito_idleito = models.ForeignKey(Leito, models.DO_NOTHING, db_column='Leito_idLeito')  # Field name made lowercase.
    leito_hospital_idhospital = models.ForeignKey(Leito, models.DO_NOTHING, db_column='Leito_hospital_idhospital', related_name='+')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paciente_has_leito'
        unique_together = (('paciente_idpaciente', 'leito_idleito', 'leito_hospital_idhospital'),)


class PacienteHasMedico(models.Model):
    paciente_idpaciente = models.OneToOneField(Paciente, models.DO_NOTHING, db_column='Paciente_idPaciente', primary_key=True)  # Field name made lowercase.
    medico_idmedico = models.ForeignKey(Medico, models.DO_NOTHING, db_column='Medico_idMedico')  # Field name made lowercase.
    medico_hospital_idhospital = models.ForeignKey(Medico, models.DO_NOTHING, db_column='Medico_hospital_idhospital', related_name='+')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paciente_has_medico'
        unique_together = (('paciente_idpaciente', 'medico_idmedico', 'medico_hospital_idhospital'),)
