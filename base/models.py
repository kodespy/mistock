from django.db import models

from django.contrib.auth.models import User
import uuid






class ClaseModelo(models.Model):
	estado = models.BooleanField(default=True)
	fc = models.DateTimeField(auto_now_add=True)
	fm = models.DateTimeField(auto_now=True)
	uc = models.ForeignKey(User, on_delete=models.CASCADE)
	um = models.IntegerField(blank=True, null=True)

	class Meta:
		abstract = True	



class Empresa(ClaseModelo):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	documento = models.CharField(
		max_length = 20,
		help_text = 'RUC y/o CI N°',
		unique = True 
	)
	razonsocial = models.CharField(
		max_length = 100,
		help_text = 'Razón Social'
	)
	direccion = models.CharField(
		max_length = 200,
		help_text = 'Dirección',
		null=True, blank=True
	)	

	def __str__(self):
		return '{} : {}'.format(self.razonsocial, self.documento)

	def save(self):
		self.razonsocial = self.razonsocial.upper()
		self.direccion = self.direccion.upper()
		super(Empresa, self).save()

	class Meta:
		verbose_name_plural = "Empresas"	


class EmpresaUsuario(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)	
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)	

