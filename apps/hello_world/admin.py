from django.contrib import admin
from filebrowser.sites import site

# Register your models here.
from django.contrib.admin import AdminSite

class HelloWorldAdmin(AdminSite):

    # Text to put in each page's <h1> (and above login form).
    admin.site.site_header = 'WebPres.org'
    admin.site.site_title = 'Cms Site Builder | WebPres,org'
    admin.site.index_title = 'Hello World'



admin_site = HelloWorldAdmin(name='hello_admin')
