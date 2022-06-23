from django.contrib import admin

# Registramos post que esta en models aca

from .models import Post

admin.site.register(Post)
