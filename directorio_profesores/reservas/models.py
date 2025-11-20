from django.db import models


class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    ci= models.CharField(max_length=20,unique=True)
    fecha_registro = models.DateField()
    
    class Meta:
        managed = False
        db_table = 'alumno'
        
class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100,blank=True,null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        managed = False
        db_table = 'profesor'
        
class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nombre_materia = models.CharField(max_length=100)
    sigla = models.CharField(max_length=20)
    duracion = models.PositiveBigIntegerField()
    precio =  models.DecimalField(max_digits=10,decimal_places=2)
    profesor = models.ForeignKey(Profesor,on_delete=models.PROTECT,db_column='id_profesor',related_name='materias')
    
    class Meta:
        managed = False
        db_table = 'materia'
class ReservaClase(models.Model):
    ESTADOS = [
        ('pendiente','Pendiente'),
        ('confirmada','Confirmada'),
        ('cancelada','Cancelada'),
    ]
    id_reserva = models.AutoField(primary_key=True)
    fecha_reserva = models.DateField()
    estado = models.CharField(max_length=10,choices=ESTADOS,default='pendiente')
    requerimientos =models.CharField(max_length=100,blank=True,null=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE,db_column='id_alumno',related_name='alumno')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE,db_column='id_profesor',related_name='profesor')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE,db_column='id_materia',related_name='materia')
    
    class Meta:
        managed = False
        db_table = 'reserva_clase'