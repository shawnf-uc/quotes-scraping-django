from django.contrib import admin

from .models import Author,Quote,QuoteJunction,Tag

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','dob','description')
    search_fields = ['name']


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote_text','author_name']
    search_fields = ['author__name']

    def author_name(self, obj):
        return obj.author.name

# class QuoteJunAdmin(admin.ModelAdmin):
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name']

admin.site.register(Author,AuthorAdmin)
admin.site.register(Quote,QuoteAdmin)
admin.site.register(QuoteJunction)
admin.site.register(Tag,TagAdmin)