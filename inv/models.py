from django.db import models
from django.core.validators import RegexValidator




from base.models import ClaseModelo
from compras.models import Proveedor


numerico = RegexValidator(r'^[0-9+]', 'Only digit characters.')

class Moneda(ClaseModelo):
	descripcion = models.CharField(
		max_length = 30,
		help_text = 'Descripción de la Marca',
		unique = True 
	)
	simbolo = models.CharField(
		max_length = 3,
		help_text = 'Simbolo de la Moneda',
		unique = True 
	)
	compras = models.IntegerField(
		help_text = 'Valor de compras',
		default = 0,
		validators=[numerico] 
	)
	ventas = models.IntegerField(
		help_text = 'Valor de ventas',
		default = 0, 
		validators=[numerico] 
	)
	maestra = models.BooleanField(
		help_text = 'Moneda Maestra',
		default = False
	)

	def __str__(self):
		return '{} : {}'.format(self.descripcion, self.simbolo)

	def save(self):
		self.descripcion = self.descripcion.upper()
		self.simbolo = self.simbolo.upper()
		super(Moneda, self).save()

	class Meta:
		verbose_name_plural = "Monedas"	


class Marca(ClaseModelo):
	descripcion = models.CharField(
		max_length = 30,
		help_text = 'Descripción de la Marca',
		unique = True 
	)

	def __str__(self):
		return '{}'.format(self.descripcion)

	def save(self):
		self.descripcion = self.descripcion.upper()
		super(Marca, self).save()

	class Meta:
		verbose_name_plural = "Marcas"	

class Categoria(ClaseModelo):
	descripcion = models.CharField(
		max_length = 100,
		help_text = 'Descripción de la Categoria',
		unique = True 
	)

	def __str__(self):
		return '{}'.format(self.descripcion)

	def save(self):
		self.descripcion = self.descripcion.upper()
		super(Categoria, self).save()

	class Meta:
		verbose_name_plural = "Categorias"		


class SubCategoria(ClaseModelo):
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	descripcion = models.CharField(
		max_length = 100,
		help_text = 'Descripción de la Sub Categoria'
	)

	def __str__(self):
		return '{} : {}'.format(self.descripcion, self.categoria.descripcion)

	def save(self):
		self.descripcion = self.descripcion.upper()
		super(SubCategoria, self).save()

	class Meta:
		verbose_name_plural = "Sub Categorias"		
		unique_together = ('categoria', 'descripcion')


class Producto(ClaseModelo):
	codigo_barra = models.CharField(
		max_length = 50,
		help_text = 'Código de Barra',
		unique = True 
	)	
	descripcion = models.CharField(
		max_length = 200,
		help_text = 'Descripción del producto',
	)
	imagen = models.ImageField(
		help_text = 'Imagen',
		upload_to = 'fotos/',
		null = True, blank = True 

	)
	detalle = models.CharField(
		max_length = 250,
		help_text = 'Detalle',
		null = True, blank = True 
	)
	unidad = models.CharField(
		max_length = 3,
		help_text = 'Unidad de Medidas',
	)	
	existencia_inicial = models.FloatField(
		help_text = 'Existencia Inicial',
		default = 0 
	)
	existencia_actual = models.FloatField(
		help_text = 'Existencia Actual',
		default = 0,
		null = True, blank = True 
	)	
	precio_costo = models.FloatField(
		help_text = 'Precio Costo',
		default = 0 
	)
	precio_venta = models.FloatField(
		help_text = 'Precio Venta',
		default = 0 
	)	
	descuento_maximo = models.FloatField(
		help_text = 'Descuentos Máximo',
		default = 0 
	)	
	incremento_precio_credito = models.FloatField(
		help_text = 'Incremento Precio Crédito',
		default = 0 
	)	
	ultima_compra = models.DateField(
		help_text = 'Fecha de Ultima Compra',
		null = True, blank = True
	)	
	marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
	moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
	subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	IVA = (
       (0, 0),
       (5, 5),
       (10, 10),
   	)
	iva_valor = models.IntegerField(default=10)

	def __str__(self):
		return '{}:{}'.format(self.descripcion, self.marca.descripcion)

	def save(self):
		self.descripcion = self.descripcion.upper()
		self.unidad = self.unidad.upper()
		super(Producto, self).save()

	class Meta:
		verbose_name_plural = "Productos"	

