from django import forms
from .models import Article

class ArticleCreateForm (forms.ModelForm):
    """ Форма добавление статей на сайте """
    class Meta:
        model=Article
        fields =('title','slug', 'category','short_description','full_description','thumbnail','status')
    def __init__(self,*args,**kwargs):
        """ Обовление стилей формы Bootstrap """

        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'autocomplete':'off'
            })