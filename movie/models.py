from django.db import models

# Create your models here.
#  Para esta entrega solo requerimos Dieta y Rutina para crearlas y mostrarlas en la página
#  En este modelo no se encuentran las tablas r_rutina y r_dieta, además usuario no se esta utilizando por ahora hasta que se pueda iniciar sesión
class Usuario(models.Model):
    Id_user = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length= 50)
    edad = models.SmallIntegerField()
    altura = models.SmallIntegerField()
    peso = models.SmallIntegerField()
    deporte = models.CharField(max_length= 40, blank = True)
    enfermedades = models.CharField(max_length= 100, blank = True)
    sexo = models.CharField(max_length=1, null=True)
    #correo = models.EmailField()

    def __str__(self):
        falta = "nombre: "+ self.nombre
        return falta

class Dieta(models.Model):
    Id_dieta = models.IntegerField(primary_key=True)
    nombre_dieta = models.CharField(max_length= 40)
    desc_dieta = models.CharField(max_length= 400)
    info_dieta1 = models.CharField(max_length= 750, null = True)
    info_dieta2 = models.CharField(max_length= 750, blank=True)
    info_dieta3 = models.CharField(max_length= 750, blank=True)
    recomendacion = models.CharField(max_length= 750, blank=True)
    duracion_dieta = models.SmallIntegerField(null=True)
    d_dieta = models.CharField(max_length= 3, blank = True) #este campo solo existe para poder acceder a cada dieta desde el catalogo
    
    def __str__(self):
        falta = "nombre_dieta: "+ self.nombre_dieta
        return falta

class Rutina(models.Model):
    Id_rutina = models.IntegerField(primary_key=True)
    nombre_rutina = models.CharField(max_length= 40)
    desc_rutina = models.CharField(max_length= 400)
    previo = models.CharField(max_length= 750, blank=True) #puede quitarse en un futuro porque es igual para todos
    info_rutina1 = models.CharField(max_length= 750, null = True)
    info_rutina2 = models.CharField(max_length= 750, blank=True)
    info_rutina3 = models.CharField(max_length= 750, blank=True)
    dificultad = models.SmallIntegerField(null=True)
    d_rutina = models.CharField(max_length= 3, blank = True) #este campo solo existe para poder acceder a cada rutina desde el catalogo

    def __str__(self):
        falta = "nombre_rutina: "+ self.nombre_rutina
        return falta

    #Se crean desde /admin

    #Notas:-----------------------------
    #null=True, blank=TruePuede ser null excepto a momento de crearla, igual en el otro orden
    #null=True, no permite datos nulos, blank=True si

#opciones_consulta = [
#    [0, "consulta"],
#    [1, "reclamo"],
#    [2, "sugerencia"],
#    [3, "felicitacion"]
#]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
#    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    tipo_consulta = models.CharField(max_length=20)
    mensaje = models.TextField()
#    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre

class Imc(models.Model):
    edad = models.SmallIntegerField()
    altura = models.SmallIntegerField()
    peso = models.SmallIntegerField()
    sexo = models.CharField(max_length=1)

    def _get_imc(self):
        return (self.peso)/((self.altura/100)*(self.altura/100))
    imc = property(_get_imc)