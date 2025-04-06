from django.contrib import admin
from django.conf import settings
from django.contrib.admin import AdminSite
from .models import Post, Comment, Contact

class BlogAdminSite(AdminSite):
    site_header = 'Daily Thoughts| ADMIN PANEL'
    site_title = 'Daily Thoughts | BLOGGING WEBSITE'
    index_title = ' Administration'
    site_url = '/'  # Link to your main site
    
    # Add custom CSS and JS for enhanced UI
    class Media:
        css = {
            'all': (
                'admin/css/admin_custom.css',
                'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap',
            )
        }
       
# Use the custom admin site
admin_site = BlogAdminSite(name='blog_admin')

# Register models with the custom admin site
admin_site.register(Post)
admin_site.register(Comment)
admin_site.register(Contact)

# Use the custom admin site
admin.site = admin_site