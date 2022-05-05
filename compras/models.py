
from django.db import models
from django.db.models import ManyToManyField, Model, OneToOneField


#from inv.models import Moneda
from base.models import ClaseModelo



class Proveedor(ClaseModelo):
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
	contacto = models.CharField(
		max_length = 100,
		help_text = 'Contacto',
	)
	telefono = models.CharField(
		max_length = 10,
		help_text = 'Teléfono',
		null=True, blank=True
	)
	email = models.CharField(
		max_length = 250,
		help_text = 'Teléfono',
		null=True, blank=True
	)
	
	def __str__(self):
		return '{} : {}'.format(self.razonsocial, self.documento)

	def save(self):
		self.razonsocial = self.razonsocial.upper()
		self.direccion = self.direccion.upper()
		self.contacto = self.contacto.upper()
		super(Proveedor, self).save()

	class Meta:
		verbose_name_plural = "Proveedores"	


class Compras(ClaseModelo):
	TIPO = (
       (1, 'Contado'),
       (2, 'Créditos'),
   	)

	factura_numero = models.CharField(
		max_length = 20,
		help_text = 'Factura N°'
	)
	factura_fecha = models.DateField()
	factura_tipo = models.PositiveSmallIntegerField(
       choices=TIPO,default=1)
	factura_total = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	moneda = models.OneToOneField('inv.Moneda', on_delete=models.CASCADE, related_name="moneda_id")

	def __str__(self):
		return '{}'.format(self.id)

	def save(self):
		#self.razonsocial = self.razonsocial.upper()
		#self.direccion = self.direccion.upper()
		#self.contacto = self.contacto.upper()
		super(Compras, self).save()

	class Meta:
		verbose_name_plural = "Compras"	


class ComprasDetalle(ClaseModelo):
	IVA = (
       (1, 0),
       (2, 5),
       (3, 10),
   	)
	compras = models.ForeignKey(Compras, on_delete=models.CASCADE)
	producto = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	cantidad = models.DecimalField(default=0, max_digits=6, decimal_places=2)
	iva_valor = models.DecimalField(default=3, choices=IVA, max_digits=4, decimal_places=2)
	precio_costo = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	precio_venta = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	total_iva = models.DecimalField(default=0, max_digits=12, decimal_places=2)
	subtotal = models.DecimalField(default=0, max_digits=12, decimal_places=2)

	def __str__(self):
		return '{}'.format(self.id)

	def save(self):
		#self.razonsocial = self.razonsocial.upper()
		#self.direccion = self.direccion.upper()
		self.subtotal = (self.precio_costo * self.cantidad)
		super(ComprasDetalle, self).save()

	class Meta:
		verbose_name_plural = "ComprasDetalles"	

