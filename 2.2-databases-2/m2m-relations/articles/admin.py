from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticlePosition


class ArticlePositionInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            var = form.cleaned_data
            if var.get('is_main'):
                i += 1
            else:
                continue
        if i == 0:
            raise ValidationError('Выберите основной тег')
        elif i > 1:
            raise ValidationError('Основной тег должен быть один')
        return super().clean()


class ArticlePositionInline(admin.TabularInline):
    model = ArticlePosition
    formset = ArticlePositionInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ArticlePositionInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


