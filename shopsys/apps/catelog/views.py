from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from shopsys.apps.catelog import models

# Create your views here.

def my_custom_page_not_found_view():
	return render(req, '404.html')

def index(req, template_name):
	return render(req, template_name)


def category_home(req, template_name):
	page_title = '产品分类目录'
	return render(req, template_name, locals())


def category_list(req, category_slug, template_name):
	c = get_object_or_404(models.Category, slug=category_slug)
	products = c.product_set.all()
	page_title = c.name
	meta_keywords = c.meta_keywords
	meta_description = c.meta_description
	return render(req, template_name, locals())


def product_list(req, product_slug, template_name):
	p = get_object_or_404(models.Product, slug=product_slug)
	categories = p.categories.filter(is_active=True)
	page_title = p.name
	meta_keywords = p.meta_keywords
	meta_description = p.meta_description
	return render(req, template_name, locals())
