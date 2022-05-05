from django import forms

from .models import Proveedor, Compras



class ProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields = ['documento', 'razonsocial', 'direccion','contacto', 
			'telefono', 'email']
		labels = {'documento': "RUC y/o CI N°", 'razonsocial': "Razón Social", 
			'direccion': "Dirección", 'contacto': "Contacto", 
			'telefono': "Teléfono", 'email': "Email"}
		widget = {'documento': forms.TextInput}
	
	def __init__(self, *args,  **kwargs):
		super().__init__(*args,  **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})	
		self.fields['documento'].widget.attrs.update({'class': 'form-control'})	
		self.fields['razonsocial'].empty_label = "Razón Social"
		self.fields['direccion'].empty_label = "Dirección"

class ComprasForm(forms.ModelForm):
	class Meta:
		model = Compras
		fields = ['factura_tipo', 'factura_numero', 'factura_fecha','proveedor', 
			'moneda']
		widget = {'factura_tipo': forms.TextInput}
	
	def __init__(self, *args,  **kwargs):
		super().__init__(*args,  **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})	
		self.fields['factura_tipo'].widget.attrs.update({'class': 'form-control'})	
		self.fields['proveedor'].empty_label = "Seleccionar Proveedor"
		self.fields['moneda'].empty_label = "Seleccionar Categoria"

	