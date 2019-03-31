from django.contrib import admin
from shopsys.apps.catelog import models
from shopsys.apps.catelog import forms

# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
	form = forms.ProductAdminForm
	list_display = ('name', 'brand', 'is_active', 'is_bestseller', 'is_featured',
		'quantity', 'price', 'old_price', 'created_at', 'updated_at')
	list_display_links = ('name',)
	list_per_page = 30
	ordering = ['-created_at']
	search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
	# 添加记录的时候不包括的字段，排除的字段
	exclude = ('created_at', 'updated_at', )
	# 添加记录的时候包括的字段，包括的字段
	field = ()
	prepopulated_fields = {'slug': ('name', )}


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'created_at', 'updated_at')
	list_display_links = ('name',)
	list_per_page = 20
	ordering = ['-created_at']
	search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
	exclude = ('created_at', 'updated_at', )
	prepopulated_fields = {'slug': ('name', )}
