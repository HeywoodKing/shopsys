from shopsys import settings
from shopsys.apps.catelog import models

# 全局可用变量
def shopsys(req):
	return {
		'active_categories': models.Category.objects.filter(is_active=True),
		'site_name': settings.SITE_NAME,
		'meta_keywords': settings.META_KEYWORDS,
		'meta_description': settings.META_DESCRIPTION,
		'request': req
	}