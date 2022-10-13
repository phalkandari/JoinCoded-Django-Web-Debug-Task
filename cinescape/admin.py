from django.contrib import admin
from .models import (
    Category,
    Movies,
    Location,
    Theater)

admin.site.register(
    [
        Category,
        Movies,
        Location,
        Theater,
    ]
)
