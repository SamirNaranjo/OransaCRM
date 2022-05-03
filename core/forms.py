from cProfile import label
from django.forms import ModelForm, TextInput, Textarea
from .models import Category

class CategoryForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class']= 'form-control'
        #     form.field.widget.attrs['autocomplete']= 'off'
        self.fields['name'].widget.attrs['autofocus']= True
    

    class Meta:
        model = Category
        fields = ('__all__')
        widgets={
            'name': TextInput(
                attrs={
                    'placeholder':'Ingrese Descripcion'
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder':'Ingrese Descripcion',
                    'rows':3,
                    'cols':3
                }
            ),

        }
    

    def clean(self):
        cleaned=super().clean()
        if len(cleaned['name']) <= 50:
            self.add_error('name', 'Faltan Caracteres')
        return cleaned    