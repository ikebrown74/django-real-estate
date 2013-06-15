import realestate

from site_setup.models import *

def global_data(request):
	try:
		global_site_title = SiteTitle.objects.get(active=1)
		default_header_image = SiteHeaderImage.objects.get(active=1)
	
		site_data = {	'site_title': global_site_title.title,
						'title_sep' : global_site_title.seperator,
						'header_image' : default_header_image.image,
						'header_image_alt' : default_header_image.alt,
					}
	except:
		site_data = False
	return {'global_data' : site_data}
