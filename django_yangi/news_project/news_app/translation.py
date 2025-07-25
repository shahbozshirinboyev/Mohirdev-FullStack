from modeltranslation.translator import register, TranslationOptions, translator
from .models import News, Category

@register(News)
class NewsTranslationOptions(TranslationOptions):
  fields = ('title', 'body')

# translator.register(News, TranslationOptions)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
  fields = ('name',)
