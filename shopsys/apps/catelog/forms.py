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


class ProductAddToCart(forms.Form):
	quantity = forms.IntegerField(
		label='数量',
		widget=forms.TextInput(attrs={
			'size': '2',
			'value': '1',
			'class': 'quantity',
			'maxlength': '5'
		}),
		error_messages={'invalid': '请输入有效值！'},
		min_value=1
	)
	product_slug = forms.CharField(widget=forms.HiddenInput())

	def __init__(self, request=None, *args, **kwargs):
		self.request = request
		super(ProductAdminForm, self).__init__(*args, **kwargs)
		
	def clean(self):
		"""检查用户浏览器是否启用cookie"""
		if self.request:
			if not self.request.session.test_cookie_worked():
				raise forms.ValidationError('需要启用Cookie!')
		return self.cleaned_data
		