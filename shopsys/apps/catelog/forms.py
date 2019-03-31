from django import forms
from shopsys.apps.catelog import models

class ProductAdminForm(forms.ModelForm):
	"""docstring for ProductAdminForm"""
	class Meta:
		model = models.Product
		exclude = []

	def clean_price(self):
		if self.cleaned_data['price'] <= 0:
			raise forms.ValidationError('价格必须大于0.')
		return self.cleaned_data['price']

			
		