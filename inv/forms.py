from django import forms

from .models import Moneda, Marca, Categoria, SubCategoria, Producto

from compras.models import Proveedor



class MonedaForm(forms.ModelForm):
	class Meta:
		model = Moneda
		fields = ['descripcion', 'simbolo', 'compras', 'ventas', 'maestra']
		labels = {'descripcion': "Descripción de la Moneda", 'simbolo': "simbolo de la moneda",
			'compras': 'Valor de Compras', 'ventas': 'Valor de Ventas', 'maestra': 'Si es moneda maestra'}
		widget = {'descripcion': forms.TextInput}
		compras = forms.IntegerField(min_value=1, 
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
		ventas = forms.IntegerField(min_value=1, 
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
	
	def __init__(self, *args,  **kwargs):
		super().__init__(*args,  **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})
		self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})	
		self.fields['descripcion'].empty_label = "Descripción de la Moneda"
		self.fields['simbolo'].empty_label = "Simbolo de la Moneda"
		#self.fields['compras'].widget.attrs['class'] = "text_type_number"
		#self.fields['ventas'].widget.attrs['class'] = "text_type_number"



class MarcaForm(forms.ModelForm):
	class Meta:
		model = Marca
		fields = ['descripcion']
		labels = {'descripcion': "Descripción de la Marca"}
		# fields = ['descripcion', 'estado']
		# labels = {'descripcion': "Descripción de la Categoria",
		# 		'estado': "Estado"}
		widget = {'descripcion': forms.TextInput}
	
	def __init__(self, *args,  **kwargs):
		super().__init__(*args,  **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})			

class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = ['descripcion']
		labels = {'descripcion': "Descripción de la Categoria"}
		# fields = ['descripcion', 'estado']
		# labels = {'descripcion': "Descripción de la Categoria",
		# 		'estado': "Estado"}
		widget = {'descripcion': forms.TextInput}
	
	def __init__(self, *args,  **kwargs):
		super().__init__(*args,  **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})			

class SubCategoriaForm(forms.ModelForm):
	categoria = forms.ModelChoiceField(
		queryset=Categoria.objects.filter(estado=True)
		.order_by('descripcion')
	)
	class Meta:
		model = SubCategoria
		fields = [ 'descripcion', 'categoria']
		labels = {'descripcion': "Descripción de la Sub Categoria"}
		widget = {'descripcion': forms.TextInput}
	
	def __init__(self, *args,  **kwargs):
		super().__init__(*args,  **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})
		self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})	
		self.fields['descripcion'].empty_label = "Descripción de la Categoria"
		self.fields['categoria'].empty_label = "Seleccionar Categoria"								


class ProductoForm(forms.ModelForm):
	subcategoria = forms.ModelChoiceField(
		queryset=SubCategoria.objects.filter(estado=True)
		.order_by('descripcion')
	)
	proveedor = forms.ModelChoiceField(
		queryset=Proveedor.objects.filter(estado=True)
		.order_by('razonsocial')
	)	
	marca = forms.ModelChoiceField(
		queryset=Marca.objects.filter(estado=True)
		.order_by('descripcion')
	)
	moneda = forms.ModelChoiceField(
		queryset=Moneda.objects.filter(estado=True)
		.order_by('descripcion')
	)	
	detalle = forms.CharField(widget=forms.Textarea(attrs={'rows':10}))	


	class Meta:
		model = Producto
		fields = ['codigo_barra', 'descripcion', 'unidad', 'existencia_inicial',
			'existencia_actual', 'precio_costo', 'precio_venta', 'descuento_maximo',
			'incremento_precio_credito', 'ultima_compra', 'subcategoria', 'marca',
			'moneda', 'proveedor', 'imagen', 'detalle', 'iva_valor']
		labels = {'descripcion': "Descripción del Producto"}
		widget = {'descripcion': forms.TextInput}
	
	def __init__(self, *args,  **kwargs):
		super().__init__(*args,  **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})
		self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})	
		self.fields['descripcion'].empty_label = "Descripción del producto"
		self.fields['subcategoria'].empty_label = "Seleccionar Sub Categoria"			
		self.fields['marca'].empty_label = "Seleccionar Marca"					
		self.fields['moneda'].empty_label = "Seleccionar Moneda"							
		self.fields['proveedor'].empty_label = "Seleccionar Proveedor"	
		self.fields['iva_valor'].empty_label = "Seleccionar Valor de Iva"	
		self.fields['precio_costo'].widget.attrs['class'] = "form-control"
		self.fields['precio_venta'].widget.attrs['class'] = "form-control"
		self.fields['descuento_maximo'].widget.attrs['class'] = "form-control"
		self.fields['incremento_precio_credito'].widget.attrs['class'] = "form-control"
		self.fields['existencia_actual'].widget.attrs['class'] = "form-control"
		self.fields['existencia_inicial'].widget.attrs['class'] = "form-control"
		
		#widget=forms.Textarea()								