from django.conf.urls import url
from shopsys.apps.catelog import views



urlpatterns = [
	url(r'^$', views.category_home, {'template_name': 'catelog/index.html'}, 'category_home'),
	url(r'^category/(?P<category_slug>[-\w]+)/$', views.category_list,
		{'template_name': 'catelog/category.html'}, 'category_list'),
	url(r'^product/(?P<product_slug>[-\w]+)/$', views.product_list,
		{'template_name': 'catelog/product.html'}, 'product_list'),
]