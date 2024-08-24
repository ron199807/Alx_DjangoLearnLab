from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# customizing the admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

# book registration
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fiedsets = UserAdmin.fiedsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    admin.site.register(CustomUser, CustomUserAdmin)
