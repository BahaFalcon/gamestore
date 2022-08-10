from django.contrib import admin
from django import forms
from .models import Game, Genre
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe


class GameAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Game
        fields = '__all__'


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Игры"""
    form = GameAdminForm
    list_filter = ('name',)
    list_display = ('id', 'name', 'price', 'available')
    list_display_links = ('id', 'name',)
    fields = ['name',  'genres', 'image', 'preview',
              'description', 'video_url', 'price', 'available']
    readonly_fields = ["preview"]
    search_fields = ('name__startswith',)
    list_per_page = 20
    ordering = ['created']
    save_on_top = True
    save_as = True

    def preview(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="430" height="330">')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ('title',)


admin.site.site_title = 'OYNOP-JYRGA'
admin.site.site_header = 'OYNOP-JYRGA'
