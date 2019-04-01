from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="名称")
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True,
    	help_text="根据name生成的，用于生成页面URL，必须唯一", verbose_name="Slug")
    description = models.TextField(verbose_name="描述", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="是否激活")
    meta_keywords = models.CharField(max_length=255, null=True, blank=True,
    	help_text="meta关键词，用户seo搜索，用逗号分隔", verbose_name="Meta关键字")
    meta_description = models.CharField(max_length=255,null=True, blank=True,
    	help_text="meta描述", verbose_name="Meta描述")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")


    class Meta(object):
    	db_table = "categories"
    	ordering = ['-created_at']
    	verbose_name = "类别"
    	verbose_name_plural = "Categories"    		


    def __str__(self):
        return self.name

    def get_absolute_url(self):
    	return reverse('catelog_category', args=(self.slug,))


class Product(models.Model):	
    name = models.CharField("名称", max_length=255, unique=True)
    slug = models.SlugField("Slug", max_length=255, unique=True, null=True, blank=True,
    	help_text="根据name生成的，用于生成页面URL，必须唯一")
    brand = models.CharField("品牌", max_length=50, null=True, blank=True)
    sku = models.CharField("计量单位", max_length=50, null=True, blank=True)
    price = models.DecimalField("价格", default=0.00, max_digits=9, decimal_places=2)
    old_price = models.DecimalField("旧价格", max_digits=9, decimal_places=2, 
    	blank=True, default=0.00)
    image = models.ImageField("图片", max_length=50, null=True, blank=True)
    is_active = models.BooleanField("是否激活", default=True)
    is_bestseller = models.BooleanField("是否畅销", default=False)
    is_featured = models.BooleanField("是否推荐", default=False)
    quantity= models.IntegerField("数量", default=0)
    description = models.TextField("商品描述", null=True, blank=True)
    meta_keywords = models.CharField("Meta关键词", max_length=255, null=True, blank=True,
    	help_text="meta 关键词标签")
    meta_description = models.CharField("Meta描述", max_length=255, null=True, blank=True,
    	help_text="meta 描述标签")
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)
    categories = models.ManyToManyField(Category)


    class Meta(object):
    	db_table = "products"
    	ordering = ['-created_at']
    	verbose_name = "商品"
    	verbose_name_plural = "Products"

    def __str__(self):
    	return self.name

    def get_absolute_url(self):
    	return reverse('catelog_product', args=(self.slug,))

    def sale_price(self):
    	if self.old_price > self.price:
    		return self.price
    	else:
    		return None


class Order(object):
	order_no = models.CharField("订单编号", max_length=32, unique=True)
		

		
